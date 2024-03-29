---

layout: single
title: \[기술도서\] 가상 면접 사례로 배우는 대규모 시스템 설계 기초
date: 2022-03-22 23:56:00 +0900
categories: engineering_boog high_availability
toc: true
toc_sticky: true
toc_label: Contents

---

# [기술도서] 가상 면접 사례로 배우는 대규모 시스템 설계 기초

Property: March 22, 2022 11:52 PM

시작일 : 2022-03-21

제목 : 가상 면접 사례로 배우는 대규모 시스템 설계 기초 (인사이트, 2021)

저자 : 알렉스 쉬

가격 : 21600원

경로 : 팀원 추천

# 1장 사용자 수에 따른 규모 확장성

## 1. 용어

- 스케일 업 : 수직 규모 확장. 장비 스펙 강화
- 스케일 아웃 : 수평 규모 확장. 장비 대수 증가
- SPOF : Single Point Of Failure. 특정 지점의 장애가 전체 서비스의 장애가 되는 포인트

## 2. 확장

가정 : 웹, 모바일 단말 대응 서버 어플리케이션

### 2-1. 단일서버 : 테스트, 소규모

모든 컴포넌트(웹, 앱, 데이터베이스, 캐시) 모두 서버 한 대에 구성

### 2-2. 데이터베이스 : 지속적인 사용자 발생

웹 계층과 데이터 계층 분리

RDB와 NoSQL 사용. 상황에 따라 다르지만 보통 혼합해서 쓴다.

NoSQL 고려사항

- low latency
- 비정형 데이터
- 파일이 아닌 API 서버
- 데이터의 양이 많은 경우

### 2-3. 웹 서버 규모 확장

스케일 업은 failover 대응이 불가능하고, 서버 비용이 비싸서 보통 스케일 아웃을 한다.

### 2-4. 로드밸런서

스케일 아웃 한 웹 서버에 부하를 고르게 분산하는 로드밸런서 설치

- 안정성 : 서버 failout 시 자동으로 연결을 끊음
- 확장성 : 반대로 서버가 추가되면 자동으로 연결

### 2-5. 데이터베이스 확장

보통 쓰기보다 읽기의 비중이 크기 때문에, 쓰기를 수행하는 주DB와 읽기를 수행하는 부DB 구성

- 성능 : 데이터 정합성을 위해 사본을 전달해야 해서 쓰기 성능이 떨어지나, 비중이 높은 읽기를 병렬로 처리해 성능이 좋아진다.
- 안정성 + 가용성 : 부DB가 죽으면 다른 부DB에 연결, 주DB가 죽으면 부DB 중 하나를 주DB로 변경

### 2-6. 캐시

데이터베이스의 읽기는 느리니, 속도가 빠른 캐시 서버에 둔다.

유의사항

- 데이터 갱신이 잦으면 사용 자제 : 캐시의 갱신은 DB 읽기와 같거나 느리다
- 휘발성 데이터만 저장 : 캐시는 서버 재시작 시 데이터 삭제
- 데이터 만료 기한 선정 : 짧으면 갱신이 잦아지고, 길면 불필요 데이터로 성능 하락
- 데이터 저장소와 캐시 저장소의 데이터 일관성 유지
- SPOF 회피 전략
- 캐시 메모리 크기 선정 : 크면 느리고 작으면 갱신이 잦아진다.
- eviction 정책 선정 : 저장 공간이 없을 때 어떤 데이터를 방출할 것인가. LRU, LFU, FIFO 등

### 2-7. CDN : 넓은 사용자 분포

Content Delivery Network. 정적 콘텐츠(이미지, html 등)를 가까운 서버에 캐싱.

동적 콘텐츠 캐싱도 있다.

고려사항

- 비용 : 콘텐츠 전송량으로 요금이 부과되어 자주 사용되지 않는 데이터는 제거
- 만료 기한 : 길면 콘텐츠 신선도가 떨어지고, 짧으면 원본 서버 조회가 잦아진다.
- 장애 대처 : CDN 이 죽었을 때 원본 서버를 조회하도록 클라이언트 구현 필요
- 콘텐츠 invalidation : 만료되지 않은 컨텐츠를 제거하는 방법

