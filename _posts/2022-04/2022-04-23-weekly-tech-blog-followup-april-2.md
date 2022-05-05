---

layout: single
title: \[기술블로그\] 4월 2주 주간 기술블로그 Follow Up
date: 2022-04-16 18:55:00 +0900
categories: engineering_blog_followup searchengine
toc: true
toc_sticky: true
toc_label: Contents

---

4/9 ~ 4/15 기간에 포스팅 된 주요 기술 블로그의 포스팅을 요약하여 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를, 지난주 포스팅은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/weekly-tech-blog-sk-search-posts/)를 참고하세요.


---

# [NHN Cloud MeetUp!](https://meetup.toast.com/)

## [리액트 커스텀 훅을 테스트하는 과정](https://meetup.toast.com/posts/321)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 라이브러리 사용법 | React, testing |

React 16.8에 추가된 컴포넌트 상태 로직 추상화 기능인 리액트 훅의 작성 방법과 testing-library/reacthooks를 이용한 테스트 방법

## [Go 제네릭](https://meetup.toast.com/posts/320)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 언어 사용법 | Go, Generic |

Go 1.18에 추가된 제네릭의 문법과 사용법을 예제 코드 중심으로 소개

자바와 다르게 대괄호를 사용하고, any 또는 타입 제한자를 걸어주어야 한다. 그외 constraints, ~ 문법 등을 소개한다.

## [사용자 입력 텍스트를 바이트(byte) 길이로 제한하는 Vue 컴포넌트 만들기](https://meetup.toast.com/posts/319)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.14 | 기능 구현, 입력값 검증 | javascript, vue, encoding |

Vue에서 글자 수 제한 기능을 개발하기 위해 한글 인코딩을 설명하고, 함수를 구현해 콜백을 붙이는 과정

기능 자체는 반복문으로 검사해서 잘라내는 간단한 구조이다.

---

# [LINE Engineering](https://engineering.linecorp.com/ko/blog/)

## (추천) [계정(account) 기반 블록체인에서의 개인 정보 보호](https://engineering.linecorp.com/ko/blog/how-do-we-secure-transaction-data-in-account-base-blockchain/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 암호화 기술 소개 | 블록체인, ZKP, UTXO |

2021 개발자 데이에서 발표한 내용을 글로 옮긴 것. 블록체인 환경에서 보안 거래를 구현하기 위한 기술을 소개

잔액을 관리 방법과 각종 암호화 기술을 소개하고, 실제로 적용한 account-UTXO 하이브리드 모델과 ZKP을 알기 쉽게 설명했다.

## [Turborepo로 모노레포 개발 경험 향상하기](https://engineering.linecorp.com/ko/blog/monorepo-with-turborepo/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 시스템 소개 | 모노레포, turborepo, CI/CD |

모노레포의 필요성과 모노레포 빌드 시스템인 Turborepo의 장점을 소개한다.

모노레포는 하나의 repository에 여러 프로젝트를 관리하는 것으로, 의존성 관리나 배포 작업을 쉽게 처리할 수 있어 사용합니다

turborepo는 이전 빌드 결과를 캐시해 전체 빌드를 회피하고 빌드 파이프라인을 한 곳에 모을 수 있고 병렬처리로 성능도 높일 수 있다고 합니다. 

## [Kotlin JDSL: Kotlin을 이용해 좀 더 쉽게 JPA Criteria API를 작성해 봅시다](https://engineering.linecorp.com/ko/blog/kotlinjdsl-jpa-criteria-api-with-kotlin/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 개발한 라이브러리 소개 | Kotlin, JPA, Criteria |

Kotlin의 CriteriaBuilder를 대체하기 위해 개발한 오픈소스 JDSL을 소개한다.

CriteriaBuilder에 비해 상당히 깔끔하게 복잡한 쿼리를 짤 수 있어보인다.

---

# [당근마켓 팀 블로그](https://medium.com/daangn)

## [당근마켓 디자인 챕터의 첫 컨퍼런스 참가 이야기](https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93-%EB%94%94%EC%9E%90%EC%9D%B8-%EC%B1%95%ED%84%B0%EC%9D%98-%EC%B2%AB-%EC%BB%A8%ED%8D%BC%EB%9F%B0%EC%8A%A4-%EC%B0%B8%EA%B0%80-%EC%9D%B4%EC%95%BC%EA%B8%B0-2e5dcd6fad0d)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.14 | 컨퍼런스 참여 후기 | - |

