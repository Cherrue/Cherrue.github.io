---
layout: single
title: \[기술블로그\] 10월 2주 주간 기술블로그 Follow Up
date: 2023-10-09 01:18:26 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-10-02 ~ 2023-10-09 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

## [FE News 10월 소식](https://d2.naver.com/news/8498532)

 Turbo와 Svelte 개발에는 타입스크립트를 사용하지 않는다는데 우리도 타입스크립트를 벗어날 때인가

  FE News 10월 보러가기

  FE News란

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

## [당근페이 입사 후 비로소 알게 된 것들](https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%ED%8E%98%EC%9D%B4-%EC%9E%85%EC%82%AC-%ED%9B%84-%EB%B9%84%EB%A1%9C%EC%86%8C-%EC%95%8C%EA%B2%8C-%EB%90%9C-%EA%B2%83%EB%93%A4-09a7620c0404?source=rss----4505f82a2dbd---4)

 일상을 더 편리하게 하는 당근페이 같은 핀테크 서비스 이제 제법 익숙해진 서비스지만 핀테크라는 회사를 입사하기로 결심할 때는 또 새롭게 바라보게 됐던 것같아요

 당근페이에 입사한 지 어느덧 1년이 되어가는 당근페이 백엔드 엔지니어로서 그런 고민을 어떻게 해결해 나갔는지 이야기해 보려고 해요

 이런 성장은 당근페이 구성원들과 함께했기에 가능했다고생각하고요

