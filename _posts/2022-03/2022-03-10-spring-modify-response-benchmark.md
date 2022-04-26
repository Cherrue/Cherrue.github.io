---

layout: single
title: \[성능비교\] Spring 응답 수정 방법 4 가지 성능 비교
date: 2022-03-10 22:32:00 +0900
categories: spring benchmark
toc: true
toc_sticky: true
toc_label: Contents

---

하나의 REST 어플리케이션으로 여러 플랫폼을 서비스 할 때

같은 API 지만 플랫폼에 따라 다른 응답이 주고 싶은 경우가 있다.

API 를 나누는 것이 정석이지만, 여러 여건으로 불가능 할 때 응답만 바꾸는 방법을 알아보고 비교하자.

전체 소스코드는 https://github.com/Cherrue/spring-response-modify-compare 참고

# 응답 수정 방법

내 경우 특정 플랫폼에서 부가 정보를 제거하고 반환하는 것이 목적이기 때문에

기본 정보를 갖는 ParentEntity 와 부가 정보를 갖는 ChildEntity 를 만들어

응답 후처리에서 ChildEntity의 필드를 제거하는 방법을 아래 4 가지로 구현했다.

1. Filter
2. HttpMessageConverter
3. AOP
4. 비즈니스 내 단순 분기 처리

## Filter

filter 는 servlet이 호출되기 전후에 처리하고 싶은 공통적인 로직을 처리하는 sevlet 스펙의 기술이다.

servlet 스펙이기 때문에 Spring 컨텍스트 외부에 존재한다.

### Filter 구현

필터에 넘어온 응답은 객체가 아니라 byte stream 형태이다.

1. 읽어올 수 있는 byte stream을 갖는 ResponseBodyWrapper 를 filterChain 에 보내고,
2. 돌아온 Wrapper의 내용을 문자열로 바꾸고
3. 원하는 내용만 남긴 후
4. byte stream에 write하여 응답으로 내보낸다.

**소스코드 (stream 등은 github > modifybyfilter > ... > filter 패키지 참고)**

```java
public class SampleFilter implements Filter {
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        // 1. 원래 response 대신 wrapper 를 컨트롤러에 보낸다.
        ResponseBodyWrapper responseBodyWrapper = new ResponseBodyWrapper((HttpServletResponse) servletResponse);
        filterChain.doFilter(servletRequest, responseBodyWrapper);
        // 2. 요청이 끝난 후 wrapper 에 담긴 응답을 꺼낸다
        String oldResponseMessage = new String(responseBodyWrapper.getDataStream(), StandardCharsets.UTF_8);

        // 3. jackson 으로 부모 형식으로 변환
        ObjectMapper objectMapper = objectMapper();
        ParentEntity parentEntity = objectMapper.readValue(oldResponseMessage, ParentEntity.class);
        String newResponseMessage = objectMapper.writeValueAsString(parentEntity);
				// 4. 원래 response 에 데이터 쓰기
        servletResponse.getOutputStream().write(newResponseMessage.getBytes());

    }
}
```

## HttpMessageConverter

spring 을 사용하면 default 로 jackson 컨버터를 사용하여 객체를 json 으로 변환한다.

이 jackson 은 특정 객체에 대해 커스텀 serializer 를 만들어 붙일 수 있다.

### HttpMessageConverter 변경 구현

커스텀 serializer 에서 제거하고자 하는 필드는 json 추가하지 않도록 작성하면 된다.

**소스코드 (커스텀 serializer 는 github > modifybyconverter > ... > converter 패키지 참고)**

```java
@Configuration
public class SampleConfiguration extends WebMvcConfigurationSupport {
    @Override
    protected void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        converters.add(new SampleConverter().sampleConverter());
        super.configureMessageConverters(converters);
    }
}
```

## AOP

AOP(Aspect Oriented Programming) 란 관점 지향 프로그래밍으로, 관심사에 따라 모듈화 한다는 개념이다.

Spring boot 에서는 spring-boot-starter-aop를 지원한다.

Spring AOP는 성능에 영향을 많이 끼쳐서 사용에 주의해야 한다.

