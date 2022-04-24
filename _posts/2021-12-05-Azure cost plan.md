---
layout: single
title: \[강의요약\] MS Learn - Azure cost plan
date: 2021-12-05 03:13:00 +0900
categories: Azure azure_fundamentals
show_in_home: false
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/plan-manage-azure-costs/](https://docs.microsoft.com/ko-kr/learn/modules/plan-manage-azure-costs/)

# Azure Fundamentals part 6: Describe Azure cost management and service level agreements

---

## Azure 비용 계획 및 병합하기

##### 1. TCO(Total Cost of Ownership). 총 소유 계산기

> 온 프레미스 대신에 클라우드를 쓸 때 절감되는 비용 예측 계산기. 기본적인 비용만 계산함(라이센스 이런거)

사용 방법 : 워크로드 정의 > 가정 조정 > 보고서 보기

1-1. 워크로드 정의

- 서버 : OS, 가상화 방법, CPU 코어+메모리
- DB : 동시 사용자 수, DB 유형, 하드웨어, Azure 서비스
- 스토리지 : 보관 / 백업 스토리지를 포함해 스토리지 유형 / 용량
- 네트워킹 : 네트워크 대역폭의 양

1-2. Adjust Assumptions. 가정 조정

Software Assurance가 있다면 Azure에서 해당 라이센스를 재활용

운영비용 산정 : 전기 요금. IT 관리 요금. 네트워크 유지 관리 비용 등을 포함

1-3. 보고서 보기 : 1~5년 기간을 설정해 보고서를 볼 수 있다.

##### 2. [연습] TCO 계산기 써보기

https://azure.microsoft.com/ko-kr/pricing/tco/calculator/

AWS보다 쉬운거 같기도?

##### 3. Azure 서비스 구입

3-1. 구독 유형

- 평가판 : 12개월 무료 서비스. 30일 크레딧. 만료 시 서비스 비활성화
- 종량제 : 사용한 만큼 지불
- 멤버 프로모션 : 기존 MS 제품을 쓴다면 할인 요금

3-2. 구입 방법

- 기업 계약 : MS와 기업 계약. 3년 간 정액 결제. 가격을 좀 맞춰주는 듯
- 웹에서 구입 : Azure Portal에서 표준 가격 지불
- CSP(클라우드 솔루션 공급자)를 통해 구입 : MS의 파트너 회사가 있음. CSP에서 정한 금액으로 청구

3-3. 비용 영향 요인

- 리소스 유형 : 리소스에 따라 비용 다름
- 사용량 미터 : 사용량을 추적하는 meter를 만듬. 사용량(시간, 트래픽, 디스크IO 등) 레코드로 청구
- 리소스 사용량 : 중간중간 끄면 절감 가능
- 구독 유형 : 비용 다름
- Azure Marketplace : 타사 서비스를 구입하여 사용하면 돈 늘어남
- region : 인프라 까는 비용이 달라서
- billing zone(청구 영역) : 데이터 센터로 들어오거나 나간 데이터의 양

3-4. Azure Pricing calculator

지역 / 계층 / 청구 옵션 / 지원 옵션 / 프로그램 및 제품 / 개발,테스트 가격 책정 을 넣으면 계산해줌

##### 4. [연습] Azure Pricing calculator 써보기 (걍 안 함)

##### 5. 비용 최소화 하기

먼저 가격계산기와 TCO 계산기로 예상 비용 계산

5-1. Azure Advisor 사용하기 : 사용량 저조 리소스를 식별해서 알려줌

5-2. 지출 한도 지정 : 할당량을 넘어가면 구독 일시 중단. 위험

5-3. Azure Reservations : 선납해서 할인 받기

5-4. 저렴한 Region 선택

5-5. 프로모션 확인하기 ^ㅗ^;;

5-6. Azure Cost Management + 청구 : 권장사항을 제공해줌

5-7. 태그 적용 : 재무 부서 같은 데서 봐주기

5-8. 안 쓰는 가상머신 줄이기

5-9. 업무 외 시간엔 머신 할당 취소 : 스토리지는 남으니까 VM만 할당 취소

5-10. 미사용 리소스 삭제하기

5-11. IaaS -> PaaS로 마이그레이션 : 라이센스 비용을 말하는 듯

5-12. 저렴한 운영체제 사용 : 운영체제에 따라서도 비용이 바뀜

5-13. Software Assurance : 이게 있으면 애져로 라이센스 용도 변경이 가능

----

지식점검

총 소유 비용 계산기 실행 / 개발 팀의 Azure 구독에 지출 한도를 적용합니다. / 사용 중이 아닌 가상 머신을 할당 취소합니다. / 각 가상 머신에 해당 청구 부서를 식별하는 태그를 적용합니다.