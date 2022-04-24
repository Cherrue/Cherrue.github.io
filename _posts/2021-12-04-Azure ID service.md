---
layout: single
title: \[강의요약\] MS Learn - Azure ID service
date: 2021-12-04 13:09:00 +0900
categories: Azure azure_fundamentals
show_in_home: false
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/secure-access-azure-identity-services/](https://docs.microsoft.com/ko-kr/learn/modules/secure-access-azure-identity-services/)

# Azure Fundamentals part 5: Describe identity, governance, privacy and compliance features

---

## Azure ID 서비스를 사용하여 애플리케이션에 안전하게 액세스

BYOD : Bring Your Own Device. 재택근무가 느니까 정해진 장비로만 접근 가능하게 인증

##### 1. 인증과 권한 부여

1-1. 인증 Authentification (AuthN) : 자격 증명으로 사용자가 본인인지 확인

1-2. 권한 부여 Authorization (AuthZ) : 사용자에게 부여되는 액세스 수준 설정

##### 2. Azure Active Directory (Azure AD)

1-1. Azure Active Directory 와 그냥 Active Directory 의 차이

그냥 AD는 온-프레미스에서, Azure AD 는 클라우드에서 동작

##### 3. Azure AD 의 사용자

- IT 관리자 : 앱 / 리소스 접근 제어
- 앱 개발자 : 앱에 SSO 기능 붙임
- 사용자 : 내 ID 관리. 비번 변경 등
- 온라인 서비스 구독자 : 365 서비스들은 이미 사용중임.

##### 4. 제공 기능

- 인증 : ID 확인. 암호 정합성 확인 등
- SSO : 한 서비스에서 인증하면 다른 서비스 접근 가능
- 애플리케이션 관리 : 프록시, SaaS, 액세스 패널, SSO 를 통해 앱 관리
- 디바이스 관리 : 계정 뿐 아니라 기기도 등록 가능하다.

대상 리소스 : Azure 리소스, Microsoft 365, Azure Portal, SaaS 등 과 클라우드에 탑재한 자체 애플리케이션에도 적용 가능

##### 5. 기존 AD 와 Azure AD 연결 방법

- Azure AD Connect

##### 6. Multifactor authN(다단계 인증)과 Conditional Access(조건부 액세스)

factor 종류

- Something the user knows : 지식 기반
- Something the user has : 소유 기반
- Something the user is : 생체 기반

6-1. 다단계 인증 제공 서비스

- Azure Active Directory : 무료버전만 써도 SMS 코드 등으로 가능. 프리미엄은 조건부 액세스도 가능
- Office 365용 다단계 인증 : Azure AD랑 같음

6-2. 조건부 액세스

> Identity signal에 따라 액세서 접근 제한

예시 : 알려진 위치에서는 일반 인증만, 모르는 위치에서는 multifactor 인증을 적용 또는 아예 접근 제한

사용하는 경우

- 애플리케이션 접근 : 특정 사용자에게만 요구도 가능.
- 승인된 클라이언트 애플리케이션으로만 접근 가능
- 관리형 디바이스를 통해서만 접근
- 예기치 못한 접근을 차단

6-3. 조건부 액세스 제공 서비스 : Azure AD Premium 또는 365 Premium

----

지식 점검

조건부 액세스 / Multi-Factor Authentication / SSO