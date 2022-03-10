---
layout: single
title: \[기술블로그\] 3월 1주 주간 기술블로그 Follow Up
date: 2022-03-07 11:30:00 +0900
categories: engineering_blog_followup
toc: true
toc_sticky: true
toc_label: Contents
---

금주(2/26~3/4)에 포스팅 된 주요 기술 블로그의 포스팅을 요약하여 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를, 지난주 포스팅은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/weekly-tech-blog-follow-up/)를 참고하세요.

추천 포스팅은 번역 및 요약을 해두었습니다.

---

# [LINE Engineering](https://engineering.linecorp.com/ko/blog/)

## **[오래된 프로덕트 디자인 리뉴얼하기](https://engineering.linecorp.com/ko/blog/)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.04 | 프로젝트 기획 | UX, 소프트웨어 공학 |

LINE에서 인수한 일본 배달 어플 Demaecan의 3단계의 리뉴얼 계획

---

# [직방 TECH](https://medium.com/zigbang)

## ****[Node.js와 Express환경에서 IP 화이트리스트, IP 블랙리스트 적용하기](https://medium.com/zigbang/node-js%EC%99%80-express%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-ip-%ED%99%94%EC%9D%B4%ED%8A%B8%EB%A6%AC%EC%8A%A4%ED%8A%B8-ip-%EB%B8%94%EB%9E%99%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0-32d810e6e4a7)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.02.28 | 기능 구현, Back-End | Express, JavaScript, HTTP |

Express와 express-ip-filter-middleware를 사용하여 IP를 차단/허용하는 코드 공유

## ****[디더 투명도 셰이더를 만들어보자](https://medium.com/zigbang/%EB%94%94%EB%8D%94-%ED%88%AC%EB%AA%85%EB%8F%84-%EC%85%B0%EC%9D%B4%EB%8D%94%EB%A5%BC-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EC%9E%90-98756735487e)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.03 | 기능 구현, 성능 개선 | Unity, Dither, Texture |

Dither Transparency와 알파 블렌딩을 소개하고, Unity의 Dither Functions 라이브러리를 사용해 구현

---

# [Google Developers](https://developers.googleblog.com/)

## ****[Students in LATAM come together for continent-wide tech conference](https://developers.googleblog.com/2022/02/students-in-latin-america-come-together.html)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.02.28 | 행사 소개 | - |

2021년 11월에 진행한 라틴 아메리카 학생 개발자 컨퍼런스 참가자의 소감 모음

## ****[Discontinuing authorization support for the Google Sign-In JavaScript Platform Library](https://developers.googleblog.com/2022/03/gis-jsweb-authz-migration.html)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.01 | 라이브러리 만료 안내 | OAuth, OpenAPI |

2023년 3월 31일 deprecate 예정인 구글 인증 라이브러리의 deprecate 영향 범위와 마이그레이션 방법 안내

---

# [Amazon Science Blog](https://www.amazon.science/blog)

## **[Improving question-answering models that use data from tables](https://www.amazon.science/blog/improving-question-answering-models-that-use-data-from-tables)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.02.28 | 알고리즘 소개, 벤치마크, 성능 개선 | Question-Answering Model, NLP |

테이블 기반의 질문-답변 모델의 fine tune 이전에 합성 데이터로 pre-train 하여 성능을 개선한 사례

## **[How Prime Video uses machine learning to ensure video quality](https://www.amazon.science/blog/how-prime-video-uses-machine-learning-to-ensure-video-quality)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.04 | 알고리즘 소개, 기능 소개 | Residual-NN, No-reference model, LipSync |

Amazon Prime Video의 퀄리티 검수 인공지능 18개 중 세 가지 소개

- Block corruption : Residual neural network를 이용해 탐지
- Audio artifact detection : no reference model을 통해 5개로 분류
- Audio/Video sync detection : 옥스포드 대학의 SyncNet 기반의 LibSync를 사용해 판별

---

# [ebay Tech Blog](https://tech.ebayinc.com/)

## (추천) **[Building a Deep Learning Based Retrieval System for Personalized Recommendations](https://tech.ebayinc.com/engineering/building-a-deep-learning-based-retrieval-system-for-personalized-recommendations/)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.01 | 기능 소개, 근실시간 서비스 | Hadoop, ML |

개인화 추천 서비스를 근실시간으로 서비스하기 위해 적용한 ML 라이브러리와 인프라

<details>

<summary>포스팅 요약 보기</summary>

