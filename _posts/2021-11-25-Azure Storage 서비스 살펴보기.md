---
layout: single
title: \[강의요약\] MS Learn - Azure Storage 서비스 살펴보기
date: 2021-11-25 22:17:00 +0900
categories: Azure azure_fundamentals
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

https://docs.microsoft.com/ko-kr/learn/modules/azure-storage-fundamentals/

# Azure Fundamentals part 2: Describe core Azure services

---

## Azure Storage 서비스 살펴보기

### 1. Azure Storage 종류

1-1. Disk Storage : 가상머신에 디스크 제공.

- 표준 SSD / HDD : 중요도 낮은 워크로드 
- 프리미엄 SSD  : 중요 업무용 워크로드
- Ultra Disks : 데이터 집약적 워크로드, 최상위 계층 DB, 트랜잭션 집약적 워크로드

1-2. Azure Blob Storage : 클라우드용 개체 스토리지. 엄청 큰 Blob 같은 거 저장. 데이터 종류 제한 없음

- 스트리밍, 분산 저장, 백업/보관용 데이터, 분석용 데이터 등 비정형이고 형태가 중요하지 않은 큰 데이터

1-3. Azure Files : SMB(Server Message Block) 및 Network File System을 통해 접근 가능한 관리형 파일 공유

- 여러 온 프레미스 앱에 파일 공유 : 변경이 적어야 함
- 여기저기서 쓰이는 configure files 저장
- 나중에 공유 / 분석 등을 위한 파일 저장. logs, metrics, crash dumps 등

SMB로 통신할 때 암호화 함

SAS (Shared Access Signature)만 있으면 어디서나 접근 가능 (https://파일 URI?sv=SAS)

### 2. Blob access tier

많고 큰 데이터를 아무렇게나 저장하면 비효율적임.

frequency of access / retention period 를 이용해 저장 계층을 지정

- hot : 자주 액세스

- cool : 액세스가 적고 30일 이상 저장

- archive : 액세스 없고 180일 이상 저장

  > 계정 수준에서 접근 불가. 데이터 액세스 비용이 비쌈

속도는 hot이 가장 빨라야 하고, 내구성은 archive가 가장 좋아야 한다.

---

지식 점검

Azure Storage 계정 만들기 / Azure Blob Storage