---
layout: single
title: \[강의요약\] MS Learn - managing and configuring tool 선택
date: 2021-12-03 00:19:00 +0900
categories: Azure azure_fundamentals
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/management-fundamentals/](https://docs.microsoft.com/ko-kr/learn/modules/management-fundamentals/)

# Azure Fundamentals part 3: Describe core solutions and management tools on Azure

---

## Azure 환경 관리 및 구성에 가장 적합한 도구 선택

##### 1. 도구의 종류

1-1. 시각적 도구

> 편하지만, 종속성이 있거나 구성이 복잡한 리소스 배포에 부적합

1-2. 코드 기반 도구

> 복잡한 리소스를 빠르게 구성하려면 코드

IaC : Infrastructure as Code. 설정 / 구성용 소스 코드를 작성해 형상관리하는 방법

- imperactive(명령적) 코드 : 각각 어떠한 outcome을 받기 위해 실행하는 코드
- declarative(선언적) 코드 : 원하는 outcome이 하나이고 이를 달성하기 위한 최적의 인터프리터를 결정

##### 2. Azure의 Product

2-1. Azure Portal

> 웹 기반 UI. Azure 모든 기능 사용 가능. 하지만 노가다 필요

사용하는 경우 : 일회성. Azure를 처음 사용 하는 사람. UI가 필요한 사람. 비전문가

2-2. Azure Mobile App

> 컴퓨터를 못 쓸 때 모바일로 리소스 액세스. 모니터링 / 재시작 / CLI 명령 실행

사용하는 경우 : 컴퓨터 없을 때. 출근하기 싫을 때

2-3. Azure PowerShell

> cmdlet(command-let) 명령어를 호출. 모든 Azure 리소스 관리 기능 호출 가능. 자동화 가능

오케스트레이션 가능 : 리소스 루틴 설정. 많은 리소스를 포함하는 인프라 전체 배포

사용하는 경우 : 일회성/다회성. 빠른 작업. PowerShell 전문가라면

2-4. Azure CLI

> Bash 명령어 실행. Azure Rest API 호출. PowerShell이랑 똑같음.

사용하는 경우 : 일회성/다회성. 빠른 작업. CLI 전문가라면

2-5. ARM 템플릿

> 리소스 구성 json 사용. 리소스 생성을 병렬로 오케스트레이션 함.

사용하는 경우 : 다회성. Azure CLI도 호출 가능함. 유효성 검사가 가능함

----

지식검사

Azure CLI / Azure Portal / ARM 템플릿