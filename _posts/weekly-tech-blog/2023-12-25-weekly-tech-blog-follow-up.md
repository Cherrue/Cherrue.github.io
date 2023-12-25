---
layout: single
title: \[기술블로그\] 12월 4주 주간 기술블로그 Follow Up
date: 2023-12-25 01:22:12 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

2023-12-18 ~ 2023-12-25 기간에 포스팅 된 주요 기술 블로그의 포스팅을 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를 참고하세요.

# [네이버 D2](https://d2.naver.com/d2.atom)

## [네이버에는 테크 월드를 꿈꾸는 사람들이 있다! - Tech Radio : 보안 편](https://d2.naver.com/news/4029141)

 저희는 네이버 시큐리티에서 일하고 있는 박영석 박현준 김태우 입니다

 MC  네이버 직원들도 할 수 있나요

 네이버 보안 팀 업무 살펴보기

## [HDFS 쓰기 파이프라인을 활용한 HBase의 WAL 쓰기 최적화](https://d2.naver.com/helloworld/6445508)

 HDFS 클라이언트는 데이터를 쓰다가 DataNode에서 오류가 발생하면 클라이언트가 파일에 데이터를 계속 쓸 수 있도록 파이프라인을 복구한다

 writeBlock DataNode 파이프라인에 블록을 쓴다

 DataNode와 기존 HDFS 쓰기 파이프라인에 파이프라인 설정 단계까지 마친  FanOutOneBlockAsyncDFSOutputHelper는 클라이언트가 데이터를 쓸 수 있도록 FanOutOneBlockAsyncDFSOutput을 생성한다

---



# [NHN Cloud Meet Up!](https://meetup.toast.com/rss)

---



# [당근마켓 팀 블로그](https://medium.com/feed/daangn)

---



# [우아한형제들 기술 블로그](https://techblog.woowahan.com/feed/)

## [[트러블슈팅기] CSR에서 동적 OG 메타태그 적용하기](https://techblog.woowahan.com/15469/)

 테스트를 하면서 필연적으로 하는 것은 로그확인 입니다

 정리를 하면 CloudFront에서 동작하는 Lambdaedge 함수의 로그를 확인하려면

 CloudFront Functions는 Lambdaedge와는 다른 로그확인 방식을 사용합니다

## [결제는 계속된다: 결제 담당자가 장애에 대응하는 방법](https://techblog.woowahan.com/15236/)

 그림 2 조건에 걸려서 발생한 결제 장애 알림

 장애가 발생한 PG사에서 결제가 진행되지 않도록 PG 배분율을 조정합니다

 특정 PG사에 장애가 발생한 경우  간편결제

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

## [Bit(Binary digit) Byte 의 고찰](https://medium.com/zigbang/bit-binary-digit-byte-%EC%9D%98-%EA%B3%A0%EC%B0%B0-ebefe5afb8d3?source=rss----2f055286701b---4)

 바이트Byte 는 일정량의 비트 모음을 정의할때 사용하며 컴퓨터의 기억장치의 크기를 나타내는 단위로 자주 쓰인다

 orgwiki비트단위 httpsko

 orgwiki바이트 httpsko

## [TypeORM QueryBuilder 활용 사례: 재사용성을 높이는 방법과 테스트 작성하기](https://medium.com/zigbang/typeorm-querybuilder-%ED%99%9C%EC%9A%A9-%EC%82%AC%EB%A1%80-%EC%9E%AC%EC%82%AC%EC%9A%A9%EC%84%B1%EC%9D%84-%EB%86%92%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95%EA%B3%BC-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0-c604f1913920?source=rss----2f055286701b---4)

 객체를 통한 조회는 테스트 코드를 작성하고 검증하기가 비교적 수월하며 쿼리 조건을 명시적으로 나열하여 가독성을 높일 수 있어 코드로서의 명료성을 지킬 수있습니다

 이때 일부 쿼리문이 코드로 들어오면서 QueryBuilder를 사용하는 코드는 가독성을 낮추고 테스트 작성이 어려워지며 코드의 재사용성이 떨어질 수있습니다

 결론QueryBuilder를 사용해야하는 케이스에서 재사용성을 높이고 테스트 코드 작성의 편의성을 높이기 위해 다양한 빌더 클래스를 도입하였습니다

## [MYSQL 인덱스 튜닝](https://medium.com/zigbang/mysql-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%ED%8A%9C%EB%8B%9D-18e183e9246d?source=rss----2f055286701b---4)

 인덱스가 있는데도 인덱스를 안타는 상황  인덱스 손익분기점인덱스를 타긴 타는데 성능이 안나오는 상황  인덱스 스캔비효율인덱스 스캔 비효율은 없지만 성능이 안나오는 상황  테이블 랜덤엑세스최소화인덱스가 너무 많이 있는 상황  중복 인덱스최적화 테스트 환경은 아래와 같이구성했습니다

 인덱스 스캔보다 테이블 풀스캔 비용이 더 낮아지는 지점을 인덱스 손익 분기점 이라고하는데요

 인덱스 스캔 자체에서 비효율이 발생하는 경우인데요

---



# [Google Developers](https://developers.googleblog.com/feeds/posts/default?alt=rss)