당근마켓 디자인 챕터의 컨퍼런스 참가 후기. 현재 프로덕트 디자이너 직무 채용이 진행중이다.

---

# [우아한형제들 기술 블로그](https://techblog.woowahan.com/)

## (추천) [회원시스템 이벤트기반 아키텍처 구축하기](https://techblog.woowahan.com/7835/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.12 | 아키텍처 설계 과정 | MSA, event 기반 아키텍처 |

MSA 적용 시 시스템 간 결합도를 제거하는 방법과 안전한 이벤트 발행 및 처리를 위한 이벤트 저장소 구축 방법 소개

내용은 상당히 좋은 글인데, 전문 용어가 많고 문장 호흡이 길어 읽기가 꽤 어렵다. 이벤트 기반 처리를 이해하기 좋은 글

## [Yarn berry workspace를 활용한 프론트엔드 모노레포 구축기](https://techblog.woowahan.com/7976/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.13 | 환경 설정 | 모노레포, yarn berry, typescript |

여러 백오피스 FE가 제멋대로 흩어져서 개발되어 비효율적으로 관리되는 것을 모노레포로 합쳐 설정하는 과정

설정 관리, 중복 코드  제거 등의 장점과 프로젝트 열 때의 불편함 등의 단점을 모두 소개해 흥미로운 글이다.

## [[모집] 2022우아한테크캠프 5기](https://techblog.woowahan.com/8154/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 교육 프로그램 소개 | - |

JS 기반 웹 풀스택(React + Node js + AWS + MySQL), Kotlin 모바일 안드로이드 과정

8주 간 300만원 정도, 배민 신입 채용 시 전용 전형 운영

---

# [kakao Tech](https://tech.kakao.com/blog/)

## [제네시스 – 광고추천팀의 카프카 기반 스트리밍 데이터 플랫폼](https://tech.kakao.com/2022/04/13/kafka-connect-streaming-data-platform/)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.13 | 플랫폼 이관 | Kafka, logstash |

기존에 Kafka + logstash로 운영하던 ETL 프로세스를 Kafka connector + Kafka로 이관한 사례

web admin의 개발이 필요하고 보안 설정된 데이터 플랫폼의 설정이 좀 복잡할 수 있다

작업에 jira id 를 붙여 오너십을 부여하고, 모니터링과 배포 편의성을 확보할 수 있다.

---

# [무신사 기술 블로그](https://medium.com/musinsa-tech)

## [Apache Airflow와 Amazon EKS가 만났을 때 벌어지는 일](https://medium.com/musinsa-tech/sre-9fe5113de898)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.11 | 환경 설정 | Airflow, AWS, k8s |

AWS의 EKS 위에 Airflow를 Helm Chart를 이용해 설치하는 스크립트를 공유

GPU와 AWS Neuron 추가 설정도 있는데, 실제 스크립트를 공유해서 좋다.

---

# [야놀자](https://medium.com/yanolja/archive)

## [[야놀자R&D] 개발자에서 PMO로, PMO팀 도영석님](https://medium.com/yanolja/%EC%95%BC%EB%86%80%EC%9E%90r-d-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%97%90%EC%84%9C-pmo%EB%A1%9C-pmo%ED%8C%80-%EB%8F%84%EC%98%81%EC%84%9D%EB%8B%98-8dbc462214e7)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.14 | 인터뷰 | - |

대기업 11년차 개발자에서 스타트업 PMO로 헤드 헌팅 후 소감 인터뷰

## [[야놀자R&D] 인턴십부터 정규직 채용까지, Discovery팀 강영우님](https://medium.com/yanolja/%EC%95%BC%EB%86%80%EC%9E%90r-d-%EC%9D%B8%ED%84%B4%EC%8B%AD%EB%B6%80%ED%84%B0-%EC%A0%95%EA%B7%9C%EC%A7%81-%EC%B1%84%EC%9A%A9%EA%B9%8C%EC%A7%80-discovery%ED%8C%80-%EA%B0%95%EC%98%81%EC%9A%B0%EB%8B%98-5fc4d6aaf6ec)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.13 | 인터뷰 | - |

인턴 후 정규직 전환 후 소감 인터뷰

---

# [SK DEVOCEAN](https://devocean.sk.com/blog/sub/index.do?ID=&searchData=&page=&subIndex=Tech+Gallery&idList=#none)

## [사람 대신 보고 이해하다](https://devocean.sk.com/blog/techBoardDetail.do?ID=163827&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163827%2C+163757%2C+163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.11 | 기술 소개 | AI, 객체 인식 |

