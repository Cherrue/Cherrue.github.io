import string
import feedparser
from bs4 import BeautifulSoup
import requests
import re
from textrankr import TextRank  # https://github.com/theeluwin/textrankr
from typing import List
from konlpy.tag import Okt
from datetime import datetime, date, timedelta
import csv

TARGET_BLOG_LIST_FILE_URL = "./target_blog_list.csv"
POST_PATH = "../../../_posts/weekly-tech-blog/"
PERIOD_PARSING = 7
NUM_SUMMARIZED_SENTENCE = 3


class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens


def get_blog_list():
    result = list()
    with open(TARGET_BLOG_LIST_FILE_URL, "r") as target_blog_list_file:
        csv_reader = csv.reader(target_blog_list_file)
        next(csv_reader, None)  # skip header
        for row in csv_reader:
            result.append(row)
    return result


def get_post_url():
    return POST_PATH + f"{date.today().strftime('%Y-%m-%d')}-weekly-tech-blog-follow-up.md"


def get_document_header(_base_date: date):
    month = _base_date.month
    week = _base_date.isocalendar()[1]\
        - date(_base_date.year, _base_date.month, 1).isocalendar()[1]\
        + 1

    return f'''\
---
layout: single
title: \[기술블로그\] {month}월 {week}주 주간 기술블로그 Follow Up
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

{_base_date} ~ {_base_date + timedelta(PERIOD_PARSING)} 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

'''


def get_document_footer():
    return '''\
* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
'''


def validate_feed(_base_date, _feed):
    # find upload date
    if 'published_parsed' in _feed.keys():
        update_date = date(*_feed.published_parsed[:3])
    elif 'updated_parsed' in _feed.keys():
        update_date = date(*_feed.updated_parsed[:3])
    else:
        return False

    # validate date
    if update_date < _base_date:
        return False
    elif update_date > _base_date + timedelta(PERIOD_PARSING):
        return False

    # find content
    if 'content' not in _feed.keys() and 'summary_detail' in _feed.keys():
        return False
    else:
        return True


def parse_feed(_base_date, _feed):
    if 'content' in _feed.keys():
        html = _feed.get('content')[0].get('value')
    elif 'summary_detail' in _feed.keys():
        html = _feed.get('summary_detail').get('value')

    soup = BeautifulSoup(html)

    my_tokenizer: OktTokenizer = OktTokenizer()
    text_rank: TextRank = TextRank(my_tokenizer)
    summaries: List[str] = text_rank.summarize(
        soup.get_text(), NUM_SUMMARIZED_SENTENCE, verbose=False)

    list_result = list()
    list_result.append(f"## [{_feed.title}]({_feed.link})")

    for summary in summaries:
        s = summary.split(' ')
        result = ""
        for word in s:
            result = result + ' ' + ''.join(c for c in word if c.isalnum())
        list_result.append(result)

    return list_result


def parse_blog(_base_date: date, _name: string, _url: string):
    feeds = feedparser.parse(_url).entries

    list_result = list()
    list_result.append(f"# [{_name}]({_url})")
    for feed in feeds:
        if validate_feed(_base_date, feed):
            list_result.extend(parse_feed(_base_date, feed))
    list_result.append("---\n\n")

    return list_result


def get_contents(_base_date: date):
    contents = ""
    tech_blog_urls = get_blog_list()
    list_result = list()
    for name, url in tech_blog_urls:
        list_result.extend(parse_blog(_base_date, name, url))

    return "\n\n".join(list_result)


def main():
    base_date = date.today() - timedelta(PERIOD_PARSING)

    header = get_document_header(base_date)
    contents = get_contents(base_date)
    footer = get_document_footer()

    with open(get_post_url(), mode="w", encoding="utf-8") as post_file:
        post_file.write(header)
        post_file.write(contents)
        post_file.write(footer)


if __name__ == "__main__":
    main()
