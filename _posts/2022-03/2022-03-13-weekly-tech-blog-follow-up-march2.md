---
layout: single
title: \[기술블로그\] 3월 2주 주간 기술블로그 Follow Up
date: 2022-03-12 14:40:00 +0900
categories: engineering_blog_followup searchengine
toc: true
toc_sticky: true
toc_label: Contents
---

금주(3/5~3/11)에 포스팅 된 주요 기술 블로그의 포스팅을 요약하여 공유합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를, 지난주 포스팅은 [이 링크](https://cherrue.github.io/engineering_blog_followup/weekly-tech-blog-follow-up/)를 참고하세요.

추천 포스팅은 요약을 해두었습니다.

---

# [NHN Cloud MeetUp!](https://meetup.toast.com/)

## **[Speech to Text 서비스 소개](https://meetup.toast.com/posts/313)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.11 | 기능 소개 | - |

NHN Cloud 기능 소개 1. 음성 파일(mp3, aac, wav 등) 업로드 시 텍스트 반환 REST API

## **[Text to Speech 서비스 소개](https://meetup.toast.com/posts/314)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.11 | 기능 소개 | - |

NHN Cloud 기능 소개 2. 텍스트 입력 시 음소 단위 음성 합성으로 자연스러운 음성 제공.

성별, 높낮이, 속도, 음량 설정 가능

---

# [Google Developers](https://developers.googleblog.com/)

## ****[Celebrating global women in tech and trailblazers](https://developers.googleblog.com/2022/03/whm22.html)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.08 | 인물 소개, 인터뷰 | - |

Women’s History Month 를 맞아 여성 Google Developer Experts 인터뷰

## ****[Machine Learning Communities: Q4 ‘21 highlights and achievements](https://developers.googleblog.com/2022/03/Q4mlhighlight.html)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.08 | 프로젝트 소개 | ML |

21년 4분기의 프로젝트를 몇 가지 소개한다.

구글 자료라 TensorFlow + Google Developer Experts 관련 자료가 많다.

개인적인 추천은 순수 TensorFlow로 퍼즐 풀기를 수행한 [Advent Of Code](https://adventofcode.com/)([설명 블로그](https://pgaleone.eu/))와 주요 ML 관련 논문에 설명을 덧붙여둔 repository의 web 버전 [Annotated Research Papers](https://devlibrary.withgoogle.com/products/ml/repos/AakashKumarNain-annotated_research_papers) 를 추천한다.

---

# [Amazon Science Blog](https://www.amazon.science/blog)

## **[25 years of QIP](https://www.amazon.science/blog/25-years-of-qip)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.10 | 인터뷰 | QIP(양자컴퓨팅) |

QIP(Quantum Information Processing) 25주년 기념 `Thomas Vidick` 교수와 `Simone Severini` AWS 양자컴퓨팅 담당 이사 인터뷰. 이론에서 실전으로 넘어가는 단계라고 한다.

## **[Bringing practical applications of quantum computing closer](https://www.amazon.science/blog/bringing-practical-applications-of-quantum-computing-closer)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.11 | 기술소개 | QIP(양자컴퓨팅), 컴퓨터과학 |

양자 컴퓨팅과 큐비트, 양자 컴퓨팅으로 해결 가능한 문제와 관련 논문들을 소개한다.

---

# [Linked in Engineering](https://engineering.linkedin.com/blog)

## **[Performance-Adaptive Sampling Strategy (PASS) for GNNs: Open sourcing PASS](https://engineering.linkedin.com/blog/2022/open-sourcing-PASS)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.07 | 기술소개 | ML, GNN, Sampling |

성능 향상을 위한 GNN 샘플링 시 정확도가 떨어진다. 이를 해결하기 위해 개발한 attribute based 샘플링 기법 PASS를 소개한다. 일반 샘플링에 비해 2~3배 정확도가 높아졌다고 한다.

---

# [Engineering at Meta](https://engineering.fb.com/)

## **[Augmenting Flexible Paxos in LogDevice to improve read availability](https://engineering.fb.com/2022/03/07/core-data/augmenting-flexible-paxos-logdevice/)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.07 | 기술소개 | 고가용성, 분산 저장, Paxos |

Meta의 데이터 저장 시스템 LogDevice에 적용한 Flexible Paxos에 대한 설명이다.

서버 다운에도 대응하는 높은 write ability를 위해 어떻게 데이터를 저장하고, 어떻게 복구하는지 자세히 설명한다.

기술적인 특징인지 설명하는 단어들이 너무 추상적이라 이해하기 어려운데, 설명하려고 애쓴 흔적이 보인다.

## (추천) **[An open source compositional deadlock detector for Android Java](https://engineering.fb.com/2022/03/08/android/deadlock-detector-for-android-java/)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.08 | 기술소개 | Java, Deadlock |

meta의 CI에 실제로 적용한 모바일 java 프로그램 deadlock static analyzer, [Infer static analysis framework](https://fbinfer.com/)를 소개한다. 무려 오픈소스로 공개했다.

2년 간 CI 과정에 사용하여 200개의 reports를 생산했고, 54%를 실제로 fix 했다.

<details>

<summary>포스팅 요약 보기</summary>

<div markdown="1">

### 개요

- 목표 : 안드로이드 개발 중 소스코드 실행 없이 deadlock 발생을 탐지할 수 있는 툴 개발
- 이유 : 프로그램을 실행 및 기능 동작 때 deadlock 발생을 탐지하면 너무 오래걸린다.
- 배경지식 : deadlock

### 내용

#### 동작방식

애널라이저 설계에 abstract interpretation 적용

애널라이저가 각 메서드마다 lock의 acquisition과 release 동작 summary를 계산

이렇게 계산한 summary로 critical method pair를 찾아낸다.

찾아낸 pair를 강제로 lock하여 deadlock이 발생하는지 확인한다.

#### 필요한 이유

1. deadlock이 발생하면 회복시키기 어려운 에러이다. 
2. 실행으로 찾아내기 어렵다. 쓰레드 스케줄링이 우리가 결정할 수 없기 때문.
3. 이걸 빌드 없이 찾아낸다? 안 쓸 이유가 없죠.

### Paper 추가 요약

abstract 환경에서 deadlock을 탐지하는 방법을 설명한 [paper](https://scontent-ssn1-1.xx.fbcdn.net/v/t39.8562-6/260077364_220682913511004_3166489779435697585_n.pdf?_nc_cat=110&ccb=1-5&_nc_sid=ad8a9d&_nc_ohc=km8wDLWAKC4AX_slpXm&_nc_ht=scontent-ssn1-1.xx&oh=00_AT-sjUV7464CvVlAErCEaFCmkbMrXAOq3e8luRxVsEV24w&oe=623173C6)

#### 특징

1. 첫 실행 시에는 하루종일도 걸리지만, 이후에는 코드 변경점에만 실행해 속도를 높였다.
2. false negative 를 선호한다. 즉 모든 deadlock을 찾기 위해 실행시간이 엄청 늘어나는 것을 피했다.
3. synchronize 와 같은 키워드를 수집해서 critical pair 를 찾아내는데, NP 문제가 되어버리니까 각 포인트끼리 compatible 관계를 찾아내서 줄여나가는 식으로 동작한다고 한다.

</div>

</details>

## **[Code Verify: An open source browser extension for verifying code authenticity on the web](https://engineering.fb.com/2022/03/10/security/code-verify/)**

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.10 | 기능소개, 기술소개 | Web extension, security |

WhatsApp 웹 버전이 공개되면서 메세지 보안에 대한 문제가 대두되었다.

이를 위해 보안 해쉬와 소스코드가 안전하다고 verify 하는 Web Extension을 opensource로 공개했다.

해쉬는 Cloudfare 라는 외부 인프라를 이용해 보관한다. [meta-code-verify github](https://github.com/facebookincubator/meta-code-verify/)

---

# [slack engineering](https://slack.engineering/)

## ****[Applying Product Thinking to Slack’s Internal Compute Platform](https://slack.engineering/applying-product-thinking-to-slacks-internal-compute-platform/)****

| 게시일 | 분류 | 주요 기술 |
| --- | --- | --- |
| 22.03.10 | 프로그램 소개 | Bedrock, CI/CD, Container |

슬랙에서 차용한 Microsoft에서 만든 GitOps 기반 클라우드 CI/CD 지원 프로그램 Bedrock([github](https://github.com/microsoft/bedrock))을 소개하고, 슬랙 내에서의 반응과 활용 방안 등을 공유한다.

전반적으로 좋은데 많이들 안 써서 아쉽다는 글이다.

---

# 포스팅이 없는 블로그

[네이버 D2](https://d2.naver.com/home) : 1/29

[LINE Engineering](https://engineering.linecorp.com/ko/blog/) : 3/4

[당근마켓 팀 블로그](https://medium.com/daangn) : 2/18

[우아한형제들 기술 블로그](https://techblog.woowahan.com/) : 2/17

[kakao Tech](https://tech.kakao.com/blog/) : 2/22

[WATCHA 팀 블로그](https://medium.com/watcha) : 2/14

[무신사 기술 블로그](https://medium.com/musinsa-tech) : 21/12/17

[야놀자](https://medium.com/yanolja/archive) : 2/25

[직방 TECH](https://medium.com/zigbang) : 3/3

[THE NETFLIX TECH BLOG](https://netflixtechblog.com/) : 2/19

[ebay Tech Blog](https://tech.ebayinc.com/) : 3/1