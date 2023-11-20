---
layout: single
title: \[기술블로그\] 11월 3주 주간 기술블로그 Follow Up
date: 2023-11-20 01:23:35 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-11-13 ~ 2023-11-20 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

## [데이터 품질 이슈로 발생하는 data downtime을 줄이자](https://d2.naver.com/helloworld/5766317)

 데이터 품질

 위와 같은 일을 도와주는 데이터 품질 도구가 이미 많이 나와 있다

 데이터 품질 규칙

## [Kotlin으로 Cli를 만든다고?](https://d2.naver.com/helloworld/2236952)

 네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY10월에서 발표되었던 세션을 공개합니다

  NAVER ENGINEERING DAY란

 그중 1년에 3번씩 열리고 있는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

## [Feed Infra팀을 소개해요!](https://medium.com/daangn/feed-infra%ED%8C%80%EC%9D%84-%EC%86%8C%EA%B0%9C%ED%95%B4%EC%9A%94-e77d132afbdf?source=rss----4505f82a2dbd---4)

 위와 같은 이유로 피드 서비스에서는 2가지에집중했는데요

 그러다 피드 서비스가 모든 것을 모은 후 노출 하는 것이 아니라 각 서비스들이 피드에 노출할 수 있는 규약을 만들고 전달한 콘텐츠를 정하는 권한을 위임해야겠다고 생각했어요

 피드 서비스에 정의되어있는 규칙에 의해서 중고차 당근알바 등 콘텐츠를 노출할 수 있게 해 주었어요

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [따끈따끈한 전사 로그 시스템 전환기: ELK Stack에서 Loki로 전환한 이유](https://techblog.woowahan.com/14505/)

 각 서비스에서 발생하는 대부분의 로그를 수집해야하기 때문에 종류가 많고  비용이 많이 발생하지 않는지 시스템 운영을 효율적으로 하고 있는지 데이터를 효율적으로 저장하고 있는지 등 항상 풀어야 하는 숙제가 있습니다

 특히 로그 시스템은 HighWrite LowRead 패턴으로 많은 데이터를 수집하지만 그에 비해 조회는 수집된 모든 데이터를 대상으로 하지 않습니다

 우아한형제들에서는 로그 시스템으로 ELK Stack을 사용하고 있었습니다

---



# [kakao Tech](https://tech.kakao.com/feed/)

---



# [WATCHA 팀 블로그](https://medium.com/feed/watcha)

---



# [무신사 기술 블로그](https://medium.com/feed/musinsa-tech)

---



# [야놀자](https://medium.com/feed/yanolja)

---



# [직방 TECH](https://medium.com/feed/zigbang)

---



# [Google Developers](https://developers.googleblog.com/feeds/posts/default?alt=rss)

---



# [Amazon Science Blog](https://www.amazon.science/index.rss)

---



# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/feed)

## [Psyberg: Automated end to end catch up](https://netflixtechblog.com/3-psyberg-automated-end-to-end-catch-up-260fbe366fe2?source=rss----2615bd06b42e---4)

 WriteApply the ETL business logic to the input data identified in Step 1 and write to an unpublished iceberg snapshot based on the Psybergmodeb

 CalloutsHaving the Psyberg step isolated from the core data pipeline allows us to maintain a consistent pattern that can be applied across stateless and stateful processing pipelines with varying requirements

 The Psyberg initialization for the cancel fact identifies late data from hour 5 and additional data from hours 6 and 7 Since this ETL operates in stateful mode the data in the target table from hours 5 to 7 will be overwritten with the newdata

## [Diving Deeper into Psyberg: Stateless vs Stateful Data Processing](https://netflixtechblog.com/2-diving-deeper-into-psyberg-stateless-vs-stateful-data-processing-1d273b3aaefb?source=rss----2615bd06b42e---4)

 Similar to the approach in stateless data processing Psyberg uses the provided inputs to parse out the partition information for each Iceberg snapshot of the sourcetable

 Any latearriving signup events data is appended to the target table partitions as part of this

 Audits like sourcetotarget count comparison and checking for no missing events in the target Iceberg snapshot ensure data integrity and completeness

## [1. Streamlining Membership Data Engineering at Netflix with Psyberg](https://netflixtechblog.com/1-streamlining-membership-data-engineering-at-netflix-with-psyberg-f68830617dd1?source=rss----2615bd06b42e---4)

 We expect complete and accurate data at the end of each run

 Step 3 Identify the number of partitions to be rerun for the sequential stateful load jobs to account for the delayed data and rerun them from the impacted datehour

 One of the critical features of Psyberg is its ability to detect and manage latearriving data no matter the partition it lands in

## [Detecting Speech and Music in Audio Content](https://netflixtechblog.com/detecting-speech-and-music-in-audio-content-afd64e6a5bf8?source=rss----2615bd06b42e---4)

 Like semantic segmentation for audio SMAD separately tracks the amount of speech and music in each frame in an audio file and is useful in content understanding tasks during the audio production and delivery lifecycle

 The detailed temporal metadata SMAD provides about speech and music regions in a polyphonic audio mixture are a first step for structural audio segmentation indexing and preprocessing audio for the following downstream tasks

 TVSM is significantly larger than other SMAD datasets and contains both speech and music labels at the frame level

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [Watch: Meta’s engineers on building network infrastructure for AI](https://engineering.fb.com/2023/11/15/networking-traffic/watch-metas-engineers-on-building-network-infrastructure-for-ai/)

 But the sheer scale and complexity of GenAI models means new challenges for Metas network infrastructure

 Hany Morsy and Susana Contrera delve into how Metas network builds have evolved to support the needs of AI services

 He sheds light on how Metas infrastructure is designed to both maximize the raw performance and consistency that is fundamental for AIrelated workloads

---



# [slack engineering](https://slack.engineering/feed/)

## [The Query Strikes Again](https://slack.engineering/the-query-strikes-again/)

 This means that an enormous number of database queries were sent to the multiple Vitess shards

 The purpose of the leave channel job was to unsubscribe a user from all of the threads that they were subscribed to in that channel

 For some users this was tens of thousands of subscription IDs which is very expensive for the database to process

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
