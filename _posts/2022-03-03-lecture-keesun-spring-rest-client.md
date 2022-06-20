---

layout: single
title: \[강의요약\] 스프링부트 개념과 활용 - 스프링 REST 클라이언트
date: 2022-03-03 22:26:00 +0900
categories: lecture_summary springboot springboot_getting_started
toc: true
toc_sticky: true
toc_label: Contents
show_in_home: false
---

개인적인 학습을 위한 [Inflearn - 스프링부트 개념과 활용](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8/dashboard)(백기선) 강의 요약입니다.

개념과 원리 위주로 요약합니다.

[이전 글](https://cherrue.github.io/lecture_summary/springboot/springboot_getting_started/lecture-keesun0-spring-security/) 에서 이어집니다.

# 4부. 스프링 부트 활용 - 스프링 REST 클라이언트

---

## 1. RestTemplate과 WebClient

신규 프로젝트 생성 : springbootrestclient (의존성 web만)

RestClient은 스프링의 기능

스프링 부트는 RestTemplateBuilder, WebClient.builder 를 등록

**1-1. RestTemplate : Blocking I/O 기반의 synchronous API**

순차적으로 실행하고, Thread.sleep이 있으면 그게 끝날 때 까지 기다림

컨트롤러 작성

```java
@RestController
public class SampleController {
    @GetMapping("/hello")
    public String hello() throws InterruptedException {
        Thread.sleep(5000L);
        return "hello";
    }
    @GetMapping("/world")
    public String world() throws InterruptedException {
        Thread.sleep(3000L);
        return "world";
    }
}
```

러너 작성

```java
@Component
public class RestRunner implements ApplicationRunner {

    @Autowired // spring-boot-starter-web 에서 주입
    RestTemplateBuilder restTemplateBuilder;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        RestTemplate restTemplate = restTemplateBuilder.build();

        StopWatch stopWatch = new StopWatch();
        stopWatch.start();

        String helloResult = restTemplate.getForObject("http://localhost:8080/hello", String.class);
        System.out.println(helloResult);

        String worldResult = restTemplate.getForObject("http://localhost:8080/world", String.class);
        System.out.println(worldResult);

        stopWatch.stop();
        System.out.println(stopWatch.prettyPrint());
    }
}
```

**결과**

```java
hello
world
StopWatch '': running time = 8149928815 ns
---------------------------------------------
ns         %     Task name
---------------------------------------------
8149928815  100%
```

**1-2. WebClient : Non-Blocking I/O 기반의 Asynchronous API**

의존성 추가

```xml
<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-webflux</artifactId>
        </dependency>
```

runner 작성

```java
@Component
public class WebRunner implements ApplicationRunner {

    @Autowired
    WebClient.Builder builder;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        WebClient webClient = builder.build();

        StopWatch stopWatch = new StopWatch();
        stopWatch.start();

        Mono<String> helloMono = webClient.get().uri("http://localhost:8080/hello")
                .retrieve()
                .bodyToMono(String.class);
        helloMono.subscribe(s -> {
            System.out.println(s);

            if(stopWatch.isRunning()) {
                stopWatch.stop();
            }
            System.out.println(stopWatch.prettyPrint());
            stopWatch.start();
        });

        Mono<String> worldMono = webClient.get().uri("http://localhost:8080/world")
                .retrieve()
                .bodyToMono(String.class);

        worldMono.subscribe(s -> {
            System.out.println(s);

            if(stopWatch.isRunning()) {
                stopWatch.stop();
            }
            System.out.println(stopWatch.prettyPrint());
            stopWatch.start();
        });

        stopWatch.stop();
        System.out.println(stopWatch.prettyPrint());
    }
}
```

**결과**

```java
world
StopWatch '': running time = 212657951 ns
---------------------------------------------
ns         %     Task name
---------------------------------------------
212657951  100%  

hello
StopWatch '': running time = 2178554336 ns
---------------------------------------------
ns         %     Task name
---------------------------------------------
212657951  010%  
1965896385  090%
```

## 2. 커스터마이징

WebClient.builder와 RestTemplateBuilder 둘 다 커스텀 안 해도 충분히 쓸 수 있다.

defaultCookie, defaultHeader, baseUrl 등 설정 가능

2-1. 로컬(지역적) 설정 : builder 와 .build() 함수 사이에 함수 호출

```java
		@Override
    public void run(ApplicationArguments args) throws Exception {
        WebClient webClient = builder
                .baseUrl("http://localhost:8080")
								.build();

        StopWatch stopWatch = new StopWatch();
        stopWatch.start();

        Mono<String> helloMono = webClient.get().uri("/hello")
...
```

2-2. 글로벌 설정 : WebClientCustomizer 빈 등록 또는 WebClientBuilder를 재구현해도 가능

```java
@SpringBootApplication
public class SpringbootrestclientApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootrestclientApplication.class, args);
    }

    @Bean
    public WebClientCustomizer webClientCustomizer() {
        return webClientBuilder -> webClientBuilder.baseUrl("http://localhost:8080");
    }
}
```

2-3. HttpClient 사용이 강제되는 경우

의존성 추가

```xml
		<dependency>
            <groupId>org.apache.httpcomponents</groupId>
            <artifactId>httpclient</artifactId>
        </dependency>
```

빈 등록

```java
@SpringBootApplication
public class SpringbootrestclientApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootrestclientApplication.class, args);
    }

    @Bean
    public WebClientCustomizer webClientCustomizer() {
        return webClientBuilder -> webClientBuilder.baseUrl("http://localhost:8080");
    }
    
    @Bean
// 요거 추가
    public RestTemplateCustomizer restTemplateCustomizer() {
        return restTemplate -> restTemplate.setRequestFactory(new HttpComponentsClientHttpRequestFactory());
    }
}
```

## 3. 그밖에 다양한 기술 연동

3-1. 캐시

다양한 캐시 구현체를 지원. spring framework에서 해주는 것이고, spring boot는 자동설정을 해주는 것

3-2. messaging

3-3. web socket, web service, jmx 뭐 등등등 굉장히 많으니, reference를 확인할 것