## [Navigating AI Safety & Compliance: A guide for CTOs](http://developers.googleblog.com/2023/12/navigating-ai-safety-and-compliance-cto-guide.html)

 AI safety principles involve identifying and mitigating potential risks and challenges early in the development cycle

 Track the performance and behavior of AI systems in real time with continuous monitoring and auditing

 As AIs role in core and critical systems grows proper governance is essential for its success and that of the systems and organizations using AI

## [Create smart chips for link previewing in Google Docs](http://developers.googleblog.com/2023/12/create-smart-chips-for-link-previewing-in-google-docs.html)

 When creating smart chips for link previewing you can choose from two different technologies to create your addon Google Apps Script or alternate runtime

 If you want to create your smart chip with Apps Script you can check out the video below in which you learn how to build a smart chip for link previewing in Google Docs from A  Z

 You can learn more about how to create smart chips using alternate runtimes from the developer documentation

## [Global developers use Google tools to build solutions in recruiting, mentorship and more](http://developers.googleblog.com/2023/12/global-developers-use-google-tools-to-build-solutions-in-recruiting-mentorship-and-more.html)

 Also I used Google Bard to translate the content of the website into English and Portuguese

 Google Developer Expert Machine Learning and Google Cloud

 Lately I was part of the team that delivered an endtoend Virtual Career Center solution that matches job candidates to job vacancies using Vertex AI Matching Engine via text embeddings and SCANN

## [#WeArePlay | Meet Steven from Indonesia. More stories from around the world](http://developers.googleblog.com/2023/12/weareplay-meet-steven-from-indonesia-more-stories-from-around-the-world.html)

 He hopes to take Super even further and improve economic distribution across the whole of rural Indonesia

 Now were landing in the Middle East where former kindergarten friends Chris and Rene decided to use their experience being expats in Dubai to create a platform for connecting disparate communities across the city

 Community is at the heart of everything we do and our goal is to have a positive effect says Chris

---



# [Amazon Science Blog](https://www.amazon.science/index.rss)

---



# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/feed)

---



# [ebay Tech Blog](https://tech.ebayinc.com/rss)

---



# [Linked in Engineering](https://engineering.linkedin.com/blog.rss.html)

## [Building Trust and Combating Abuse On Our Platform](https://engineering.linkedin.com/blog/2023/casal--building-trust-and-combating-abuse---the-anti-abuse-core-)

 In this blog post we discuss how we are harnessing AI to help us with abuse prevention and share an overview of our infrastructure and the role it plays in identifying and mitigating abusive behavior on our platform

 These algorithms consider the diversity and context of signals to make informed decisions

 Labeling holds immense significance in our quest to maintain the highest standards by helping assess the accuracy and performance of our ML models

## [Enhancing Content Review: Proactively addressing threats with AutoML](https://engineering.linkedin.com/blog/2023/enhancing-content-review--proactively-addressing-threats-with-au)

 While feature engineering used to be the province of ML engineers alone the AutoML framework is adept at looking for common patterns and automating feature engineering as much as possible

 The AutoML framework extends its automation capabilities to include the critical phase of model deployment

 To build additional trust in our content moderation defenses among our members and other stakeholders we plan to integrate different fairness assessment solutions as part of the AutoML framework

## [Practical Magic: Improving Productivity and Happiness for Software Development Teams](https://engineering.linkedin.com/blog/2023/practical-magic--improving-productivity-and-happiness-for-softwa)

  We then use this framework to describe the specific goals and signals that we selected

 We cover the key principles youll need to think about when designing any engineeringrelated metric and explain some of the common pitfalls in metric design

 We are also looking forward to community contributions that help move forward the state of the art in understanding software developers across the entire software industry

## [Deployment of Exabyte-Backed Big Data Components](https://engineering.linkedin.com/blog/2023/deployment-of-exabyte-backed-big-data-components)

 The namenode is the central component of HDFS and is responsible for storing the metadata information about files and directories in the HDFS cluster

 Ultimately version drift ensures the timely and reliable upgrade of all healthy drifted nodes helping to meet compliance requirements for live nodes in the system

 Through these measures we aimed to ensure a smoother and more reliable upgrade process of our big data system in the face of this multifaceted deployment challenge

---



# [Engineering at Meta](https://engineering.fb.com/feed/)

## [How Meta built the infrastructure for Threads](https://engineering.fb.com/2023/12/19/core-infra/how-meta-built-the-infrastructure-for-threads/)

 The seamless scale that people experienced as they signed up by the millions came on the shoulders of over a decade of infrastructure and product development

 Its built from the ground up to leverage Metas infrastructure and keyspaces hosted on it can be scaled up and down with relative ease and flexibly placed across any number of data centers

 Metas products leverage a shared infrastructure that has withstood the test of time empowering product teams to move fast and rapidly scale successful products

## [AI debugging at Meta with HawkEye](https://engineering.fb.com/2023/12/19/data-infrastructure/hawkeye-ai-debugging-meta/)

 HawkEye enables users to efficiently navigate the decision tree and quickly identify the root cause of complex issues

 HawkEye uses model explainability and feature importance algorithms to localize prediction changes to subsets of features

 HawkEye provides observability into the upstream data pipelines and their health and helps locate the root cause of bad training data

---



# [slack engineering](https://slack.engineering/feed/)

---

* 이 글은 자동으로 작성되었으며 [TextRankr](https://github.com/theeluwin/textrankr)로 요약되었습니다.
