---

layout: single
title: \[기술블로그\] SK Devocean 검색, 추천 분야 포스팅 요약
date: 2022-03-27 21:39:00 +0900
categories: engineering_blog_followup searchengine
toc: true
toc_sticky: true
toc_label: Contents

---

주간 팔로업 블로그 리스트에 SK의 데보션(DEVOCEAN)을 추가하려고 합니다.

3월 27일까지 올라온 Tech Space 포스팅 중 검색, 추천과 연관된 포스팅을 모아 요약합니다.

이번 주의 주간 기술 블로그 팔로업은 이 게시글로 대체합니다.

F/U 하는 기술 블로그 목록은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/FU-%EA%B8%B0%EC%88%A0-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%AA%A9%EB%A1%9D/)를, 지난주 포스팅은 [이 링크](https://cherrue.github.io/engineering_blog_followup/searchengine/weekly-tech-blog-follow-up-march3/)를 참고하세요.

---

# [SK DEVOCEAN Tech Space](https://devocean.sk.com/blog/sub/index.do?ID=&searchData=&page=&subIndex=Tech+Gallery&idList=)

## **[AI 챗봇 채티는 당신의 질문 의도를 알고 있다! (시맨틱 검색 플랫폼 Synapse)](https://devocean.sk.com/blog/techBoardDetail.do?ID=163686&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)**

SKT AI 상담사 채티에 적용한 Semantic Search Platform : Synapse를 설명한다.

- Semantic Search : 검색어의 문맥과 의미에서 이용자의 의도를 분석하여 연관된 문서를 추론

대화형 쿼리가 늘어나면서 기존의 키워드 검색 실패가 늘어 Synapse를 개발했다.

Synapse의 구성요소

- 모델 : BERT + Metric Learning → Bi Encoder Model + Null Query 분류 모델 → ANN
- Manager : 신규 model로 색인 생성, TC로 검증, 무중단 배포, 회귀 테스트, 스케일아웃 모두 자동화
- 모니터링 : 서버 Resource와 엔진 status 모니터링 → 알람 전송
- 서빙 API : FastAPI + Uvicorn. API 상태 확인. Faiss library + Product Quantization.

## **[AI가 내게 맞는 아이유 노래를 찾는 방법 (NUGU 개인화 검색 기술)](https://devocean.sk.com/blog/techBoardDetail.do?ID=163563&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)**

NUGU에 적용된 개인 profile 기반 개인화 검색 기술을 설명한다.

범용 검색 모델링 : Relevance = a * Similarity + b * Popularity + c * Recency

한계점

- 검색 정답이 없다. 빅뱅의 거짓말을 찾을 수도 GOD의 거짓말을 찾을 수도 있기 때문
- 디스플레이 인터페이스라면 둘 다 보여줘도 상관 없지만, 음성 인터페이스에선 1위가 제일 중요하다.

개인 Profile

- 묵시적인 상호작용 : 어떤 노래를 80% 이상 들었는가
- 명시적인 상호작용 : 플레이리스트에 추가, 좋아요, 싫어요 등
- 상호작용한 결과를 모델로 임베딩

개인화 검색 : 범용 검색을 진행한 결과를 Profile에 따라 Re-Ranking

## **[누구나 만드는 AI 음성인식 서비스 (Open NLU 기술)](https://devocean.sk.com/blog/techBoardDetail.do?ID=163467&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)**

NUGU 오픈 풀랫폼에서 제공하는 전처리 기술과 품질을 방해하는 요인, 극복하기 위한 기술을 설명한다.

이용자 발화 모델(User Utterance Model) : 이용자 발화 이해, 의도 파악 모델

- 학습 Corpus 작성 : 서비스에 적절한 예상 발화를 Intent 별로 그룹화 하고, Entity를 지정해 구조화
- Entity Built-in 사전 : 자주 사용되는 Entity 사전을 Built-in 형태로 제공
- Play Builder : 학습 말뭉치를 구축하고 발화 모델을 생성 및 테스트하는 도구 지원

학습 Corpus 확장 : 오픈 플랫폼에서 학습 데이터가 부족할 수 있는데, 이 때 동일한 의미의 발화로 확장

- 용언 치환 : 조식 → 아침, 수영장 → 헬스장
- synonym : 가르쳐줘 → 찾아줘, 추천해줘 → 들려줘
- 문장 형태 변황 : 어미 변경, 문장 구성요소 추가. 찾아줘 → 찾아주렴

학습 말뭉치를 활용한 자동 규칙 생성 : 발화 명령을 정확하게 예측하기 위한 모델에 들어갈 규칙

- 예상 발화를 토큰으로 쪼개 형태소 분석 정보 결합
- 체언과 용언에 대한 규칙 생성 : 용언에는 태그를 붙인다. 체언은 그냥 쓴다. 등

## **[내 최애곡과 닮은 노래, NUGU는 이렇게 찾는다 (유사 음악 추천 기술)](https://devocean.sk.com/blog/techBoardDetail.do?ID=163457&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)**

NUGU에서 지원하는 메타 데이터 + 이용자 로그를 통한 유사 음악 추천 기술을 설명한다.

유사 음악 추천 시스템

- 로그 → 트랙 임베딩 → 트랙 유사도 계산 → 메타 보정 → 랭킹 → 추가 필터링
- 트랙 임베딩 : 트랙 세션 정의(청취 시간 등) → 인텐트 정의 → 해당 인텐트의 소비 이력 → Skip gram
- 메타 보정 : 음악 장르 기준으로 보정. 키즈 장르 등은 메타 데이터 전처리를 해둔다.

아티스트 유사곡 추천 서비스

- 유사 아티스트 확장 : 로그 → 아티스트 임베딩 → 아티스트 유사도 → 메타보정
- 아티스트 대표곡 랭킹 : 로그 → 트랙 메타 → 아티스트 대표곡 → 유사 아티스트와 병합 → 랭킹

## **[내 취향 어떻게 알았지? NUGU의 섬세한 추천 비결 (NUGU Nudge 추천 기술 편)](https://devocean.sk.com/blog/techBoardDetail.do?ID=163401&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)**

음성 인터페이스인 NUGU의 이용자 프로파일 기반 서비스 추천기술 : Nudge

Feature engineering : Garbage In, Garbage Out. 목적에 맞게 데이터를 정제, 재가공이 제일 중요하다

이용자 프로파일의 Feature engineering

- 정규사용성 : 개인의 전체 사용주기, 각 아이템 사용주기로 계산
- 서비스 성공률 : 서비스를 실제로 경험(추천이 성공)했는지 측정하는 지표

Nudge 추천 엔진

- 이용자 액션 모델 : Matrix Factorization, CF, Sequence Pattern → score → evaluator
- 이용자 채택 모델 : Ridge Regression, Clustering → 수용도 score → evaluator
- 시간 단위 모델 : 위 두 모델은 8주간의 데이터를 활용하기 때문에 일별, 시간별 결과로 만들어야 했다.

이용자 액션 모델

- 다양한 모델을 결합하여 과적합을 방지
- 앙상블 시 Thompson Sampling 결과를 각 옵션의 가중치로 사용

이용자 채택 모델 : AI의 마지막 말 결정. ~라고 말해보세요 or 지금 확인해볼래요? 등

- 사용자 친숙도 + Demography + 성격 + 신뢰도 등 60개의 피쳐 사용

## **[‘말이야’ 해도 ‘마리아’ 찾아주는 NUGU의 검색 노하우 (검색 품질 관리 기술 편)](https://devocean.sk.com/blog/techBoardDetail.do?ID=163319&searchData=Tech+Gallery&page=&subIndex=Tech+Gallery&idList=%5B163735%2C+163686%2C+163617%2C+163600%2C+163583%2C+163579%2C+163574%2C+163563%2C+163549%2C+163542%2C+163534%2C+163520%2C+163511%2C+163507%2C+163467%2C+163457%2C+163441%2C+163418%2C+163411%2C+163405%2C+163401%2C+163384%2C+163366%2C+163355%2C+163319%2C+163310%2C+163288%2C+163280%2C+163252%2C+163248%2C+163236%2C+163226%2C+163198%2C+163195%2C+163187%2C+163182%2C+163163%2C+163127%2C+163117%2C+163118%2C+163119%5D)**

검색 품질 관리 기술 : 만족도 측정 + 사용자 패턴으로 자동 개선 + 인터페이스 상관없이 만족스러운 결과

최적의 만족도 측정 방식

- ERF : Explicit Relevance Feedback. 랜덤으로 평가 팝업 발생
- IRF : Implicit Relevance Feedback. 화면의 클릭, 음악의 중지, 재검색 등의 후속 액션

만족도를 활용 방법

- 중의적 발화 시 콜렉션 교정 시스템 (클래식 음악, 영화 클래식)
- 재검색 발생 시 검색어 대체 (말이야, 화사 마리아)
- 만족도 통계 : 동의어, 유의어, DB 오류 판단을 위한 품질 웹페이지 운영
