---
layout: single
title: \[기술블로그\] 5월 3주 주간 기술블로그 Follow Up
date: 2023-05-22 01:44:58 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-05-15 ~ 2023-05-22 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

## [MySQL Optimizer Error](https://medium.com/daangn/mysql-optimizer-error-e438aa02e622?source=rss----4505f82a2dbd---4)

 SELECT  INDEXtab ixbidcreatedat  COUNT FROM tabWHERE bid1198442   AND createdatDATESUBNOW INTERVAL 9 HOURSELECT  INDEXtab ixbidid  COUNT FROM tabWHERE bid1198442   AND id14025956힌트를 사용한 쿼리의 실행 계획을 한번 살펴보면 다음과 같아요

 이 결과만 보면 옵티마이저는 ixbidid 인덱스를 사용하는 실행 계획이 더 빠를 것이라고 예측했다는 것을 알 수 있죠

 mysql EXPLAIN SELECT COUNT FROM tab WHERE bid1198442 AND createdatDATESUBNOW INTERVAL 9 HOUR type   key               keylen  ref   rows     filtered  Extra                     range  ixbidcreatedat  14       NULL  1490996    10000  Using where Using index 쿼리의 실행 계획이 ixbidcreatedat 인덱스를 사용하도록변경되었어요

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [우아한형제들에서 PM끼리 소통하는 법 – 카르페피엠](https://techblog.woowahan.com/11642/)

 카르페피엠에서는 PM들의 질문사항을 익명으로 접수받고 있는데요

 PM들이 궁금해 하시는 것들을 모아서 카르페피엠에서 답변드리려고 하고 있어요

 PM 스터디

## [배민상회와 검색플랫폼 연동기](https://techblog.woowahan.com/11732/)

 배민상회와 검색플랫폼 연동 개략도출처 내가 그린 그림

 설명을 보면 알겠지만 배민상회와 검색플랫폼의 연동은 매우 간단해 보입니다

 배민상회에서 다수의 개발 존은 당연한 것이었고 검색플랫폼에서는 당연한 것이 아니었습니다

## [배민 앱 리뷰 품질을 향상시킨 방법은? 머신 러닝 X 네트워크 탐지 모델 도입](https://techblog.woowahan.com/11829/)

 Deep SAD는 라벨 데이터가 있는 경우에는 준지도 이상 탐지로 동작하고 라벨 데이터가 없는 경우에는 비지도 이상 탐지로 동작하는 알고리즘입니다

 Deep SAD는 준지도 학습 알고리즘이기 때문에 비지도 이상 탐지와 달리 라벨 데이터를 학습에서 사용합니다

 다음 그림은 준지도 학습 이상 탐지 알고리즘인 Deep SAD와 네트워크 탐지 방법을 결합한 리뷰 조작 업체 탐지 모델의 구성도입니다

---



# [kakao Tech](https://tech.kakao.com/feed/)

---



# [WATCHA 팀 블로그](https://medium.com/feed/watcha)

---



# [무신사 기술 블로그](https://medium.com/feed/musinsa-tech)

## [무신사 QA 엔지니어 업무 전격 파헤치기!](https://medium.com/musinsa-tech/qaengineer-roles-and-responsibilities-d1fc088c7a43?source=rss----f107b03c406e---4)

 매끄러운 무신사 서비스를 위해 품질을 보증하고 새롭게 업데이트 되는 다양한 기술들이 안정적으로 배포되어 고객에게 제공될 수 있도록 힘쓰는 무신사의 QA그룹의 업무를소개합니다

 첫번째로 테스팅은 QA에게 있어서 가장 기본적이고 필수적인 업무입니다

 그림4 일단위 자동화 테스트를 통한 주요 기능점검QA그룹의 업무는 어떻게진행되나요

---



# [야놀자](https://medium.com/feed/yanolja)

---



# [직방 TECH](https://medium.com/feed/zigbang)

---



# [Google Developers](https://developers.googleblog.com/feeds/posts/default?alt=rss)

## [Jetpack Compose Buttons for Google Pay and Google Wallet](http://developers.googleblog.com/2023/05/jetpack-compose-buttons-for-google-pay-google-wallet.html)

 Weve now made the new Google Pay button available to Jetpack Compose developers with a new open source library composepaybutton

 Jetpack Compose is Androids modern toolkit for building user interfaces when using the Kotlin language and with this new library you can implement the Google Pay button in your Android apps with even less code than before

 Figure 2 Both regular and condensed versions of the Google Wallet button are available in the new library

## [How Web GDE Martine Dowden approaches web design from an accessibility perspective](http://developers.googleblog.com/2023/05/global-accessibility-awareness-day-gde-martine-dowden.html)

 One principle that might not be top of mind when looking at our favorite sites is accessibility and when applying it to web design its purpose is to make sites available to everyone

 Martine is the CTO of Andromeda Galactic Solutions where she builds sites for her clients with an accessibility approach

 This resource provides specs and a lot of supporting documentation that explains why the specs exist but it is an exhaustive resource that Martine doesnt recommend reading from beginning to end

## [Powering Talking Characters with Generative AI](http://developers.googleblog.com/2023/05/generative-ai-talking-character.html)

 We also provide an example of how personality and backstory can be changed to assume the persona of a reliable insurance agent  or anything else for that matter

 First provide developers and users with a test interface to experiment with the powerful concept of prompt engineering for character development and leveraging specific datasets on top of the PaLM API to create unique experiences

 Googles Partner Innovation team has developed a series of Generative AI Templates showcasing the possibilities when combining LLMs with existing Google APIs and technologies to solve specific industry use cases

## [Generative AI ‘Food Coach’ that pairs food with your mood](http://developers.googleblog.com/2023/05/generative-ai-recipe-developers.html)

 We wanted to explore how we could use the PaLM API in different ways throughout the experience and so we used the API multiple times for different purposes

 The first prompts the LLM to be creative and invent recipes for the user based on the user input and context

 The messages is an array of chat messages from past to present alternating between the user author0 and the LLM author1

---



# [Amazon Science Blog](https://www.amazon.science/index.rss)

---



# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/feed)

## [Debugging a FUSE deadlock in the Linux kernel](https://netflixtechblog.com/debugging-a-fuse-deadlock-in-the-linux-kernel-c75cd7989b6d?source=rss----2615bd06b42e---4)

 If the kernel is currently doing something on behalf of the task the signal may be pending

 When were shutting down the pid namespace in zappidnsprocesses itdoesgroupsendsiginfoSIGKILL SENDSIGPRIV task PIDTYPEMAXwhich eventually gets to sendsignallocked whichhaspending  type

 If we look at the fatalsignalpending code weseestatic inline int fatalsignalpendingstruct taskstruct p        return unlikelysigismemberppending

## [ABAC on SpiceDB: Enabling Netflix’s Complex Identity Types](https://netflixtechblog.com/abac-on-spicedb-enabling-netflixs-complex-identity-types-c118f374fa89?source=rss----2615bd06b42e---4)

  SpiceDB is then responsible for figuring out which relations map back to the autoscaling group e

 All this meant that Netflix would have to write and prune the relationship state with significant freshness requirements

 SpiceDB Caveats simplify this approach by allowing Netflix to specify authorization policy as they have in the past for applications

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [MSVP is Meta’s first video processing ASIC](https://ai.facebook.com/blog/meta-scalable-video-processor-MSVP)

 The post MSVP is Metas first video processing ASIC appeared first on Engineering at Meta

## [Meta introduces its first-generation AI inference accelerator](https://ai.facebook.com/blog/meta-training-inference-accelerator-AI-MTIA)

 The post Meta introduces its firstgeneration AI inference accelerator appeared first on Engineering at Meta

## [Building and deploying MySQL Raft at Meta](https://engineering.fb.com/2023/05/16/data-infrastructure/mysql-raft-meta/)

 We have migrated a large portion of our deployment to MySQL Raft and plan to fully replace the current MySQL semisynchronous databases with it

 A leader in Raft would also be the primary in MySQL and the one accepting client writes

 A follower would be a replica in MySQLs point of view and would be applying the transactions to its engine

---



# [slack engineering](https://slack.engineering/feed/)

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
