# Weekly Tech Blog Parser

## Environments

| env | name | version | detail |
| --- | --- | --- | --- |
| language | python | python3 | 3.8.5 |

## Requirements

| library | version | comment |
| --- | --- | --- |
| feedparser | latest(6.0.10) | RSS 파싱을 위함 |
| textrankr | latest(1.1)) | 세 줄 요약을 위한 pagerank의 변형 라이브러리 |
| konlpy | latest(0.6.0) | 한국어 형태소 분석을 위함 |

## Schedules

1 0 * * 1
매주 월요일 00시 01분 실행

## Flows

![flow](/assets/images/weekly-blog-parser.drawio.png)