### 2-8. stateless 웹 계층

세션 등 상태 의존적 데이터를 공유 저장소에 유지하고, 서버는 stateless 하게 처리

요청을 받은 서버가 요청을 한 클라이언트에게 데이터를 돌려주기 위해 발생하는 대기 등의 비용을 줄인다.

### 2-9. 데이터 센터 : 국제적 사용자 발생

물리적으로 다른 지역에 웹 서버 + 데이터베이스 + 캐시를 묶어 구성한다.

이 때 데이터 센터 선택을 위해 geo-routing 을 사용한다.

물론, 한 데이터 센터가 죽으면 가까운 다른 센터에서 서비스한다.

고려사항

- 트래픽 우회 : 가까운 데이터 센터 선택 방법. 보통 GeoDNS
- 데이터 동기화 : 데이터 센터 간 동기화
- 테스트와 배포 : 데이터 센터가 다르면 보통 환경이 다르다. 각 환경에 맞는 테스트와 자동 배포가 필요

### 2-10. 메시지 큐

트래픽 처리 서버와 별개로 미디어 서버와 같이 별개의 작업을 수행하는 서버를 따로 구성하고,

웹 서버가 작업 서버에 비동기 요청을 보내기 위해 메시지 큐를 중간에 둔다.

### 2-11. 로그, 메트릭, 자동화

이제는 지속적인 운영을 위해 에러 로그와 CPU, 메모리 등의 메트릭 정보 모니터링이 필요하다.

CI/CD를 위해 빌드, 테스트, 배포 절차 자동화도 필요하다.

### 2-12. 데이터베이스 확장

데이터베이스도 스케일 업은 비용이 비싸고, failover 대응이 어렵다.

스케일 아웃을 위해 샤딩이 적용된다. 하나의 데이터 셋을 중복되지 않게 나누어 분산 노드에 저장.

고려사항

- 재샤딩 : shard exhaustion이 발생했을 때 데이터를 어떻게 재배치할까. 보통 안정 해시 사용
- celebrity 문제 : 특정 샤드에 질의가 집중되어 과부하가 걸리는 경우.
- 조인과 비정규화 : 샤드로 데이터를 쪼개면 join하기 어려워 애초에 데이터를 비정규화 해야한다.

### 2-13. 그 이상 : 백만 사용자 이상

시스템 최적화, 서비스를 더 작은 단위로 분할 등등

# 2장. 개략적인 규모 추정

## 1. 응답 지연 값

| 연산 | 시간 |
| --- | --- |
| L1 캐시 참조 | 0.5ns |
| 분기 예측 오류 | 5ns |
| L2 캐시 참조 | 7ns |
| mutex 락/언락 | 100ns |
| 주 메모리 참조 | 100ns |
| zippy 1kb 압축 | 10μs |
| 네트워크 2kb 전송(1Gbps) | 20μs |
| 메모리 1MB 읽기 | 250μs |
| 데이터 센터 내 메시지 왕복 | 500μs |
| 디스크 탐색 | 10ms |
| 네트워크 1mb 읽기 | 10ms |
| 디스크 1mb 읽기 | 30ms |
| 네트워크 패킷 지구 한바퀴 | 150ms |

알 수 있는 것

- L1 캐시 참조 : 캐시는 여전히 엄청 빠르다
- 주 메모리 참조 : RAM은 하드디스크와는 비교가 불가하다
- zippy : 기본적인 압축은 생각보다 빠르다. 네트워크는 압축을 하는 것이 기본이다.
- 네트워크 패킷 지구 한 바퀴 : 지역별 데이터 센터는 필수적이다.

## 2. 가용성 수치

| 가용률 | 연간 장애 시간 |
| --- | --- |
| 99% | 3.65일 |
| 99.9% | 8.77시간 |
| 99.99% | 52.60분 |
| 99.999% | 5.26분 |
| 99.9999% | 31.56초 |

## 3. QPS 측정

QPS : Query Per Seconds = 사용자 * 사용율 * 평균 질의 수 * 용량(미디어, 텍스트 구분) * 데이터 저장 기간

**주의사항**

