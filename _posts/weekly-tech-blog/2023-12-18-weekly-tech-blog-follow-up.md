---
layout: single
title: \[기술블로그\] 12월 3주 주간 기술블로그 Follow Up
date: 2023-12-18 01:23:09 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-12-11 ~ 2023-12-18 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

## [AI 플랫폼을 위한 스토리지 JuiceFS 도입기](https://d2.naver.com/helloworld/4555524)

 JuiceFS의 성능은 어떤 저장소를 데이터 스토리지로 사용하는지에 따라 다를 것이다

 즉 nubes에 데이터 스토리지로 JuiceFS를 사용해도 성능 저하는 없다

 JuiceFS의 성능은 기본적으로는 데이터 스토리지로 사용하는 저장소의 성능에 수렴한다

## [One-Source Multi-Use, 스마트플레이스 일본 진출 작업기](https://d2.naver.com/helloworld/0983091)

 네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY10월에서 발표되었던 세션을 공개합니다

 Onesource Multiuse를 위한 분기

  NAVER ENGINEERING DAY란

## [거기 말고 이 호텔 어때? - 호텔 서비스 추천 시스템 도입기](https://d2.naver.com/helloworld/2184045)

 모델 선택과 학습에 앞서 사용할 데이터를 선택해야 한다

 모델 서빙은 BentoML을 사용하여 진행한다

 추천 시스템 알고리즘에 대중화되어 있는 협업 필터링에서 행렬 분해ALS를 사용해서 실제 서비스에 적용하는 과정을 살펴 보았다

## [데이터 품질 이슈로 발생하는 data downtime을 줄이자](https://d2.naver.com/helloworld/5766317)

 데이터 품질

 위와 같은 일을 도와주는 데이터 품질 도구가 이미 많이 나와 있다

 데이터 품질 규칙

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [[신청 시작] 12월 우아한테크세미나: WOOWACON 2023 리캡](https://techblog.woowahan.com/15488/)

 12월 우아한테크세미나  WOOWACON 2023 리캡

 그전에 12월 우아한테크세미나를 통해 좋은 반응이 정말 많았던 두 세션 발표자분들을 모시고 WOOWACON 2023 리캡 자리를 마련했습니다

 마이크로프론트엔드를 도입한 이유

## [Java의 미래, Virtual Thread](https://techblog.woowahan.com/15398/)

 Virtual Thread

 Virtual Thread 톺아보기

 Virtual Thread의 parkunpark

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

## [Our First Netflix Data Engineering Summit](https://netflixtechblog.com/our-first-netflix-data-engineering-summit-f326b0589102?source=rss----2615bd06b42e---4)

 The TalksThe Netflix Data Engineering StackChris Stephens Data Engineer Content  Studio and Pedro Duarte Software Engineer Consolidated Logging walk engineers new to Netflix through the building blocks of the Netflix Data Engineering stack

 You can read more about Data Mesh Netflixs nextgeneration stream processing platform hereBuilding Reliable Data PipelinesHolden Karau OSS Engineer Data Platform Engineering talks about the importance of reliable data pipelines and how to build them covering tools from testing to validation and auditing

 Mick Dreeling ChrisColburnOur First Netflix Data Engineering Summit was originally published in Netflix TechBlog on Medium where people are continuing the conversation by highlighting and responding to this story

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

## [Extracting skills from content to fuel the LinkedIn Skills Graph](https://engineering.linkedin.com/blog/2023/extracting-skills-from-content-to-fuel-the-linkedin-skills-graph)

 The assumption is that entities and text are available information in each skill vertical and the extent to which they affect skill extraction is similar

 After the skills extraction we collect contextual skill data and job application data to identify the most important and relevant skills for a members career

 Building an accurate and comprehensive skill profile for jobs is the foundation of our skillsfirst initiatives

## [Privacy Preserving Single Post Analytics](https://engineering.linkedin.com/blog/2023/privacy-preserving-single-post-analytics)

  To handle this with noise we then introduce a seed to our randomized algorithms and use the number of distinct viewers on the post as part of the seed

 Although we can ensure that analytics will remain the same if there are no new viewers we still want to update the results after each new viewer and there can be thousands of viewers or more

  Hence for the Binary Mechanism the overall privacy loss will only scale logarithmically with the number of viewers and each count will have at most logarithmically many noise terms added to it

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

---



# [slack engineering](https://slack.engineering/feed/)

## [Our Journey Migrating to AWS IMDSv2](https://slack.engineering/our-journey-migrating-to-aws-imdsv2/)

 As an organization we rely heavily on IMDS to get insights into our instances during provisioning and the lifecycle of these instances

 This allowed the service teams to install this tool on demand and investigate IMDSv1 calls

 We blocked the ability to launch instances with IMDSv1 support and also blocked the ability to turn on IMDSv1 on existing instances

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
