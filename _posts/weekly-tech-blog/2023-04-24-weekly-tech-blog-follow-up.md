---
layout: single
title: \[기술블로그\] 4월 4주 주간 기술블로그 Follow Up
date: 2023-04-24 01:39:07 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-04-17 ~ 2023-04-24 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

## [Tuist 를 활용해 확장 가능한 모듈 구조 만들기](https://medium.com/daangn/tuist-%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%B4-%EB%AA%A8%EB%93%88-%EA%B5%AC%EC%A1%B0-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-f200992d4bf2?source=rss----4505f82a2dbd---4)

 디렉토리 구조를 통해 모듈 명세를 Swift 코드로 생성할 수 있는 스크립트를 작성합니다

 프로젝트 구성에 생성된 코드활용하기이제 생성된 모듈 명세 코드를 활용해 Project

 rawValue  Feature moduleName moduleName

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [2023 우아한테크캠프, ‘Java 백엔드 교육’으로 새롭게 돌아옵니다.](https://techblog.woowahan.com/11411/)

 2023년 여름 우아한테크캠프는 넥스트스텝과 함께 백엔드 개발 교육으로 진행합니다

 기존에는 프론트엔드 개발 교육으로 진행되었던 우아한테크캠프가

 올해에는 Java 언어를 기반으로 한 백엔드 개발 교육으로 전환되었습니다

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

## [Multi-stage Docker Build와 BuildKit](https://medium.com/zigbang/multi-stage-docker-build%EC%99%80-buildkit-a55fa60aaee7?source=rss----2f055286701b---4)

 FROM alpinelatest  RUN apk nocache add cacertificatesWORKDIR rootCOPY from0 gosrcgithub

 FROM alpinelatest  RUN apk nocache add cacertificatesWORKDIR rootCOPY frombuilder gosrcgithub

 BuildKit을 이용해 빌드를 하면 사용되지 않는 stage는 스킵되며 병렬적으로 처리가 됩니다

## [개발자도 Figma를 통해 기획자, 디자이너와 소통하는 시대?](https://medium.com/zigbang/%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%8F%84-figma%EB%A5%BC-%ED%86%B5%ED%95%B4-%EA%B8%B0%ED%9A%8D%EC%9E%90-%EB%94%94%EC%9E%90%EC%9D%B4%EB%84%88%EC%99%80-%EC%86%8C%ED%86%B5%ED%95%98%EB%8A%94-%EC%8B%9C%EB%8C%80-a1f8b96fb88d?source=rss----2f055286701b---4)

 Figma에는 comment 기능을 통해 팀원들과 커뮤니케이션할 수 있습니다

 Figma comment기능Version History프로젝트를 진행하다 보면 기획 내용이나 디자인이 바뀌게 마련입니다

 지금까지 개발자 입장에서 제가 느꼈던 Figma에 장점을 간략히 이야기해 보았습니다

## [AWS SQS와 Lambda 동시성의 밀당 (Set Visibility Timeout)](https://medium.com/zigbang/aws-sqs%EC%99%80-lambda-%EB%8F%99%EC%8B%9C%EC%84%B1%EC%9D%98-%EB%B0%80%EB%8B%B9-set-visibility-timeout-2e8f630b0159?source=rss----2f055286701b---4)

 이 메시지 큐의 트리거에 푸시를 발송하는 Lambda가 붙어서 처리하는 구조입니다

 Lambda가 끌어 가면서 이 메시지 그룹은 단일성을 보장받기 위해 메시지 큐에서 숨김처리됩니다

 그럼 Lambda 입장에서는 역으로 SQS가 메시지 그룹을 처리하는 걸 기다렸다가 끝나면 다음 그룹을 넘겨줬으면 할텐데 그러지 않습니다

## [AWS RDS Storage 성능 비교](https://medium.com/zigbang/aws-rds-storage-%EC%84%B1%EB%8A%A5-%EB%B9%84%EA%B5%90-3d1150b97b2e?source=rss----2f055286701b---4)

 테스트는 Storage 테스트라서 DB서버의 영향도를 기록하기엔 좋은 사양의 서버가 필요없다고 판단했습니다

 lua runselect  index update delete  insert 테스트용sourcesysbench  dbdrivermysql  mysqlhostendpoint  maxrequests100000  time120  mysqlusersysbenchuser  mysqlpassword12345  mysqldbsysbench  tablesize1000000  tables10  deleteinserts100  indexupdates100  nonindexupdates100  threads85  reportinterval10 usrsharesysbencholtpreadwrite

 lua run테스트용 source 데이터삭제sysbench  dbdrivermysql  mysqlhostendpoint   mysqlusersysbenchuser  mysqlpassword12345  mysqldbsysbench  tablesize1000000  tables10 usrsharesysbencholtpreadonly

---



# [Google Developers](https://developers.googleblog.com/feeds/posts/default?alt=rss)

---



# [Amazon Science Blog](https://www.amazon.science/index.rss)

---



# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/feed)

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

## [Viral spam content detection at LinkedIn](https://engineering.linkedin.com/blog/2023/viral-spam-content-detection-at-linkedin)

 To understand how viral spam content flows through member networks and is detected before it goes viral it is necessary to stay updated with the latest forms of spam content being uploaded on the platform and modify our models accordingly

 Reactive defenses serve as an additional layer of protection to the proactive defenses and act on the content after it has gathered engagement signals pointing to virality

 Through the implementation of both proactive and reactive models we have successfully decreased the overall percentage of views on spam content by 73

## [Scaling Salt for Remote Execution to support LinkedIn Infra growth](https://engineering.linkedin.com/blog/2023/scaling-salt-for-remote-execution-to-support-linkedin-infra-grow)

 A basic master and minion flow in Salt is shown in Figure 1 Minion an agent on host sees jobs and results by subscribing to events published on the event bus by master service

 Targeted minions execute the job on the host and return to master

 lisaltmaster Deployable Master  API service which orchestrates minions and exposes new Salt rest APIs endpoints for clients

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [A fine-grained network traffic analysis with Millisampler](https://engineering.fb.com/2023/04/17/networking-traffic/millisampler-network-traffic-analysis/)

 Userspace therefore configures two parameters in Millisampler the sampling interval  and the number of samples

 Using the sketch results in an approximation of the connection count that is precise up to a dozen connections and saturates at around 500 connections per sampling interval

 In a following post we will look at an extension of Millisampler  Syncmillisampler  where we run Millisampler synchronously across all hosts in a rack and use that data to identify buffer contention in the topofrack ASICs

---



# [slack engineering](https://slack.engineering/feed/)

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
