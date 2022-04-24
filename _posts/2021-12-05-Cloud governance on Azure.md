---
layout: single
title: \[강의요약\] MS Learn - Cloud governance on Azure
date: 2021-12-05 02:03:00 +0900
categories: Azure azure_fundamentals
show_in_home: false
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/build-cloud-governance-strategy-azure/](https://docs.microsoft.com/ko-kr/learn/modules/build-cloud-governance-strategy-azure/)

# Azure Fundamentals part 5: Describe identity, governance, privacy and compliance features

---

## Azure에서 클라우드 거버넌스 전략 빌드

##### 1. RBAC(Role-Based Access Control)

- 적용 범위 : 관리 그룹 / 단일 구독 / 리소스 그룹 / 단일 리소스 (부모의 권한은 자식에게 상속됨)
- 적용 타이밍 : Azure Resource Manager로 리소스를 시작할 때 적용됨. 포탈/CLI 등으로 접근 가능. allow 모델(whitelist)
- 적용 대상 : 개별 사용자 또는 사용자 그룹
- 관리 방법 : Azure Portal의 Access Control(IAM) 패널에서 설정.

##### 2. 리소스 잠금

> 리소스의 변경 및 삭제 금지

- 적용 방법 : 포탈/CLI 등에서 Azure Resource Manage 템플릿으로 관리 가능
- 확인 방법 : Azure Portal > 리소스 설정 > 설정
- 적용 수준 : CanNotDelete / ReadOnly
- 변경 방법 : 잠금을 제거하고 변경
- Azure Blueprints : 리소스 잠금마저 실수로 지우면 알아서 다시 걸 수 있음

##### 3. [연습] 리소스 잠 : 구독이 필요해서 안 했음!

리소스 그룹 > 설정 > 잠금에서 추가

만든 리소스 그룹에 원하는 리소스를 추가

##### 4. 리소스를 태그로 관리하기

제공 메타데이터

- 리소스 관리 태그 : 연결된 리소스 찾아서 작업 가능
- 비용관리 및 최적화 태그 : 관련 리소스 비용을 그룹화하여 보고 / 예산 추적 / 예상 비용 산정
- 작업관리 태그 : SLA(Service Level Agreement) 작성에 도움
- 보안 태그 : 보안 수준에 따라 분류
- 거버넌스 및 규정준수 태그 : 특정 규정 준수가 필요한 리소스들 식별
- 워크로드 최적화 및 자동화 태그 : 복잡한 작업에 엮인 모든 리소스를 시각화

4-1. 적용 방법 : 포탈, CLI 등 + Azure Policy 도 가능

----

##### 5. Azure Policy

> 리소스를 제어하거나 감사하는 정책을 생성 / 할당 / 관리 서비스

- 정의 방법 : initiative(이니셔티브)로 정의. 태그로 정책 준수 리소스 확인 가능
- 동작 방식 : 정의 생성 -> 정의 할당 -> 평가 결과 검토

5-1. 정책 정의(Policy Definition) 만들기

- 허용된 가상 머신 정의
- 허용된 지리적 위치 정의
- 쓰기 권한이 있는 계정에 MFA(MultiFactor Authentication) 적용
- 필요한 도메인만 웹앱에 접근하도록 CORS 적용
- 머신에 시스템 업데이트 설치 강요

5-2. 리소스에 정의 할당 : 범위 지정

5-3. 평가 결과 검토 : 리소스 정책 준수 / 미준수 상태 표기. 시간 당 한 번 수행

5-4. Azure Policy Initiative : 관련 정책을 하나의 세트로 그룹화하는 방법

- 정의 방법 : 명령줄 도구 또는 Portal. wㅓㅇ책 > 정의 > 이니셔티브 정의
- 할당 방법 : 위랑 같음

###### 6. [연습] Azure Policy (구독 필요해성 안 함)

6-1. 리소스그룹 만들기 : 리소스 만들기 > 리소스 그룹 만들기

6-2. 정책 구성 :  정책 > 작성 > 정의 

6-3. 정책 정의 + 할당 : 정책 > 작성 > 할당 > 정책 할당 > 범위 - 리소스 그룹 할당 > 상세 정책 정의 > 매개변수 > 만들기

6-4. 정책 할당 삭제 : 정책 > 작성 > 할당 > 할당 삭제

6-5. 리소스 그룹 삭제 : 리소스 그룹 > 리소스 그룹 삭제

##### 7. Azure Blueprints로 여러 구독 관리

> 클라우드 환경이 하나의 구독을 초과해버리면 어떡하지? 이 때 적용할 템플릿 같은 것
>
> 거버넌스 도구, 표준, 리소스 세트 등읠 정의

7-1. 오케스트레이션 대상 : 역할 할당 / 정책 할당 / Azure Resource Manager 템플릿 / 리소스 그룹

7-2. 작동 방식 : blueprints 만들기 > 할당 > 추적

7-3. blueprints artifacts : blueprints의 각 구성요소

----

##### 8. Cloude Adoption Framework (클라우드 채택 프레임워크)

구성요소 : Tools, documents, proven practices

8-1. 전략정의 : 클라우드로 전향하려는 이유와 이점 식별

- 동기 정의 : 클라우드 적용 동기를 경영진에 물어봐
- 비즈니스 결과 문서화 : 비즈니스 목표를 재무 / 영업에 물어봐
- 재무 고려 사항 평가 : 목표를 측정하고 기대 수익 산출
- 기술적 고려 사항 이해 : 하나 해보고 기술 고려 사항을 평가

8-2. 계획 수립

- 디지털 자산 : 기존 디지털 자산 목록과 워크로드 인벤토리 식별
- 초기 조직 정렬(Initial organizational alignment) : 적합한 Azure 사용자가 작업에 참여하는가
- 기술 준비 계획 : 클라우드 운영 기술 study 계획
- 클라우드 채택 계획 : 개발 / 운영 / 비즈니스 팀 함께 포괄 계획 수립

8-3. 조직 준비

- 설정 가이드
- Landing zone(랜딩 존) : 구독 빌드 시작. 거버넌스 / 회계 / 보안 / 인프라 모두 포함
- 랜딩 존 확장 : 거버넌스 / 운영 / 보안 요구사항 충족 여부 확인
- 모범 사례 : 문제 없음을 증명하는 사례로 만듬

8-4. 클라우드 채택

- 첫번째 워크로드 마이그레이션 : Azure 마이그레이션 가이드 활용
- 마이그레이션 시나리오 : 복잡한 마이그레이션 시나리오 확인
- 모범 사례 : 잘 되는 케이스 확인
- 프로세스 개선 : 더 적은 작업으로 최적화

혁신!

- 비즈니스 가치 합의 : 고객 요구사항 충족 확인
- Azure 혁신 가이드 : 개발 가속화 + Minimum Viable Product(MVP) 빌드
- 모범 사례 : 잘 되는지 확인
- 피드백 루프 : 고객과 체크인 해서 잘 되고 있는지 확인

8-5. 클라우드 환경 제어 및 관리

제어

- 방법론 : 최종 상태 솔루션을 고려해 증분 방식으로 적용
- 벤치마크 : 거버넌스 벤치마크 도구 사용
- Initial governance foundation(초기 거버넌스 기반) : MVP(Minimal Viable Product)를 만들어서 측정
- Improve 거버넌스 foundation : risk를 관리할 수 있는 거버넌스 지속 추가

관리

- 관리 기준 설정 : 자산에 적용할 최소한의 도구와 프로세스 정의
- 비즈니스 약속 정의 : 워크로드 문서화. 클라우드 관리 투자 동의
- 관리 기준 확장 : 관리 기준 중에 모범 사례 적용
- 고급 운영 및 디자인 원칙 : 복잡한 워크로드는 더 자세한 아키텍쳐 검토를 수행

##### 9. 구독 거버넌스 전략 만들때 고려 사항

- 결제 : 부서 / 프로젝트 별 구독 구성
- Access Control : 별도 구독을 만들어 액세스 개별적으로 관리하고 리소스간 격리 가능
- 구독 제한 : 구독 별 제한이 있는 리소스가 있음(Azure ExpressRoute는 10개까지만) 이걸 고려

----

지식 점검

Azure RBAC(역할 기반 액세스 제어)를 통해 역할 할당을 만듭니다. / Azure Policy에서 허용되는 SKU 크기를 지정하는 정책을 만듭니다. / 연결된 청구 부서를 포함하는 각 리소스에 태그를 적용합니다.