## [MySQL Gap Lock (두번째 이야기)](https://medium.com/daangn/mysql-gap-lock-%EB%91%90%EB%B2%88%EC%A7%B8-%EC%9D%B4%EC%95%BC%EA%B8%B0-49727c005084?source=rss----4505f82a2dbd---4)

 datalocks ENGINETRANSACTIONID  INDEXNAME  LOCKTYPE  LOCKMODE      LOCKSTATUS  LOCKDATA                             1890665  NULL        TABLE      IX             GRANTED      NULL                                  1890665  PRIMARY     RECORD     XRECNOTGAP  GRANTED      26                                    1890665  PRIMARY     RECORD     X              GRANTED      supremum pseudorecord                1890665  PRIMARY     RECORD     X              GRANTED      27                     SESSION1  BEGINSESSION1 SELECT  FROM locksupremum2 WHERE id BETWEEN 81 AND 82 FOR UPDATESESSION1 SELECT  FROM performanceschema

 datalocks ENGINETRANSACTIONID  INDEXNAME  LOCKTYPE  LOCKMODE      LOCKSTATUS  LOCKDATA                             1890666  NULL        TABLE      IX             GRANTED      NULL                                  1890666  PRIMARY     RECORD     XRECNOTGAP  GRANTED      81                                    1890666  PRIMARY     RECORD     X              GRANTED      supremum pseudorecord                1890666  PRIMARY     RECORD     X              GRANTED      82                     SESSION1  BEGINSESSION1 SELECT  FROM locksupremum2 WHERE id BETWEEN 136 AND 137 FOR UPDATESESSION1 SELECT  FROM performanceschema

 하지만 id82 레코드를 INSERT하면 2번째 리프 페이지pageno6의 supremum pseudorecord 에 걸려있는 배타적 잠금 때문에 실행되지 못하고 대기해요

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [[모집] 우아한테크코스 2024 신입생을 모집합니다](https://techblog.woowahan.com/14072/)

 우아한테크코스의 인재상

 우아한테크코스 홈페이지  지원하기 httpswww

 우아한테크코스 FAQ

## [[모집] 우아한스터디 2023 겨울시즌](https://techblog.woowahan.com/14224/)

 이 글은 PC 환경에 최적화되어 있습니다

 모바일 환경에서는 우아한스터디 2023 겨울시즌 페이지와 우아한스터디 2023 겨울시즌 신청서를 참고하세요

 The post 모집 우아한스터디 2023 겨울시즌 first appeared on 우아한형제들 기술블로그

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

## [7 dos and don'ts of using ML on the web with MediaPipe](http://developers.googleblog.com/2023/10/7-dos-and-donts-of-using-ml-on-web-with-mediapipe.html)

 View the guides in the docs and try out the web demos on Codepen to see how simple it is to get started

 Keep in mind that these samples are meant to be as simple as possible so you can understand the code and apply it to your own use case

 You can use MediaPipe Studio to test devices as well so you know right away that a solution will work on your users devices

## [#WeArePlay | Meet Solape and Yomi from Nigeria. More stories from around the world](http://developers.googleblog.com/2023/10/weareplay-meet-solape-and-yomi-from-nigeria-more-stories-from-around-the-world.html)

 This month hear about a game changing financial app for women in Nigeria to an early learning platform that uses augmented reality

 Intent on improving gender equality in the financial sphere the pair plan to reach a million women by the end of 2024 and become the goto financial platform for the financially underserved in Africa

 After being offered a place on an accelerator program they moved to Chile to launch PleIQ  an immersive early learning app for kids aged 38 Next theyre expanding across Latin America with the goal of improving education quality to create a more equal society

## [Make with MakerSuite Part 2: Tuning LLMs](http://developers.googleblog.com/2023/10/make-with-makersuite-part-2-tuning-llms.html)

 Tuning in MakerSuite uses a technique called Parameter Efficient Tuning PET to produce customized highquality models without the additional costs and complexity of traditional finetuning

 3 View your tuned model

 Tuning in MakerSuite empowers developers to harness the full potential of models like PaLM 2 with delightful ease

## [Build with Google AI: new video series for developers](http://developers.googleblog.com/2023/10/build-with-google-ai-new-video-series-for-developers.html)

 The open source projects featured in the series are selected so that you can get them working quickly and then build beyond them

 AI Coding Assistant with Pipet Code Agent 1017 Well show you how the AI Developer Relations team at Google built a coding assistance agent as an extension for Visual Studio Code and how you can take their open source project and make it work for your development workflow

 We hope you are as excited about the Build with Google AI video series as we are to share it with you

## [Improving user safety in OAuth flows through new OAuth Custom URI scheme restrictions](http://developers.googleblog.com/2023/10/enhancing-oauth-app-impersonation-protections.html)

 New Chrome extensions will be required to use the Chrome Identity API method for authorization

 In the future we may disallow Custom URI scheme methods and require all extensions to use the Chrome Identity API method

 By default new Android apps will no longer be allowed to use Custom URI schemes to make authorization requests

---



# [Amazon Science Blog](https://www.amazon.science/index.rss)

---



# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/feed)

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

## [Building Resilience in the Face of Disruption: LinkedIn's Journey to ISO 22301 Certification](https://engineering.linkedin.com/blog/2023/building-resilience-in-the-face-of-disruption--linkedin-s-journe)

 We wanted to demonstrate our commitment to continuity and resilience to our customers and thats one of the reasons why we pursued ISO 22301 business continuity certification

 This was critical in demonstrating our continued commitment to program maturity and our readiness for ISO 22301 certification

 Our ISO 22301 certification helps us assure our customers that we are prepared to support them in the event of any major disruption

## [How LinkedIn Is Using Embeddings to Up Its Match Game for Job Seekers](https://engineering.linkedin.com/blog/2023/how-linkedin-is-using-embeddings-to-up-its-match-game-for-job-se)

 LinkedIn is on the forefront of leveraging EBR technology to revolutionize the way we approach search and recommendation systems

 You can think of the request embedding as encapsulating the contextual intent of the search or recommendation request in such a way that geometric proximity in the embedding space shared by the request embedding and the EBR index is highly correlated with similarity of meaning

 The implementation of EBR at LinkedIn has significantly improved the ability to deliver personalized and relevant content to our members and customers

## [Career stories: The math-music connection in data science](https://engineering.linkedin.com/blog/2023/career-stories--the-math-music-connection-in-data-science)

 My team and mentors were welcoming and flexible with me as I leaned into my role and adapted to how we work at LinkedIn

 I visit the Mountain View office each quarter to share coffee lunch and thoughts about our projects at LinkedIn with my team members

 In my role at LinkedIn Im on one of the consumerfacing teams responsible for the algorithm recommending the feed to LinkedIn members

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [Meta contributes new features to Python 3.12](https://engineering.fb.com/2023/10/05/developer-tools/python-312-meta-new-features/)

 This weeks release of Python 312 marks a milestone in our efforts to make our work developing and scaling Python for Metas use cases more accessible to the broader Python community

 We have also been working closely with the Python community to introduce new features and optimizations to improve Pythons performance and to allow third parties to experiment with Python runtime optimization more easily

 We are grateful to be a part of this open source community and look forward to working together to move the Python programming language forward

---



# [slack engineering](https://slack.engineering/feed/)

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