<div markdown="1">

### 개요

- 목표 : 최근 본 아이템 목록에 유사한 아이템을 추천하는 근실시간 개인화 추천 서비스 개발
- 이유 : 기존의 추천 방식은 새로운 input이 반영되기 까지 시간이 소요됨
- 배경지식 : hadoop ecosystem, KNN, ANN

### 내용

#### ANN

approximate nearest neighbor 어떤 metric space 안에서 point P에서 가장 가까운 point q를 찾는 nearest neighbor 알고리즘에서, 메모리와 시간 효율을 위해 전체 점을 계산하는 것이 아니라 일부만 계산해서 반환. 실시간으로 활용이 가능하다.

#### Phase 1. 오프라인

기존의 추천 방식. 미리 추천 모델을 만들고, 이를 api로 호출

**작업 방식**

1. (Spark) 일일 ETL job 수행으로 사용자 기록 데이터와 Item 메타 데이터 aggregate
2. (PyTorch) trained 모델 파일을 사용해 사용자와 item 임베딩
3. (FAISS) 사용자 임베딩을 입력하여 KNN 검색을 수행해 Couchbase DB에 저장
4. 사용자가 검색하면 Couchbase를 조회하여 반환

#### Phase 2. 오프라인 / 근실시간 하이브리드

ANN이 등장하며 KNN을 실시간으로 수행할 수 있다. KNN을 실시간으로 빼내자

**작업 방식**

1. (Spark) 일일 ETL job 수행. phase 1과 동일
2. (PyTorch) 사용자와 Item 임베딩
3. (Couchbase) 사용자 임베딩 저장
4. (KNN service index) item 임베딩을 real-time KNN 서비스 index에 저장
5. 사용자가 검색하면 Couchbase에서 사용자 임베딩 정보를 조회해서 KNN을 실시간 수행하여 반환

#### Phase 3. NRT

이제 데이터 적재와 임베딩을 근실시간으로 수행하도록 고치자.

데이터 적재는 Kafka로 스트리밍해서, 임베딩은 비 python 환경의 자체 제작 예측 모델로 이관하여 해결한다.

(이 자체 제작 모델을 이렇게 넘어가면 포스팅의 의미가 있나..?)

**작업 방식**

1. (Kafka) 사용자 클릭 이벤트를 스트리밍한다.
2. (Apache Flink) 사용자 이벤트를 캡처하여 자체 제작한 예측 모델로 사용자 임베딩 생성
3. (Couchbase) 사용자 임베딩 저장
4. (KNN service index) Phase 2 방식으로 item 임베딩을 만들어 real-time KNN 서비스 Index에 저장
5. 사용자가 검색하면 근 실시간 user 임베딩 정보를 조회하여 KNN 수행하여 반환

</div>

</details>

---

# [Linked in Engineering](https://engineering.linkedin.com/blog)

## **[Why am I seeing this ad?](https://engineering.linkedin.com/blog/2022/why-am-i-seeing-this-ad-)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.02.28 | 기능 소개 | json, join |

링크드인의 기능 Why am I seeing this ad? 기능의 동작 방법. 데이터 조회, 표준화, 조인(매핑), 번역 등

## **[Near real-time features for near real-time personalization](https://engineering.linkedin.com/blog/2022/near-real-time-features-for-near-real-time-personalization)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.01 | 기능 소개, 실시간 서비스 | Hadoop. ML |

개인화 추천 서비스를 근실시간으로 서비스하기 위해 구현. Apache Samza 도입, 데이터 저장 방식 등

---

# 포스팅이 없는 블로그

[네이버 D2](https://d2.naver.com/home) : 1/29

[NHN Cloud MeetUp!](https://meetup.toast.com/) : 2/21

[당근마켓 팀 블로그](https://medium.com/daangn) : 2/18

[우아한형제들 기술 블로그](https://techblog.woowahan.com/) : 2/17

[kakao Tech](https://tech.kakao.com/blog/) : 2/22

[WATCHA 팀 블로그](https://medium.com/watcha) : 2/13

[무신사 기술 블로그](https://medium.com/musinsa-tech) : 21/12/16

[야놀자](https://medium.com/yanolja/archive) : 22/1/27

[THE NETFLIX TECH BLOG](https://netflixtechblog.com/) : 2/18

[Engineering at Meta](https://engineering.fb.com/) : 1/18

[slack engineering](https://slack.engineering/) : 2/18