- 근사치로 계산. 정확한 값이 아니라 규모를 산정하는 정도의 개념
- 가정은 같이 적을 것
- 단위를 빼먹지 말 것
- QPS, 최대 QPS, 저장소 요구량, 캐시 요구량, 서버 수 추정 등의 문제가 출제된다.

# 3장. 시스템 설계 면접 공략법

## 1. 4단계 접근법

### 1단계 : 문제 이해 및 설계 범위 확정 (3~10분)

혼자 가정하지 말고, 질문을 통해 요구사항을 구체화 / 수치화 할 것

중요한 기능을 특정하고 구체화할 것

스타트 업의 시스템과 중견 기업의 시스템 설계는 다르다. 요구사항을 다시 확인할 것

요구사항이 정확하지 않으면 2단계로 넘어가지 말 것

### 2단계 : 개략적인 설계안 제시 및 동의 구하기 (10~15분)

상세 기능이 아닌 기본적인 핵심 컴포넌트 수준에서 청사진을 그릴 것

면접관을 동료라 생각하고 그린 청사진에 대한 의견을 물을 것

설계 중 관련된 제약사항에 만족하는 지 “소리내어" 계산할 것

구체적인 사용 사례를 적용해 edge case 발굴할 것

문제에 대한 해결법은 가능한 여러 개를 제시할 것

### 3단계 : 상세 설계 (10~25분)

면접관과의 커뮤니케이션을 통해 컴포넌트 사이의 우선순위 선정 (성능 관련일 수도, 기능일 수도 있다)

컴포넌트의 세부사항을 면접관에게 설명할 것. 가장 중요한 컴포넌트 부터 시작하자

기능에 들어갈 알고리즘과 같이 전반적인 시스템이나 성능에 관련이 없으면 설명에 시간을 많이 할애하지 말자

모르면 힌트를 청하고, 침묵은 피하자

### 4단계 : 마무리 (3~5분)

완벽한 설계는 존재하지 않는다. 발생 가능한 병목이나 개선 가능한 지점을 설명하자

면접이 길었다면 전체적인 내용을 다시 한 번 설명해주자

면접관이 끝났다고 하지 않으면 끝난 것이 아니다. 의견을 더 구하자

오류가 발생하면 어떤 일이 생기는지 따져보자

이후 운영에 관한 로그, 메트릭, 배포 등의 방법도 논의하자

현재 시스템이 감당 가능한 트래픽과 규모 확장을 위해 해야할 방법을 고려하자

# 4장. 처리율 제한 장치 설계

> 처리율 제한 장치 : 트래픽 처리율 제어를 위해 요청 횟수 제한
> 

## 1. 처리율 제한 장치

### 장점

- DoS 공격 방어
- 비용 절감 : 서버를 많이 두지 않아도 됨
- 서버 과부하 방어

### 단점

- 응답 시간에 영향
- 장치가 죽었을 때에 대한 방어 코드 필요

## 2. 알고리즘

### 토큰 버킷

일정 시간 마다 N개의 토큰을 발행해 최대 용량 M이 정해진 버킷에 담고, 요청 인입 시 버킷에 들어있는 토큰을 사용한다.

토큰이 없으면 버린다

- 장점 : 구현이 쉽다. 짧은 시간에 트래픽이 집중되어도 처리가 가능하다
- 단점 : 버킷 크기(M)와 토큰 공급률(N)을 튜닝하기 어렵다.

### 누출 버킷

최대 크기 N이 정해진 큐에 요청을 담고 큐에 담긴 요청을 고정된 속도 V로 처리한다.

큐가 가득찼을 때 수신한 요청을 버린다.

- 장점 : 큐의 크기가 정해져있어 메모리 효율적. 속도도 제한적이라 출력이 안정적
- 단점 : 트래픽이 집중되면 큐에 오래된 요청이 쌓여 최신 요청이 전부 버려짐. N, V값 튜닝도 어렵다.

### 고정 윈도 카운터

단위 시간 T 동안 받을 수 있는 요청의 개수 N을 정해, 넘으면 버린다.

- 장점 : 메모리 효율이 좋다. 이해도 쉽다. 특정한 트래픽 패턴이 있다면 적절하다.
- 단점 : 윈도우의 경계에 트래픽이 집중되면 서비스는 기대 작업량보다 일이 많아진다.

