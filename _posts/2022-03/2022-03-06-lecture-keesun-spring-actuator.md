---
layout: single
title: \[강의요약\] 스프링부트 개념과 활용 - 스프링 Actuator
date: 2022-03-06 21:57:00 +0900
categories: lecture_summary springboot springboot_getting_started
toc: true
toc_sticky: true
toc_label: Contents
---

개인적인 학습을 위한 [Inflearn - 스프링부트 개념과 활용](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8/dashboard)(백기선) 강의 요약입니다.

실습 위주로 요약합니다.

[이전 글](https://cherrue.github.io/lecture_summary/springboot/springboot_getting_started/lecture-keesun-spring-rest-client/) 에서 이어집니다.

# 5부. 스프링 부트 운영 - 스프링 부트 Actuator

---

## 1. Actuator 소개

Actuator : Endpoint를 통해 운영중에 주시할 수 있는 유용한 정보 제공

- 유용한 정보 : metric 정보, 아니면 logging level도 운영중에 재기동 없이 바꿀 수 있다.

신규 프로젝트 생성 : springbootactuator (의존성 web 만)

**1-1. 의존성 추가**

```xml
		<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
```

**결과**

(json formatter 크롬 플러그인을 사용중이라 모양이 좀 다르게 보일 수 있습니다)

![1_actuator](/assets/images/2022-03/06/1_actuator.png)

hateoas 형식으로 보여줌 : 현재 보여주는 리소스와 연관된 상태를 링크로 만들어 줌

shutdown을 제외하고 모두 **활성화(enable)**는 되어있지만, **공개(expose)**는 health와 Info 뿐

→ JMX는 거의 다 열려있음. JMX를 먼저 살펴보자

## 2. JMX와 HTTP

2-1. jconsole

```bash
# application이 떠있는 상태에서 터미널에 jconsole 입력
$ jconsole
```

**결과**

![2_jconsole](/assets/images/2022-03/06/2_jconsole.png)

목록에서 스프링 애플리케이션을 선택 > connect 버튼 클릭 > insecure connect 클릭

![3_jconsole_application](/assets/images/2022-03/06/3_jconsole_application.png)

MBean 탭에서 Endpoint들을 볼 수 있지만, 보기 너무 불편하다.

2-2. VisualVM

java10 이후 버전을 쓴다면 설치가 필요하다. 이전 버전은 JDK에 포함되어 있다.

```bash
# application이 떠있는 상태에서 터미널에 jvisualvm 입력
$ jvisualvm
```

**결과**

바로 어플리케이션이 안 잡힐 수 있다. 조금 기다리자

![4_jvisualvm](/assets/images/2022-03/06/4_jvisualvm.png)

2-3. 웹으로 보기

웹으로 보려면 공개 설정을 해주어야 한다.

```bash
# application.properties
management.endpoints.web.exposure.include=*
# management.endpoints.web.exposure.exclude=env,beans
```

**결과**

모든 mbean이 보인다. 너무 길어 아래는 잘랐다.

![5_actuator_expose](/assets/images/2022-03/06/5_actuator_expose.png)

## 3. 스프링 부트 어드민

spring boot admin : actuator를 ui로 제공. spring boot에서 제공하는 것은 아님

admin server 역할을 할 추가 프로젝트 생성 : springbootmonitor (의존성 웹)

**3-1. 의존성 추가**

평소엔 수업대로 2.2.0.RELEASE 에 맞춰서 썼는데, 버그가 있다. 
spring-boot-starter-parent 와 아래 의존성 모두 2.6.2로 맞추어주니 문제 없다.

admin에는 민감한 정보가 있을 수 있으니 실 사용 시 security를 적용할 것

```xml
		<dependency>
            <groupId>de.codecentric</groupId>
            <artifactId>spring-boot-admin-starter-server</artifactId>
            <version>2.6.2</version>
        </dependency>
```

**3-2. SpringBootApplication에 EnableAdminServer 어노테이션 추가**

```java
@SpringBootApplication
@EnableAdminServer
public class SpringbootmonitorApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootmonitorApplication.class, args);
    }
}
```

**3-3. client 의존성 추가**

```java
		<dependency>
            <groupId>de.codecentric</groupId>
            <artifactId>spring-boot-admin-starter-client</artifactId>
            <version>2.0.1</version>
        </dependency>
```

**3-4. client 가 admin을 보도록 application.properties 설정**

```java
// springbootactuator > application.properties
management.endpoints.web.exposure.include=*
server.port=18080
spring.boot.admin.client.url=http://localhost:8080
```

**결과**

![6_admin_main](/assets/images/2022-03/06/6_admin_main.png)

위 화면에서 저 url이 아니라 id를 눌러야 한다.

문제는 외부 ip로 나갔다가 들어와서, 방화벽을 열어두지 않으면 아래 처럼 500에러가 떠버리는 것 같다.

![7_admin_application](/assets/images/2022-03/06/7_admin_application.png)

# 6부. 마무리

## 강의 마무리

**스프링 부트 원리** : 가장 중요한 파트!

- 의존성 관리
- 자동설정
- 내장 웹서버
- JAR 패키징, WAR 패키징 로더

**스프링 부트 활용** : 웹 개발의 가장 기반이 되는 기능들 소개

- 웹 개발
- 데이터베이스 연동
- NoSQL 연동
- 시큐리티
- Rest Template

+ 캐싱, 이메일 보내기 등등 더 많은 기능이 있답니다.

**스프링 부트 운영**

- Actuator
- 스프링 부트 어드민

스프링 mvc, 스프링 webflux 중요한데, 스프링 부트에서 소개하긴 좀 애매하니 다른 강의를 보자