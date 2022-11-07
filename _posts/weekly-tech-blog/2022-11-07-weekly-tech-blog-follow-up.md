---
layout: single
title: \[기술블로그\] 10월 6주 주간 기술블로그 Follow Up
date: 2022-11-07 02:11:14 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2022-10-31 ~ 2022-11-07 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

## [MySQL CATS (Contention-Aware Transaction Scheduling)](https://medium.com/daangn/mysql-cats-contention-aware-transaction-scheduling-71fe6956e87e?source=rss----4505f82a2dbd---4)

 예전 MySQL 메뉴얼의 데드락예시이 예제에서 TRXA가 먼저 SharedLock을 획득한 상태에서 TRXB가 레코드 삭제 쿼리를 실행하면서 동일 레코드에 대해서 ExclusiveLock을 요청하면서 TRXB는 대기 큐에서 기다려요

 즉 MySQL 8029 버전부터는 TRXA는 가중치trxscheduleweight 값이 1이 부여되고 TRXB는 가중치 값이 0NULL이 부여되기 때문에 TRXA가 늦게 잠금을 요청했음에도 불구하고 TRXB 보다 먼저 ExclusiveLock을 허가Grant받게 되면서 데드락 상황을 회피할 수 있게되었어요

 하지만 MySQL 서버의 CATS 스케쥴러가 이미 각 트랜잭션에 할당된 잠금을 회수하는 것은 아니기 때문에 이런 경우 데드락을 회피할 수없는거죠

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

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

## [Consistent caching mechanism in Titus Gateway](https://netflixtechblog.com/consistent-caching-mechanism-in-titus-gateway-6cb89b9ce296?source=rss----2615bd06b42e---4)

 To fulfill the existing API contract we had to guarantee that for a request received at a time T₀ the data returned to the client is read from a cache that contains all state updates in Titus Job Coordinator up to timeT₀

 Titus Gateway makes a request to the local cache to fetch the latest version of thedata

 The local cache in Titus Gateway records the local logical time and sends it to Titus Job Coordinator in a keepalive message keepaliveₐ

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

## [How LinkedIn Ditched the "One Size Fits All" Hiring Approach for InfoSec and Won](https://engineering.linkedin.com/blog/2022/how-linkedin-ditched-the--one-size-fits-all--hiring-approach-for)

 As a result of this skillsfirst hiring approach the number of new members joining our InfoSec team increased by 182 in 2022 as compared to 2021

 REACH has been an excellent source of talent for the InfoSec team at LinkedIn and InfoSec has doubled down on the program

 Another component of meeting talent where they are is finding opportunities to create new opportunities and internal mobility for team members to improve retention and keep your team engaged

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [Reducing Instagram’s basic video compute time by 94 percent](https://engineering.fb.com/2022/11/04/video-engineering/instagram-video-processing-encoding-reduction/)

 Our advanced encodings covered only 15 percent of total watch time and we projected that spending all our compute on minimum functionality versions would soon prevent us from being able to provide advanced video encoding watch time

 The diagram below shows the higher watch time we expected for advanced encodings after freeing up compute from our basic ABR

 From this test we proved that although we were degrading the compression efficiency of the basic ABR encodings in the test pool the higher watch time for advanced encodings more than made up for it

## [Improving Instagram notification management with machine learning and causal inference](https://engineering.fb.com/2022/10/31/ml-applications/instagram-notification-management-machine-learning/)

 Today we would like to share an example of how we used causal inference and ML to control sending for daily digest push notifications

 The solution we adopted to tackle this problem is the combination of causal inference and ML

 By applying this model and targeting the users  notifications with high incremental impact we reduced the sending volume substantially compared to using the CTR model and also saw no decline in user engagement

---



# [slack engineering](https://slack.engineering/feed/)

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
