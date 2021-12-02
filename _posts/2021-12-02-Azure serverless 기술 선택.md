---
layout: single
title: \[강의요약\] MS Learn - Azure serverless 기술 선택
date: 2021-12-02 23:18:00 +0900
categories: Azure azure_fundamentals
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/serverless-fundamentals/](https://docs.microsoft.com/ko-kr/learn/modules/serverless-fundamentals/)

# Azure Fundamentals part 3: Describe core solutions and management tools on Azure

---

## 비즈니스 시나리오에 적절한 Azure Serverless Technology 선택

##### 1. Azure Serverless Computing

> 개체 편집기에서 구성 요소를 연결해서 원하는 작업을 http 요청 등의 방법을 통해 실행

사용자가 서버를 설정하거나 유지 관리할 필요가 없고, 서버 중단 걱정 필요도 없음. 스케일링도 노신경

1-1. Azure Functions

> http 요청 / 타이머 / 메시지 등을 통해 단일 메서드 호스트

특징 : 원자적 특성. stateless. 프로그래밍 언어 사용. 필요하면 Durable Functions로 state 유지

필요한 경우 : 플랫폼이나 인프라 상관없이 서비스 실행하는 코드만 관심이 있는 경우

사용 가능 언어 : C#, Python, JavaScript, Typescript, Java, PowerShell

1-2. Azure Logic Apps

> 코드가 없는 개발 플랫폼. 조직에서 앱 / 데이터 / 시스템 / 서비스를 통합할 때 오케스트레이션을 위해 사용. 

필요한 경우 : 오케스트레이션이 목적인 경우. 코드를 보기 싫은 경우

----

지식검사

Azure Functions / Azure Logic Apps / Azure Logic Apps