---

layout: single
title: \[기술블로그\] 4월 3주 주간 기술블로그 Follow Up
date: 2022-04-24 20:10:00 +0900
categories: engineering_blog_followup searchengine
toc: true
toc_sticky: true
toc_label: Contents

---

4/16 ~ 4/22 기간에 포스팅 된 주요 기술 블로그의 포스팅을 요약하여 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를, 지난주 포스팅은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/weekly-tech-blog-followup-april-2/)를 참고하세요.

추천 포스팅은 요약을 해두었습니다.

---

# [네이버 D2](https://d2.naver.com/home)

## (추천) [모던 프론트엔드 프로젝트 구성 기법 - 모노레포 개념 편](https://d2.naver.com/helloworld/0923884)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.18 | 프로젝트 관리 | 모노레포 |

요즘 모노레포가 대세인가? 관련 글이 많다.

멀티레포(↔모노레포)의 단점, 모노레포에 대한 오해 해소, 모노레포 적용 시 고려사항 소개

정리하면 여러 프로젝트의 배포과정, devOps, 모듈이 유사할 때 사용하면 좋다.

다른 글에 비해 상당히 읽기 쉽게 잘 쓰였다.

## [모던 프론트엔드 프로젝트 구성 기법 - 모노레포 도구 편](https://d2.naver.com/helloworld/7553804)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.18 | 프로젝트 관리 | 모노레포, yarn, lerna, nx, turborepo |

모노레포를 위한 도구 4가지 : yarn, lerna, nx, turborepo

지금까지 읽은 포스팅을 보면 yarn과 turborepo가 대세인 듯 하다.

---

# [NHN Cloud MeetUp!](https://meetup.toast.com/)

## [Android 변조앱 만들기(feat. sandhook)](https://meetup.toast.com/posts/322)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.20 | 모의해킹 | 안드로이드 앱 변조, sandhook |

Android 변조앱 만드는 방법을 소스코드 수준에서 설명한 글. 상당히 재밌다.

## [서비스 개발하다 오픈소스 기여한 썰 (1)](https://meetup.toast.com/posts/323)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.20 | 오픈소스 기여 | js, html to pdf, html2canvas |

html to pdf를 개발하기 위해 html2canvas를 사용하다가 기여한 이야기인데, 이 편에서는 문제 소개로 끝난다.

---

# [LINE Engineering](https://engineering.linecorp.com/ko/blog/)

## [Kotlin JDSL: Kotlin을 이용해 손쉽게 Reactive Criteria API를 작성해 봅시다](https://engineering.linecorp.com/ko/blog/kotlinjdsl-reactive-criteria-api-with-kotlin/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.22 | 자체 개발 오픈소스 소개 | kotlin, jpa, reactive jpa |

지난 주의 JDSL의 reactive한 버전이다. 반응형 방식의 JPA를 처음 접한다면 hibernate reactive의 대안이 될 수 있을 것 같다.

---

# [당근마켓 팀 블로그](https://medium.com/daangn)

## (추천) [Memory Allocator for MongoDB](https://medium.com/daangn/memory-allocator-for-mongodb-1953f9cee06c)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.17 | 설정값 튜닝 | mongoDB, TCMalloc, JEMalloc |

mongos 운영 시 memory allocator 선택 가이드. 대용량 쓰레드 테스트 결과와 빌드 스크립트도 공유한다.

| 구분 | TCMalloc | JEMalloc |
| --- | --- | --- |
| 매모리 안정성 | 나쁨 | 좋음 |
| 대용량 메모리 캐싱 | 캐싱 | timeout 제한 |

정리하면 **대용량 쿼리**가 매우 빈번하게 실행되거나, mongos를 위해서 **충분한 메모리**를 가지고 있다면 TCMalloc, 그 외의 경우 JEMalloc을 사용하자.

---

# [우아한형제들 기술 블로그](https://techblog.woowahan.com/)

## [[접수중] 4월 우아한테크세미나｜지속가능한 SW개발을 위한 코드리뷰](https://techblog.woowahan.com/8159/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.19 | 세미나 소개 | 코드리뷰, PR |

SK Planet, 11번가 자문위원 백명석 님의 코드리뷰 세미나. ~26일 신청, 27일 19시 강의