### 응답 변경 관점 AOP 구현

aop를 처음 써봐서 굉장히 간단히 구현했다.

@GetMapping이 붙은 함수가 결과를 반환할 때 결과 값을 가로채서 수정하도록 작성했다.

**소스코드**

```java
@Aspect
@Component
public class SampleAop {
    @Pointcut("@annotation(org.springframework.web.bind.annotation.GetMapping)")
    private void controllerPoint() {}

    @AfterReturning(pointcut = "controllerPoint()", returning = "result")
    public void afterReturning(ChildEntity result) {
        result.setData2(null);
    }
}
```

jackson null 필드 무시 옵션 추가 (application.properties)

```java
spring.jackson.default-property-inclusion=non_null
```

## 비즈니스 내 분기처리

소스가 굉장히 지저분해지지만, 성능 비교를 위해 작성했다.

**소스코드**

controller 에서 값을 바꿔치는 내용이다.

```java
@RestController
public class SampleController {
    @GetMapping("/controller")
    public ParentEntity filter() {
        ChildEntity childEntity = new ChildEntity();
        childEntity.setData1("data1");
        childEntity.setData2("data2");

        ParentEntity parentEntity = new ParentEntity();
        parentEntity.setData1(childEntity.getData1());
        return parentEntity;
    }
}
```

# 속도 비교

## 환경

부하테스트나 벤치마크 테스트로 하고 싶었는데, 구현이 잘 안 됐다.
| 환경 | 버전 |
| --- | --- |
| java | 1.8.0_161 |
| springboot | 2.3.0.RELEASE |
| OS | macOS Monterey 12.1 |
| 테스트 방법 | junit repeat test |
| 테스트 횟수 | 100 times * 100 rounds |

**테스트 방법**

기동된 후 첫번째 응답은 느려서 버리고, 그 후 100번의 응답 시간 합을 출력한다.

- 응답이 실패하면 테스트가 멈춘다.
- @SpringBootTest 는 어플리케이션이 기동된 후 @Test 를 수행한다.

```java
@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.MOCK)
@AutoConfigureMockMvc
public class SampleTest {
    @Autowired
    MockMvc mockMvc;

    @Test
    @Repeat(100)
    public void test() throws Exception {
        long takedTime = 0L;
        StopWatch sw = new StopWatch();
        mockMvc.perform(get("/controller"))
                .andExpect(status().isOk());

        for(int i=0; i<100; i++) {
            sw.start();
            mockMvc.perform(get("/controller"))
                    .andExpect(status().isOk());
            sw.stop();
            takedTime += sw.getLastTaskTimeNanos();
        }
        System.out.println(takedTime);
    }
}
```

## 결과


| 구분 | normal | aop | controller | converter | filter |
| --- | --- | --- | --- | --- | --- |
| sum (ns) | 1491188852 | 1829324493 | 1500203548 | 1394589610 | 2424188072 |
| avg (ns) | 14911888.52 | 18293244.93 | 15002035.48 | 13945896.1 | 24241880.72 |
| 순위 |  | 3위 | 공동 1위 | 공동 1위 | 4위 |

- normal : 아무것도 변경하지 않은 프로젝트
- controller : 비즈니스 로직을 수정한 프로젝트
- 전체 수행 결과는 https://github.com/Cherrue/spring-response-modify-compare > readme 참고
  
**결과 분석**

normal과 비교했을 때 controller 와 converter는 성능이 같다고 봐야한다.

기동될 때 커스텀 serializer 를 등록하는 과정만 추가될 뿐 동작은 같기 때문이다.

AOP의 경우 filter보다 빠른 것으로 보이는데, 기존에 사용하던 AOP가 있는가, pointcut을 어노테이션으로 할 것인가 등등 요인에 따라 더 느려질 수 있다.

filter 의 경우 처리가 끝난 byte stream을 객체까지 변환하면서 시간이 오래걸리는 것 같다.

# 결론

converter 가 구현할 때 가장 귀찮은 대신, 성능에 영향이 없다.

filter가 구현이 가장 쉬운 대신, 성능에 영향을 많이 끼친다.