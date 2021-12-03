---
layout: single
title: \[강의요약\] MS Learn - monitoring service 선택
date: 2021-12-03 00:40:00 +0900
categories: Azure azure_fundamentals

---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

서비스에 대한 설명 위주로 요약합니다.

[https://docs.microsoft.com/ko-kr/learn/modules/monitoring-fundamentals/](https://docs.microsoft.com/ko-kr/learn/modules/monitoring-fundamentals/)

# Azure Fundamentals part 3: Describe core solutions and management tools on Azure

---

## visibility, insight, outage mitigation을 위한 monitoring service 선택

##### 1. Azure Monitoring Services

> 클라우드 사용 최적화 인사이트와 경고. 문제의 근본 원인 규명. 가동 중단 대비

1-1. Azure Advisor

> 리소스 평가, 안정성, 보안/성능 개선, 운영 우수성 달성, 비용 절감 권장 사항 제공을 통해 클라우드 최적화 시간 절약

권장사항 분류 : Reliability / Security / Performance / Cost / Operational Excellence

필요한 경우 : 배포된 리소스의 분석이 필요한 경우. 비용 절감. 최적화 등

1-2. Azure Monitor

> Azure/on-premise의 메트릭과 로깅 데이터를 기반으로 수집 / 분석 / 시각화 / Potentially taking action 수행

기능 : 시각화 뿐 아니라 경고 알림을 주거나, auto scaling을 할 수 있음

필요한 경우 : 특정 VM의 성능 / 문제 추적. 메트릭 정보가 필요한 경우. 중단에 대한 경고 설정

1-3. Azure Service Health

> Azure 전체 서비스 / 지역을 특별히 모니터링. personalized view 제공. 문제가 있을 때 경고도 주고, 중단이 발생하면 RCAs(Root Cause Analyses) 보고서 제공

이벤트 유형

- Service issues : 발생한 이슈가 어느 서비스 / Region / engineering team에 영향을 미치는지 확인 가능
- Planned maintenance : availability. 이벤트가 어떤 서비스/region에 어떻게 영향을 미칠 지, 어떤 작업이 필요한지 설정
- Health advisories : 서비스 중단을 피하기 위해 필요한 작업 알려줌

필요한 경우 : 내 App이 아니라 전체 Azure에서 사용하는 서비스 및 지역을 특별히 모니터링 하려고 할 때. 

----

지식점검

Azure Advisor / Azure Service Health / Azure Monitor