### 이동 윈도 로깅

요청이 도달한 순간부터 지정한 시간 T 만큼의 윈도우 동안 수신할 요청의 개수 N을 정한다. 이 N에는 버려진 요청을 포함한다.

N을 넘는 요청은 버려진다.

- 장점 : 모든 순간의 윈도우가 처리율을 절대로 넘지 않는다.
- 단점 : 버려진 요청의 타임스탬프를 저장해 메모리 효율이 떨어진다.

### 이동 윈도 카운터

현재 윈도우의 요청 수 + 직전 윈도우 요청수 * (윈도우 크기 - 현재 요청 도달 시간) 으로 처리율 계산

직전 윈도우의 요청이 고르게 분포한다고 가정해 현재 요청 기준 윈도우가 겹치는 부분을 더하는 것.

- 장점 : 이전 윈도우를 고려하므로 짧은 시간에 트래픽이 몰려도 대응이 가능하다. 메모리 효율도 좋다.
- 단점 : 직전 윈도우 요청이 고르게 분포한다고 가정하기 때문에 완벽하지는 않다.(심각하진 않다)

## 3. 단계별 설계

### 1단계 문제 이해 및 설계 범위 확정

요구사항 확정

- 처리 속도, 메모리 제한
- 처리율 제한과 관련된 특징. 티켓팅 같은 건 빡빡하게 잡아야겠지
- 처리율 제한 시 사용자에게 알릴 것인가 등등

### 2단계 개략적 설계안 제시 및 동의 구하기

**설계**

- 제한 기준 : API, ID , IP
- 설치 위치 : 클라이언트, 서버, 미들웨어
- 제한 수준 : hard, soft
- 사용 알고리즘 설정 : 토큰 버킷, 누출 버킷, 고정 윈도 카운터, 이동 윈도 로깅, 이동 윈도 카운터
- 구현 방법 : 직접 구현, 서드 파티 사용, 기 구현된 API 게이트웨이 기능 사용
- 처리율 제한 시 처리 : 429 에러 또는 모른척

**아키텍쳐 설계**

- 카운터의 저장 : time based expire를 지원하는 캐시가 적절하다.

redis는 메모리 기반 저장장치지만 INCR, EXPIRE 등 적절한 연산자를 지원해서 많이 사용한다

(INCR : increase - 카운터 값 1 증가, EXPIRE : 카운터에 만료 시간 설정)

- 동작 : 요청 인입 → redis의 카운터 값 참조 → 처리 → 카운터 값 변경

### 3단계 상세 설계

**처리율 제한 규칙**

- 규칙 생성 방법 : 설정 파일 작성
- 규칙 저장 위치 : 디스크에 저장하고 서버에 캐싱(주기적으로 동기화)

**제한된 요청 처리 방법**

- 429 too many requests + HTTP 헤더 : 남은 요청 횟수, 요청 제한 규칙, 제한이 풀리는 시간 등
- 요청 유지 : 메시지 큐에 담아 대기

**분산 환경에서의 처리율 제한**

- 카운터 접근 경쟁조건 해결 : lock, Lua script, redis 자료구조 - sorted set 사용
- 동기화 : redis를 중앙 집중형으로 공용으로 사용

**최적화**

- 지연시간 : 당연히 느려진다. 사용자와 물리적으로 가까운 지역에 edge server를 심어 그나마 빠르게 만들자.
- eventual consistency model : 키-값 저장소 설계 (6장 내용 참고..?)

**모니터링**

- 알고리즘의 효율성 모니터링 : 트래픽이 집중될 가능성이 있다면 일시적으로 알고리즘을 바꿀 수 있다.
- 처리율 제한 규칙의 효율성 모니터링

### 4단계 마무리

- 처리율 적용 강도 : hard / soft
- 다양한 계층의 제한 : API 단위의 제한은 OSI 7단계. Iptables를 이용하면 3단계에서도 적용이 가능
- 처리율 제한 회피 : 클라이언트 캐시, 클라이언트에서도 제한, 무한 요청이 발생하지 않도록 설계, retry 할 때는 일정 시간 대기

# 5장. 안정 해시 설계

## 1. 용어