---

# [WATCHA 팀 블로그](https://medium.com/watcha)

## [코드 다이어트, Android Compose!](https://medium.com/watcha/%EC%BD%94%EB%93%9C-%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8-android-compose-313b82cd784a)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.20 | 문법 소개 | kotlin, android, compose |

Android UI 개발 시 보일러 플레이트 코드를 다이어트하기 위해 적용할 수 있는 @Composable 애노테이션 소개

- 보일러 플레이트 코드 : 똑같은 텍스트를 플레이트에 박아 찍는 것처럼, 반복해서 똑같이 찍어내는 코드

---

# [Google Developers](https://developers.googleblog.com/)

## [Exploring accessibility through community with Pescara’s Google Developer Group](https://developers.googleblog.com/2022/04/exploring-accessibility-community.html)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.21 | 커뮤니티 소개 | - |

시각 장애 개발자의 경험을 공유해 개발 도구의 접근성 문제와 관련 커뮤니티를 소개

---

# [Amazon Science Blog](https://www.amazon.science/blog)

## [How does Astro localize itself in an ever-changing home?](https://www.amazon.science/blog/how-does-astro-localize-itself-in-an-ever-changing-home)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.19 | 기술 소개 | robotics, computer vision |

## [Amazon releases 51-language dataset for language understanding](https://www.amazon.science/blog/amazon-releases-51-language-dataset-for-language-understanding)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.20 | 라이브러리 소개, 대회 소개 | NLP |

이번에 아마존에서 발표한 MASSIVE라는 51가지 언어로 작성된 100만 개의 labeld utterances(발화, 여기서는 문장)와 MASSIVE를 이용한 MMNLU 경연 대회 소개

## [TheWebConf: Stable themes, new wrinkles](https://www.amazon.science/blog/thewebconf-blurring-the-line-between-industry-and-academic-research)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.21 | 컨퍼런스 소개 |  |

---

# [Linked in Engineering](https://engineering.linkedin.com/blog)

## (추천) [Addressing the last mile problem with MySQL high availability](https://engineering.linkedin.com/blog/2022/addressing-the-last-mile-problem-with-mysql-high-availability)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.22 | 문제 해결 | RDBMS,  |

링크드인은 RDB의 HA(고가용성)를 위해 Openark Ochestrator 도입하며 만난 4 가지 문제와 해결과정 소개

- The problem with huge transactions : 하나의 거대한 쿼리가 DB를 멈출 수 있음<br/>
→ each tx_rows_modified를 모니터링해서 Orchestrator 적절한 threshold를 건다.
- Measuring the absolute replication lag : 기존의 SBM으로 레플리카의 상태의 정확한 확인이 어려움<br/>
→ heartbeat 카운터 도입. 일정 시간마다 카운터를 올리고, 쿼리 시 값을 비교
- How to do candidate selection : candidate에서 primary로 승격할 때의 규칙<br/>
→ Orchestrator의 후보 뽑기 API를 사용. 단, Must 설정이 아닌 Prefer로 설정. 읽기 중인 레플리카가 쓰기까지 감당하면 걔도 죽을 가능성이 있기 때문
- The thundering problem : 여러 트래픽이 단숨에 몰려 한꺼번에 다 죽어버리는 현상<br/>
→ pre-failover hook을 걸어 일정 이상의 트래픽이 모이면 DeadMaster event를  발생시켜 실제 failover 발생 전에 수 초간 대비한다.

---

# 포스팅이 없는 블로그

[kakao Tech](https://tech.kakao.com/blog/) : 4/14

[무신사 기술 블로그](https://medium.com/musinsa-tech) : 4/10

[야놀자](https://medium.com/yanolja/archive) : 4/14

[직방 TECH](https://medium.com/zigbang) : 3/31

[SK DEVOCEAN](https://devocean.sk.com/blog/sub/index.do?ID=&searchData=&page=&subIndex=Tech+Gallery&idList=#none) : 4/14

[THE NETFLIX TECH BLOG](https://netflixtechblog.com/) : 4/12

[ebay Tech Blog](https://tech.ebayinc.com/) : 4/5

[Engineering at Meta](https://engineering.fb.com/) : 3/30

[slack engineering](https://slack.engineering/) : 4/6