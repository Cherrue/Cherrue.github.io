---
layout: single
title: \[강의요약\] MS Learn - Azure Database 및 분석 서비스 살펴보기
date: 2021-11-26 00:24:00 +0900
categories: Azure azure_fundamentals
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

https://docs.microsoft.com/ko-kr/learn/modules/azure-storage-fundamentals/

# Azure Fundamentals part 2: Describe core Azure services

---

## Azure Database 및 분석 서비스 살펴보기

### 1. Azure Database

1-1. Azure Cosmos DB

전 세계에 배포된 multi-model database service. 여러 Azure region에서 자유롭게 스케일링 가능. "Always On"함.

내부적으로 데이터를 저장할 때 ARS(atom-record-sequence)를 사용.

사용자가 DB를 만들 때 ARS로 저장한 데이터를 추상화하여 각 API로 서비스하여 DB의 형태 변경 등 이관작업에 굉장히 용이

1-2. Azure SQL Database

RDB PaaS. PaaS라서  DB 업그레이드, 패치, 백업, 모니터링에 OS도 다 업데이트 해줌. 99.99%의 가용성 제공

- 처리 데이터 형태 : json, 그래프, spatial, xml 다 지원
- 고급 : high-performance / in-memory 기술, intelligent query processing 등 advanced query도 지원
- Azure Database Migration Service : 최소한의 downtime으로 마이그레이션 가능
- Microsoft Data Migration Assitant : 마이그레이션 전 필요한 변경 사항 보고서를 만들어 줌

### 2. 실습 : SQL Database 만들기

2-1. 데이터베이스 만들기 (리소스 만들기 > 데이터베이스 > SQL Database 만들기)

![task1](/assets/images/2021-11-26/task1.png)

![task2](/assets/images/2021-11-26/task2.png)

![task3](/assets/images/2021-11-26/task3.png)

2-2. 정보 입력 : 컨시어지구독 / learn-**** / db01 / 서버 새로 만들기

실습에서는 이거저거 더 설정하게 하는데, 안 해도 괜찮다. 서버는 반드시 새로 만들기를 누르자

**해보고 싶다면 파란 버튼 대신 하얀 버튼(다음-네트워킹) 누를 것**

![task4](/assets/images/2021-11-26/task4.png)

서버 이름은 전체에서 고유해야 함. 적당히 숫자 붙여주자

![task5](/assets/images/2021-11-26/task5.png)

5분정도 소요

![task6](/assets/images/2021-11-26/task6.png)

2-3. 방화벽 설정 (외부 접근 허용, 클라이언트 IP 추가)

![task7](/assets/images/2021-11-26/task7.png)

![task8](/assets/images/2021-11-26/task8.png)

![task13](/assets/images/2021-11-26/task13.png)

2-4. 쿼리 편집기 접근 (모든 리소스 > db1(위에서 만든 SQL Database) > 쿼리편집기 > 로그인 > )

![task9](/assets/images/2021-11-26/task9.png)

![task10](/assets/images/2021-11-26/task10.png)

![task14](/assets/images/2021-11-26/task14.png)

### 3. Azure Database

3-1.  for MySQL

- 제공 버전 : 5.6 / 5.7 / 8.0
- 제공 기능 : 고가용성, 스케일링, 데이터 보호, 자동 백업 등

3-2. for PostgreSQL

고가용성, 스케일업/다운, 자동 백업 및 복원(최대 35일), 암호화 등 기능 제공

deployment 옵션

- Single Server : 고가용성, 스케일링, 모니터링, 백업, 복원 등 그냥 일반적인 거
- Hyperscale(Citus) : sharding을 이용해서 수평 스케일링. 빅데이터 병렬처리에 쓰는 거임. multi-tenent, 실시간 분석 등

### 4. Azure SQL Managed Instance

PaaS, SLA, 99.99% 고가용성. 자동 백업. 복원. 다 똑같음

차이점 : Azure SQL Database는 latin 인코딩만 사용 가능해서 못 씀

이관방법 : Azure DMS(Database Migration Service)나 일반 백업/복원을 이용해 이관 가능

### 5. 빅데이터와 분석 서비스

5-1. Azure Synapse Analystics : 데이터 웨어하우징 + 빅데이터 분석. 원하는 대로 쿼리 가능. 수집/준비/관리/제공 통합 환경

5-2. Azure HDInsight : fully managed 오픈소스 분석 서비스. Spark, Hadoop, Kafka, HBase, Storm 등 제공.

5-3. Azure Databricks : 데이터에서 인사이트를 얻고 AI 솔루션 빌드 가능. Spark 환경 구성 후 python, scala, R 등 언어와 TensorFlow, PyTorch, scikit-learn 등 프레임워크와 라이브러리 지원

5-4. Azure Data Lake Analytics : 빅데이터를 단순화하는 on-demand analytics job service. feature 추출

---

지식 점검

Azure Cosmos DB / Azure Database for MySQL / Azure Synapse Analytics