SKT에서 개발중인 AI Camera 기술 소개.

속성 인지, 자세 예측, 행동 인식. 다중 카메라 분석 4가지 방향으로 개발중이다.

---

# [Google Developers](https://developers.googleblog.com/)

## [How is Dev Library useful to the open-source community?](https://developers.googleblog.com/2022/04/dev-library-open-source.html)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.11 | 플랫폼 소개 | - |

구글에서 21년 6월부터 서비스한 Google Dev Library이라는 오픈소스 플랫폼 소개

## ****[Announcing the Apps Script connector for AppSheet: Automate workflows for Google Workspace](https://developers.googleblog.com/2022/04/apps-script-connector-for-appsheet.html)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.13 | 프로덕트 소개 | - |

Azure의 service와 같은 함수 + workflow로 동작하는 AppSheet과 Apps Script connector 튜토리얼

AppSheet은 코드 없이 쓰는 것인데, Apps Script에서 간단한 코딩 후 AppSheet에서 쓸 수 있게 하는 기능

## [Getting started is the hardest part: Find inspiration with Apps Script samples](https://developers.googleblog.com/2022/04/getting-started-is-hardest-part-find.html)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.14 | 프로덕트 소개 | - |

AppSheet의 활용방법 소개

google 스프레드 시트 custom 함수 개발, google form으로 drive의 폴더 생성 자동화 등 구글 생태계 연결 또는 자동화 가능

## [Machine Learning Communities: Q1 ‘22 highlights and achievements](https://developers.googleblog.com/2022/04/MLCommunities2022Q1.html)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.15 | 기술 근황 | ML |

분기마다 올라오는 ML 커뮤니티 근황이다.

개인적으로는 인도에서 개발한 braille to audio(점자 to 오디오) 번역 모델과, 터키에서 keras.io에 추가한 40개의 학습 모델에 관심이 간다.

---

# [Amazon Science Blog](https://www.amazon.science/blog)

## [New method for "editing" fabricated chips enables more-efficient designs](https://www.amazon.science/blog/new-method-for-editing-fabricated-chips-enables-more-efficient-designs)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.12 | 하드웨어 기술 소개 | FIB-CE |

완성된 칩에 효율성 증가를 위해 이것저것 추가하는 기법을 FIB-CE라 하는데, 이 때 칩의 손상을 최소화 하는 방법

---

# [THE NETFLIX TECH BLOG](https://netflixtechblog.com/)

## [How Netflix Content Engineering makes a federated graph searchable](https://netflixtechblog.com/how-netflix-content-engineering-makes-a-federated-graph-searchable-5c0c1c7d7eaf)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.13 | 개발 과정 소개 | GraphQL, ES, Kafka, Avro |

GraphQL 에서 검색을 위해 ES를 도입하고, 데이터를 색인하고, 자동으로 스케일아웃 하는 간단한 예시 소개

---

# [Linked in Engineering](https://engineering.linkedin.com/blog)

## [Load-balanced Brooklin Mirror Maker: Replicating large-scale Kafka clusters at LinkedIn](https://engineering.linkedin.com/blog/2022/load-balanced-brooklin-mirror-maker--replicating-large-scale-kaf)

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.04.11 | 아키텍쳐 설계 | Kafka, HA, replication |

대규모 시스템에서 mirroring으로 HA를 달성하면서 마주하는 문제들을 해결하기 위한 아키텍처 설계

Cruise Control, Apache Pinot, Apache Samza 등을 통해 수집한 mertric 정보로 남은 리소스를 유연하게 분배하는 LB Brooklin의 동작 방식을 소개한다.

## [Open sourcing Feathr – LinkedIn’s feature store for productive machine learning](https://engineering.linkedin.com/blog/2022/open-sourcing-feathr---linkedin-s-feature-store-for-productive-m)

## [Client Zero Protocol: Taking intelligent risks to go beyond the traditional SDLC control framework](https://engineering.linkedin.com/blog/2022/client-zero-protocol--taking-intelligent-risks-to-go-beyond-the-)

---

# 포스팅이 없는 블로그

[네이버 D2](https://d2.naver.com/home) : 3/24

[WATCHA 팀 블로그](https://medium.com/watcha) : 4/7

[직방 TECH](https://medium.com/zigbang) : 3/31

[ebay Tech Blog](https://tech.ebayinc.com/) : 4/5

[Engineering at Meta](https://engineering.fb.com/) : 3/30

[slack engineering](https://slack.engineering/) : 4/6