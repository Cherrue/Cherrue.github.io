---
layout: single
title: Azure 기본사항 파트 1 핵심 Azure 개념
date: 2021-11-07 19:31:00 +0900
categories: Azure azure_fundamentals
---

# Azure 기본사항

---

## Azure 기본사항 소개

링크 : https://docs.microsoft.com/ko-kr/learn/modules/intro-to-azure-fundamentals/introduction

1. ### 클라우딩 컴퓨팅

> 클라우드 컴퓨팅이란 데이터 센터의 컴퓨터를 필요한 시간만큼 대여하는 것

##### 1-1. 장점

- 스펙을 필요할 때 바꿀 수 있음
- 규모의 경제도 있고 필요한 만큼만 쓰니까 저렴

##### 1-2. 필요성

- 하나의 디바이스로 여러 가지를 하고자하는 사용자의 니즈를 해결하려면 시스템 전환이 잦음
- 클라우드에서 제공해주는 기능을 활용하면 더 빠른 개발이 가능

2. ### Azure

> Azure는 비즈니스 과제를 해결하도록 돕는 클라우드 서비스

##### 2-1. 제공 기능

잔 뜩 제 공 : VM, DB, Storage, hosting, popular framework, container, AI/ML 등등

##### 2-2. 작동방식

USER > Orchestrator - fabric controller > server > Rack > hypervisor [가상화] > virtual machine

Orchestrator는 Web API로 사용자 요청을 받아 적절한 서버에서 적절한 기능이 동작하도록 도와준다.

##### 2-3. Azure Portal

> Azure를 컨트롤할 수 있는 웹앱

##### 2-4. Azure Marketplace

> VM Image 등의 애플리케이션과 서비스를 판매

3. ### Azure 둘러보기

	1. compute
	1. network : VPN, Load Balancer, Gateway, DNS 등 
	1. storage : 내구성, 보안, 확장성
	1. mobile : 푸쉬 알림 등
	1. database
	1. web : build / deploy / manage / scale
	1. IoT : 데이터 분석, 모니터링
	1. Big data : 오픈소스 클러스터 등
	1. AI : 자연어 처리, vision, speech 등
	1. DevOps : create, build pipeline to deploy application