- 해시 키 재배치 : 분산 서버에 데이터를 분산해서 저장했는데, 서버 장애, 추가, 삭제 등의 이유로 기존 데이터를 다시 재배치 하는 상황
- 해시 키 재배치 문제 : 해시 키를 modulo 연산으로 분배하면 전체 데이터의 재배치가 발생할 수 있다.
- 안정 해시 : 해시 테이블 크기가 조정될 때 k/n개의 키만 재배치하는 기술
- 해시 공간 : 해시 함수의 출력 값 범위
- 해시 링 : 해시 공간의 시작과 끝을 붙여서 동그랗게 만든 것
- 파티션 : 인접한 서버 사이의 해시 공간

## 2. 안정 해시 구현

### 2-1. 기본 구현법

**1. 해시 서버 배치**

각 서버를 해시 링 위에 배치한다.

**2. 서버 조회**

각 해시 키 위치에서 해시 링을 시계방향으로 탐색해 처음 만나는 서버에 저장

**3. 서버 추가**

추가된 서버 Sn과 그 직전의 서버 S(n-1) 사이의 해시 키를 S(n+1) → Sn으로 재배치한다.

**4. 서버 제거**

제거된 서버 Sn과 그 직전 서버 S(n-1) 사이의 해시 키를 Sn → S(n+1)로 재배치한다.

### 2-2. 기본 구현법의 두 가지 문제

**파티션 크기 균등 유지 불가능**

균등하게 파티션을 배분해도 서버의 추가나 삭제가 발생하면 파티션으 크기가 바뀐다.

**키의 균등 분포 불가능**

서버와 서버 사이에 키를 세어서 균등하게 서버를 배포해도, 키의 추가나 서버가 추가되면 망함.

위 두 가지 문제를 가상 노드로 해결한다.

### 2-3. 가상 노드

하나의 서버가 해시 링에 한 군데에만 배치하는 것이 아니라, 여러 곳에 배치

가상 노드의 개수가 늘어나면 점점 더 균등해지지만, 저장 공간이 많이 필요하다.

- 가상노드 개수에 따른 표준편차 : 100개 10% ~ 200개 5%

## 3. 안정 해시의 장점

- 서버 개수 변경 시 재배치되는 키의 수를 최소화
- modulo로 만든 해시나 기본 구현법보다 데이터를 균등하게 저장해 수평적 규모 확장성 달성이 쉽다
- 데이터 균등 저장으로 특정 샤드에 지나친 접근으로 서버에 과부하를 일으키는 핫스팟 문제를 줄인다.

# 6장. 키-값 저장소 설계

## 6-1. key-value store

(k,v) pair를 저장하는 데이터베이스로 보통 non-RDB 이다.

key : 해시를 쓰기도, 텍스트를 쓰기도 한다. 짧을수록 빠르다

value : RDB가 아니라서 저장하는 형식이 정해져있지 않다. list, object, string 암거나

## 6-2. 요구사항

- pair의 크기
- 저장할 데이터의 대략적인 총량
- 가용성 vs 일관성
- 자동 규모 확장 여부
- 응답 지연시간 수준

## 6-3. 단일 서버 키-값 저장소

그냥 다 저장하면 된다. 용량이 아까우니 압축정도만

자주 쓰이는 데이터는 메모리에 캐싱

## 6-4. **CAP 정리**

Consistency, Availability, Partition tolerance 를 모두 만족하는 분산 시스템은 불가능하다는 정리

- Consistency : 접속한 노드와 상관없이 항상 같은 데이터를 반환
- Availability : 일부 노드에 장애가 발생해도 응답을 받을 수 있어야 함
- Partition tolerance : 파티션 간 네트워크 장애가 발생해도 시스템의 동작이 유지되어야 함

CP 시스템 : P 문제가 생기면 데이터 갱신을 막고 같은 데이터만 반환

AP 시스템 : P 문제가 생기면 데이터 일관성 유지를 포기하고 계속해서 데이터 갱신을 제공

CA 시스템 : P 문제가 없는 현실 시스템은 없다. 실세계에 존재하지 않는 시스템

## 6-5. 분산 시스템 컴포넌트

### **데이터 파티션**

