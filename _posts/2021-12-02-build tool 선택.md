---
layout: single
title: \[강의요약\] MS Learn - build tool 선택
date: 2021-12-02 23:18:00 +0900
categories: Azure azure_fundamentals

---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/azure-devops-devtest-labs/](https://docs.microsoft.com/ko-kr/learn/modules/azure-devops-devtest-labs/)

# Azure Fundamentals part 3: Describe core solutions and management tools on Azure

---

## 조직의 솔루션 빌드를 위한 최적의 tool 선택

##### 1. Azure DevOps products

1-1. Azure DevOps Services

> 소프트웨어 개발 수명 주기 관리 서비스 모음

제공 서비스

- Azure Repos : 코드 repository
- Azure Boards : 이슈 관리를 위한 Kanban 보드 등을 제공하는 프로젝트 관리 제품군
- Azure Pipelines : CI/CD 파이프라인 자동화 도구
- Azure Artifacts : 테스트 / 파이프라인으로 넘길 컴파일 소스코드 등의 artifact를 호스트하는 repository
- Azure Test Plans : 품질 보증을 위한 CI/CD 파이프라인에서 사용 가능한 자동화 테스트 도구

필요한 경우 : 복잡한 권한 지정. 정교한 칸반 보드

1-2. Github / Github Actions

제공 기능 : code repo, kanban board, discuss, CI/CD pipelines, wiki

필요한 경우 : 오픈소스 빌드. 간단한 권한 지정, 간단한 칸반 보드

1-3. Azure DevTest Labs

> 소프트웨어 빌드가 포함된 VM 설정 / 삭제 프로세스 자동화 도구. VM 말고 다른 프로비저닝도 가능

필요한 경우 : 여러 테스트 환경을 구성하는 경우

----

지식검사

Azure Boards / Azure DevTest Labs / Azure Pipelines

Azure 테스트 랩이라는게 있네??? DevTest랑 구분할 것