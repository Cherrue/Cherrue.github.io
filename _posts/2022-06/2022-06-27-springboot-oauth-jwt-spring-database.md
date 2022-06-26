---
layout: single
title: \[Springboot\] OAuth2 와 JWT (3) database 연결
date: 2022-06-27 07:59:31.504803 +0900
categories: springboot authentication
toc: true
toc_sticky: true
toc_label: Contents
---

[이전 글 - SNS 연동 편](https://cherrue.github.io/springboot/authentication/springboot-oauth-jwt-spring-tutorials/) 에서 이어집니다.

# 구현

springboot를 이용해 OAuth2.0 과 JWT를 이용해 로그인을 구현합니다.

클라이언트는 별도 구성 없이 springboot에서 thymeleaf를 이용해 구현합니다

**환경**

| 환경 | 버전 |
| --- | --- |
| java | 11 |
| springboot | 2.7.0 |
| gradle | 7.4.1 |

## Step 2. 회원가입 (Database 연결)

### 1. 인메모리 데이터베이스 h2 연결하기

DB 스키마가 계속 변경될 수 있어 여기서는 h2로 진행합니다. 

**의존성 추가**

- build.gradle

```groovy
dependencies {
		...

    // DATABASE
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    runtimeOnly 'com.h2database:h2'

		...
}
```

**datasource 설정**

spring.datasource.url 을 지정하지 않으면 매 실행시마다 jdbc url이 랜덤 하게 바뀝니다. test로 고정하겠습니다.

- application.yml

```yaml
spring:
  ...

  h2:
    console:
      enabled: true
  datasource:
    driver-class-name: org.h2.Driver
    url: jdbc:h2:mem:test

	...
```

**h2-console 접근을 위한 security 설정**

h2-console 접근 편의성을 위한 보안 예외를 처리합시다.

http와 web configure이 모두 필요합니다. csrf 쪽도 설정해주어야 합니다.

- SecurityConfiguration.java

```java
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        // @formatter:off
        http
                .authorizeRequests(a -> a
                        .antMatchers("/", "/error", "/webjars/**", "/h2-console/**").permitAll()
                        .anyRequest().authenticated()
                )
                .exceptionHandling(e -> e
                        .authenticationEntryPoint(new HttpStatusEntryPoint(HttpStatus.UNAUTHORIZED))
                )
                .logout(l -> l
                        .logoutSuccessUrl("/").permitAll()
                )
                .csrf(c -> c
                        .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
                        .ignoringAntMatchers("/h2-console/**").disable()
                )
                .httpBasic(withDefaults())
                .oauth2Login();
        // @formatter:on
        return http.build();
    }

    @Bean
    public WebSecurityCustomizer webSecurityCustomizer() {
        return web -> web.ignoring().antMatchers("/h2-console/**");
    }

}
```

여기까지 잘 되었는지 테스트 : localhost:8080/h2-console 접속. 양식 입력 후 Test Connection, connect 정상 수행

- URL : jdbc:h2:mem:test (application.yml > spring.datasource.url 에 작성한 내용)
- User Name : sa (default)
- Password : 값 없음 (default)

![10_h2.png](/assets/images/2022-06/27/10_h2.png)

![11_h2_login_success.png](/assets/images/2022-06/27/11_h2_login_success.png)

### 2. OAuthUserService 추가

**OAuthUserService 등록**

OAuth 로그인에 성공했을 때 동작할 서비스를 등록하겠습니다.

- `oauth/CustomOAuth2UserService.java`

기존과 같게 동작하도록 DefaultOAuth2UserService 를 사용해줍니다. 

기본 동작을 DefaultOAuth2UserService가 대신 해주어 보통 변수명을 delegate(대리자) 라고 짓습니다.

```java
@Service
public class CustomOAuth2UserService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {
    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        OAuth2UserService<OAuth2UserRequest, OAuth2User> delegate = new DefaultOAuth2UserService();
        OAuth2User oAuth2User = delegate.loadUser(userRequest);
        return oAuth2User;
    }
}
```

작성한 서비스를 security에 붙여줍시다.

- `config/SecurityConfiguration.java`

```java
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfiguration {
    private final CustomOAuth2UserService customOAuth2UserService;
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        // @formatter:off
        http
                ...
                .oauth2Login(o -> o
                        .userInfoEndpoint()
                        .userService(customOAuth2UserService));
        // @formatter:on
        return http.build();
    }
```

여기까지 잘 되었는지 테스트 : 로그인, 로그아웃, h2-console이 이전과 똑같이 잘 동작합니다.

**extract attributes**

DefautlOAuth2UserService.loadUser 의 github 결과를 찍어보면 아래와 같습니다.

```java
Granted Authorities: [[ROLE_USER, SCOPE_read:user]], 
User Attributes: [
{login=Cherrue, 
avatar_url=https://avatars.githubusercontent.com/u/22141516?v=4, 
name=TaeHyeong Lee, 
[email=th885172@gmail.com](mailto:email=th885172@gmail.com),
...
}]
```

Granted Authorites 는 우리 서비스의 권한이 아닌, 연결시킨 서비스에서의 권한입니다.

attributes는 Map 형태인데, 제공 서비스마다 필드 명이 다릅니다.

서비스마다 적절하게 데이터를 추출해주는 객체를 작성합니다.

- `oauth/UserDto.java`

객체 사이에서 데이터를 들고 다닐 객체입니다. 관리할 데이터 중 최소한의 데이터만 갖습니다.

```java
@Getter
public class UserDto {
		private final String registrationId;
    private final String oAuthId;
    private final String email;
    private final String name;
    private final String image;

    @Builder
    public UserDto(String registrationId, String oAuthId, String email, String name, String image) {
        this.registrationId = registrationId;
        this.oAuthId = oAuthId;
        this.email = email;
        this.name = name;
        this.image = image;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("registrationId", registrationId);
        map.put("id", oAuthId);
        map.put("name", name);
        map.put("email", email);
        map.put("image", image);
        return map;
    }
}
```

- `oauth/OAuthAttributes.java`

서비스(registrationId)에 따라 적절하게 데이터를 추출하는 enum 입니다.

```java
public enum OAuthAttributes {
    GITHUB("github", (attributes) -> UserDto.builder()
            .registrationId((String) attributes.get("registrationId"))
            .oAuthId(String.valueOf(attributes.get("id"))) // Integer
            .name((String) attributes.get("name"))
            .email((String) attributes.get("email"))
            .image((String) attributes.get("avatar_url"))
            .build());

		private final String registrationId;
    private final Function<Map<String, Object>, UserDto> of;

    OAuthAttributes(String registrationId, Function<Map<String, Object>, UserDto> of) {
        this.registrationId = registrationId;
        this.of = of;
    }

    public static UserDto extract(String registrationId, Map<String, Object> attributes) {
        return Arrays.stream(values()) // values 는 enum 의 values 이다. 이 enum 개체를 반복문 돌린다고 보면 된다.
                .filter(provider -> registrationId.equals(provider.registrationId)) // 이 enum 객체가 반복문을 돌고 있으니 provider 는 OAuthAttributes 이다.
                .findFirst() // 일치하는 registrationId를 찾는다.
                .orElseThrow(IllegalArgumentException::new) // 없으면 에러를 발생시킨다.
                .of.apply(attributes); // 이 of 가 UserDto.builder 로 값을 매핑해주는 부분이다.
    }
}
```

- `oauth/entity/Role.java`

내 서비스의 권한을 의미합니다. 현재는 일반 user만 있습니다.

spring security의 규칙 상 항상 “ROLE_” prefix 가 붙어야 합니다.

```java
@Getter
@RequiredArgsConstructor
public enum Role {
    ROLE_USER("ROLE_USER");
    private final String key;
}
```

- `oauth/CustomOAuth2UserService.java`

데이터 추출을 서비스에 추가

```java
@Service
@Slf4j
public class CustomOAuth2UserService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {
    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        // 기본 동작
        OAuth2UserService<OAuth2UserRequest, OAuth2User> delegate = new DefaultOAuth2UserService();
        OAuth2User oAuth2User = delegate.loadUser(userRequest);
        // 정보 제공 서비스의 id
        String registrationId = userRequest.getClientRegistration().getRegistrationId();
        // 제공 서비스 별 키 값으로 사용되는 attribute 의 이름
        String userNameAttributeName = userRequest.getClientRegistration().getProviderDetails().getUserInfoEndpoint().getUserNameAttributeName();
				// 수정할 수 있게 새로운 map 에 담음
        Map<String, Object> attributes = new HashMap<>(oAuth2User.getAttributes());
        attributes.put("registrationId", registrationId); // 계속 필요한 정보라 추가

        // 회원 가입에 사용할 데이터 추출
        UserDto userDto = OAuthAttributes.extract(registrationId, attributes);
        Map<String, Object> memberAttributes = userDto.toMap();

        log.info(userDto.toString());
        log.info(memberAttributes.toString());

        // 우리 서비스에 맞는 권한 부여
        return new DefaultOAuth2User(
                Collections.singleton(new SimpleGrantedAuthority(Role.ROLE_USER.getKey())),
                memberAttributes, // 필요한 데이터만 전달
                userNameAttributeName
        );
    }
}
```

여기까지 잘 되었는지 테스트 : 로그인 시 콘솔에 로그가 정상적으로 남는다.

```java
2022-06-06 20:50:26.729  INFO 9980 --- [nio-8080-exec-8] m.c.p.oauth.CustomOAuth2UserService      : {image=https://avatars.githubusercontent.com/u/22141516?v=4, registrationId=github, name=TaeHyeong Lee, id=22141516, email=th885172@gmail.com}
2022-06-06 20:50:28.233  INFO 9980 --- [nio-8080-exec-1] m.c.p.PrototypeOauthJwtApplication       : Name: [22141516], Granted Authorities: [[ROLE_USER]], User Attributes: [{image=https://avatars.githubusercontent.com/u/22141516?v=4, registrationId=github, name=TaeHyeong Lee, id=22141516, email=th885172@gmail.com}]
```

### 3. 사용자 정보 DB에 저장

**entity, repository 작성**

- `/src/main/resources/application.yml`

open-in-view : view가 그려질 때 까지 트랜잭션 유지

ddl-auto : DDL 발생 시 쿼리 실행 여부. update로 하면 entity 구조를 보고 알아서 업데이트 칩니다. 초기 개발 중에는 update, 운영 시에는 꺼버립니다.

show-sql : 실행된 쿼리문들을 로그에 찍습니다.

```yaml
spring:
  jpa:
    open-in-view: true
    hibernate:
      ddl-auto: update
    show-sql: true
	...
```

- `oauth/entity/Member.java`

```java
@Getter
@NoArgsConstructor
@Entity
public class Member {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    private String registrationId;

    private String oAuthId;

    private String email;

    private String name;

    private String image;

    @Enumerated(EnumType.STRING)
    private Role role;

    @Builder
    public Member(String registrationId, String oAuthId, String email, String name, String image, Role role) {
        this.registrationId = registrationId;
        this.oAuthId = oAuthId;
        this.email = email;
        this.name = name;
        this.image = image;
        this.role = role;
    }

    public Member update(String name, String email, String image) {
        this.name = name;
        this.email = email;
        this.image = image;

        return this;
    }
}
```

- `oauth/repository/MemberRepository.java`

원래는 @Query 어노테이션 없이 JPA 가 알아서 쿼리를 만들어줘야 하지만,

o_auth_id 와 같이 한 글자로 시작하는 경우 jpa 가 알아서 찾아가지 못합니다.

Query 어노테이션을 붙여 구현해줍시다.

```java
@Repository
public interface MemberRepository extends JpaRepository<Member, Integer> {

    @Query(nativeQuery = true, value = "SELECT * FROM member m WHERE m.registration_id = ?1 AND m.o_auth_id = ?2")
    Optional<Member> findByRegistrationIdAndOAuthId(String registrationId, String oAuthId);
}
```

여기까지 잘 되었는지 테스트 : 실행 시 로그 확인

```java
Hibernate: create table member (id integer not null, email varchar(255), image varchar(255), name varchar(255), o_auth_id varchar(255), registration_id varchar(255), role varchar(255), primary key (id))
Hibernate: create sequence hibernate_sequence start with 1 increment by 1
```

- `oauth/dto/UserDto.java`

Dto를 entity로 바꾸어주는 함수를 작성합니다.

모든 사용자는 기본적으로 user 권한으로 시작하기 때문에, 유저 권한을 기본으로 넣어줍니다.

```java
@Getter
public class UserDto {
		...

		public Member toMember() {
        return Member.builder()
                .registrationId(registrationId)
                .oAuthId(oAuthId)
                .name(name)
                .email(email)
                .image(image)
                .role(Role.ROLE_USER)
                .build();
    }
}
```

- `oauth/CustomOAuth2UserService`

```java
@RequiredArgsConstructor
@Service
@Slf4j
public class CustomOAuth2UserService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {
    private final MemberRepository memberRepository;

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        ...
				// 우리 DB에 저장 == 회원가입
        Member member = saveOrUpdate(userDto);

        // 우리 서비스에 맞는 권한 부여
        return new DefaultOAuth2User(
                Collections.singleton(new SimpleGrantedAuthority(Role.ROLE_USER.getKey())),
                memberAttributes, // 필요한 데이터만 전달
                userNameAttributeName
        );
    }

    private Member saveOrUpdate(UserDto userDto) {
				// OAuth 제공 서비스 측 데이터가 변경될 수 있기 때문에 name, email, picture 업데이트
				// registrationId, oAuthId 는 기본적으로 변경이 없는 데이터입니다.
        Member member = memberRepository.findByRegistrationIdAndOAuthId(userDto.getRegistrationId(), userDto.getOAuthId())
                .map(m -> m.update(userDto.getName(), userDto.getEmail(), userDto.getImage()))
                .orElse(userDto.toMember());
        return memberRepository.save(member);
    }
}
```

여기까지 잘 되었는지 테스트 : 로그인 정상 동작. 로그인 성공 후 h2-console에서 저장된 데이터 확인

![12_h2_select_data.png](/assets/images/2022-06/27/12_h2_select_data.png)
