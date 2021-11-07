---
layout: single
title: 'Spring Boot 초기 설정'
date: 2021-11-07 17:31:00 +0900
categories: springboot, project

---

# Spring Boot 초기 설정

### spring boot 시작

spring boot 프로젝트는 https://start.spring.io 에서 쉽게 만들 수 있다.

아래와 같이 만들어주자

![spring_boot_dependency.png](/assets/images/2021-10-17/spring_boot_dependency.png)



### 라이브러리 추가

1. 로그 라이브러리 : slf4j + log4j2
   - slf4j : 로깅 라이브러리의 인터페이스 모듈. 로깅 라이브러리를 log4j2, logback 등을 바꿔야 할 때 굉장히 쉽게 이관이 가능하다
     @slf4j 어노테이션을 추가하고 log.debug() 등으로 호출하면 사용된다.
   - log4j2 : logback보다 기능이 좀 더 많지만 성능이 조금 안 좋다. java log package보다는 확실히 좋다.
     logback이 spring 기본 로거이고, application.properties로 잡아줄 수도 있어 편하긴 하다. 
     log4j2로 다 만들고 나면 logback 이관하는 것도 해보자
     log4j2.xml 파일을 통해 로깅 설정을 잡아줄 수 있다. jackson 패키지를 이용해 다른 형식으로도 지정할 수 있다.
2. json wrapper : jackson + gson.
   - jackson : spring 내장 json 객체 생성기 (build.gradle 작성 X)
     @RestController가 붙어있는 컨트롤러에 응답을 (lombok) getter/setter가 있는 객체로 반환하면 자동으로 생성함.
   - gson : JsonObject를 만들 수 있는 라이브러리. 딕셔너리 기반인데 빠르진 않으므로 사용을 자제할 것



### 테스트 API 작성

1. 컨트롤러 작성 : MVC의 컨트롤러 담당

   ```java
   @RestController
   public class DramaController {
   
       private TestService testService;
   
       @Autowired
       public DramaController(TestService testService){
           this.testService = testService;
       }
   
       @GetMapping("/drama/test")
       public Object testApi(){
           return testService.getTestEntity();
       }
   }
   ```

2. 서비스 작성  : 비즈니스 로직 담당

   ```java
   @Service
   public class TestService {
   
       public TestEntity getTestEntity(){
           return new TestEntity();
       }
   }
   ```

3. Entity 작성 : MVC의 모델 담당

   ```java
   @Getter
   @Setter
   public class TestEntity {
       String result = "Drama server is Alive!";
   }
   ```

### 테스트

```java
$ curl localhost:8082/drama/test
```