5장의 안정 해시로 서버를 데이터를 나누어 서버에 배치

장점 : automatic scaling 가능, heterogeneity(다양성) 지원 - 환경에 따라 가상 노드 조정

### **데이터 일관성**

중재자가 읽기 쓰기 연산이 발생했을 때 특정 개수 이상의 서버에서 연산 성공 응답을 받아 동기화

Quorum Consensus 프로토콜 사용

N : 사본 개수, W : 쓰기 quorum, R : 읽기 quorum

- W = R = 1 : 일관성 보장 X. 응답속도는 빠름
- R = 1, W = N : 빠른 읽기 최적화
- W = 1, R = N : 빠른 쓰기 최적화
- W + R > N : 강한 일관성 보장 (보통 N=3, W=R=2)
- W + R ≤ N : 강한 일관성 보장 안 함

**일관성 종류**

- 강한 일관성 : 항상 일관성 유지 → AP 시스템에 부적합
- 약한 일관성 : 읽기 연산이 가장 최근의 데이터 반환을 보장하지 않음
- 최종 일관성 : 약한 일관성이지만, 여유있을 때 다시 동기화한다. → CP 시스템에 부적합

**비일관성 해소 기법 : 데이터 버저닝**

- 벡터 시계 : [서버, 버전]의 순서쌍을 데이터에 매단 것
- 이전 버전 판단 : 버전 X의 모든 순서쌍이 버전 Y의 순서쌍보다 같거나 작으면 이전 버전
- 버전 충돌 판단 : 버전 X의 순서쌍 중 일부가 Y의 순서쌍보다 크고, 일부는 작으면 충돌

충돌을 자동으로 발견하고 해결하는 시스템을 버저닝 시스템이라 부른다. 보통 벡터시계를 이용한다.

문제점

- 클라이언트에서 충돌을 판단하기 때문에 클라이언트 소스가 복잡해짐
- 갱신될 때마다 순서쌍이 늘어버림. threshold를 설정해 오래된 순서쌍을 버려야한다. 이러면 버전 선후 관계 판단이 어려워질 수 있다

### 장애처리

**장애 감지**

가십 프로토콜 : 분산형 장애 감지 솔루션

- 노드 내에 (서버, hearbeat counter)를 저장하는 membership list를 갖는다.
- 각 노드는 주기적으로 본인의 heartbeat을 하나 올린다
- 주기적으로 무작위 노드에 내 membership list를 보낸다
- 받은 노드에서는 수신한 membership list로 값 업데이트
- 일정 시간 동안 갱신되지 않은 member를 장애 서버로 판단

**일시적 장애 처리**

sloppy quorum : 원래 처리할 서버가 중재자에 연산 성공 응답을 주는 것이 아니라,<br/>
임시로 건강한 다른 서버가 처리하는 것. 이 때 저장한 데이터는 임시 표시를 해두고, 장애 서버가 복구되면 그쪽으로 인계한다.

- strict quorum VS sloppy quorum : 엄격한 건 강한 일관성을 유지하는 것. 느슨한 건 최종 일관성을 유지하는 것

**영구적 장애 처리**

- 복구 방법 : anti-entropy 프로토콜 - 사본들을 비교해 최신 버전으로 갱신
- 데이터가 다른 사본 탐지 : merkle 트리 - 자식 노드의 레이블(또는 해시)을 이용해 해시를 계산해 내 레이블에 저장하는 이진 트리

→ 사본 간 부모의 해시가 다를 때 자식의 해시 끼리 비교해서 다른 부분을 찾아 내려가 데이터의 크기와 상관없이 log(트리의 높이) 면 찾는다.

→ 하지만 생각보다는 관리할 해시 키가 많아진다는 것은 기억하자

- 다른 데이터 센터에 다중화

### Cassandra의 읽기 쓰기 경로

**읽기 경로**

1. 쓰기 요청을 커밋 로그 파일에 기록
2. 데이터를 메모리 캐시에 저장
3. 메모리 캐시가 꽉 차면 SSTable에 저장

**쓰기 경로**

1. 메모리 캐시를 확인
2. 없으면 Bloom filter로 어느 SSTable에 데이터가 있는지 확인
3. SSTable에서 데이터를 조회해 반환
