---
layout: single
title: \[Springboot\] OAuth2 와 JWT (4) 세션 유지(JWT)
date: 2022-06-27 08:47:31.504803 +0900
categories: springboot authentication
toc: true
toc_sticky: true
toc_label: Contents
---

[이전 글 - db 연동 편](https://cherrue.github.io/springboot/authentication/springboot-oauth-jwt-database/) 에서 이어집니다.

# 구현

springboot를 이용해 OAuth2.0 과 JWT를 이용해 로그인을 구현합니다.

클라이언트는 별도 구성 없이 springboot에서 thymeleaf를 이용해 구현합니다

**환경**

| 환경 | 버전 |
| --- | --- |
| java | 11 |
| springboot | 2.7.0 |
| gradle | 7.4.1 |

## Step 3. 로그인 세션 유지 (JWT)

### 1. Token 생성 서비스 구현

**의존성 추가**

- `build.gradle`

```groovy
dependencies {
    // BE
    implementation 'org.springframework.boot:spring-boot-starter-oauth2-client'
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'io.jsonwebtoken:jjwt:0.9.1'
    implementation 'javax.xml.bind:jaxb-api' // DatatypeConverter 사용을 위해 추가
...
}
```

**JWT 서명을 위한 개인키를 설정값에 추가**

- /src/main/resources/private.yml

private.jwt.secret 에 원하는 개인 키 값을 작성합니다. 유출되면 인증이 탈탈 털리는 값입니다.

```yaml
private:
  key:
    oauth:
      github:
        clientId: 
        clientSecret: 
    jwt:
      secret: 
```

**Token 객체 추가**

- `jwt/Token.java`

```groovy
@Getter
public class Token {
    private final String token;

    public Token(String token) {
        this.token = token;
    }
}
```

**JwtSubject 객체 추가** (이건 필수가 아니다)

- `jwt/JwtSubject.java`

필수적인 요소만 넣으려고 했는데, token 발급 데이터를 oAuthId 로 잡은 이상 registrationId 가 같이 가야한다.

Claims는 subject를 하나만 가져 registrationId 와 oAuthId를 뭉쳐서 처리해주는 객체이다.

이걸 안 쓰고 싶다면 tokenService에서 oAuthId만 쓰거나 email 같은 걸 쓰면 된다. unique 하지 않을 수 있어서 subject를 쓰는 것이 더 안전하다.

```java
@Getter
@RequiredArgsConstructor
public class JwtSubject {
    private final String registrationId;
    private final String oAuthId;

    public JwtSubject(String jwtSubjectString) {
        String[] strings = jwtSubjectString.split("\t");
        if(strings.length != 2) {
            throw new IllegalArgumentException("잘못된 형식의 subject 입니다. subject : " + jwtSubjectString);
        }
        registrationId = strings[0];
        oAuthId = strings[1];
    }

    public String toString() {
        return registrationId + "\t" + oAuthId;
    }
}
```

**Token 발급 서비스 추가**

- `jwt/TokenService.java`

verifyToken()의 JWS와 claims가 기억이 안 난다면 JWT의 개념을 다시 보자.

대충 claims 는 내용물, JWS는 서명이 붙은 json 이라고 보면 된다.

```java
@Getter
@Slf4j
@Service
public class TokenService {
    @Value("${private.key.jwt.secret}")
    private String secretKey; // 토큰 서명용 개인키. 그대로 쓰지 않고 Base64 인코딩하여 사용한다.
    private long tokenPeriod = 1000L * 60L * 10L; // 토큰 만료 시간

    @PostConstruct
    protected void init() {
        if (secretKey == null) { // Bean 이기 때문에 개인키 주입이 제대로 안 되면 최초 실행 중에 죽는다.
            throw new RuntimeException("Fail to inject configuration value");
        }
        secretKey = Base64.getEncoder().encodeToString(secretKey.getBytes());
    }

    /**
     * 토큰 생성
     * @param registrationId oauth 를 이용한 서비스 id. 복합키의 구성요소
     * @param oAuthId oauth 로그인 시 제공받은 키 값. registrationId와 조합하면 키 값이 된다.
     * @param role 사용자 권한. 우리는 일반 사용자만 있다.
     * @return 생성된 토큰
     */
    public Token generateToken(String registrationId, String oAuthId, Role role) {
        JwtSubject jwtSubject = new JwtSubject(registrationId, oAuthId);
        Claims claims = Jwts.claims().setSubject(jwtSubject.toString());
        claims.put("role", role.getKey());

        Date now = new Date();
        return new Token(
                Jwts.builder()
                        .setClaims(claims)
                        .setIssuedAt(now)
                        .setExpiration(new Date(now.getTime() + tokenPeriod))
                        .signWith(SignatureAlgorithm.HS256, secretKey)
                        .compact());
    }

    /**
     * 토큰이 유효한지 확인. 만료기한 뿐만 아니라, 토큰의 포맷, 사인, 토큰 내용 등을 확인한다.
     * @param token JWT 를 담은 문자열
     * @return 유효 여부
     */
    public boolean verifyToken(String token) {
        try {
            Jws<Claims> claimsJws = Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token);
            return claimsJws.getBody().getExpiration().after(new Date());
        } catch (Exception e) {
            log.info("만료되었거나 올바르지 않은 토큰입니다" + token);
            return false;
        }
    }

		/**
     * token 에서 claim 의 subject를 가져온다.
     * 우리의 subject 는 registrationId + \t + oAuthId 의 구조를 갖는다.
     * @param token 우리가 만든 jwt token
     * @return token 에서 추출한 subject
     */
    public String getClaimsSubject(String token) {
        return Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token).getBody().getSubject();
    }
}
```

여기까지 잘 되었는지 테스트 : 테스트 코드 작성 - 아래의 테스트가 모두 성공해야 한다.

개인키 주입으로 인해 슬라이스 테스트는 안 된다.

- `/src/test/java/me/cherrue/prototypeoauthjwt/jwt/TokenServiceTest.java`

경로가 test를 제외하고는 TokenService.java 와 같아야한다. SpringBootTest의 규칙이다.

verifyToken 테스트 시 java reflection 을 사용하기보다 test용 application.yml 을 만드는 것이 어떤가 생각만 해보았다.

```java
@SpringBootTest
class TokenServiceTest {
    @Autowired
    TokenService tokenService;

    @Test
    @DisplayName("private.yml 의 secret key 가 정상적으로 주입되었는지 확인")
    public void checkConfigurationDI() {
        assertThat(tokenService.getSecretKey()).isNotNull();
    }

    @Test
    @DisplayName("jwt 토큰 생성 확인")
    /*
     * JWT 는 .을 기준으로 세 부분을 나뉘고, 각 부분은 BASE64 인코딩이 되어있다.
     * 첫 부분은 암호화 형식을, 두 번째는 claims 을, 세 번째는 서명을 담는다.
     */
    public void generateToken() {
        String registrationId = "github";
        String oAuthId = "1234";
        String algorithm = "HS256";
        Token token = tokenService.generateToken(registrationId, oAuthId, Role.ROLE_USER);
        System.out.println(token.getToken());
        String[] strings = token.getToken().split("\\.");

        assertThat(strings.length).isEqualTo(3);

        String header = new String(Base64.getDecoder().decode(strings[0]));
        String payload = new String(Base64.getDecoder().decode(strings[1]));

        assertThat(header).contains(algorithm);
        assertThat(payload).contains(registrationId).contains(oAuthId).contains(Role.ROLE_USER.getKey());
    }

    @Test
    @DisplayName("만료된 토큰에 대한 verifyToken 함수 동작 확인")
    /*
     * java reflection 을 사용하 private 한 tokenPeriod 를 잠시 1초로 바꾸었다.
     */
    public void verifyToken() throws InterruptedException {
        Object tokenPeriod = ReflectionTestUtils.getField(tokenService, "tokenPeriod");
        ReflectionTestUtils.setField(tokenService, "tokenPeriod", 1000L);

        Token token = tokenService.generateToken("registrationId", "oAuthId", Role.ROLE_USER);
        Thread.sleep(1000L);

        boolean isExpired = tokenService.verifyToken(token.getToken());

        assertThat(isExpired).isFalse();

        ReflectionTestUtils.setField(tokenService, "tokenPeriod", tokenPeriod);
    }
}
```

### 2. 토큰 발급 handler 구현

- `oauth/OAuthSuccessHandler.java`

oauth 로그인 성공 시 동작하는 핸들러이다.

토큰을 발급해 cookie 에 담아주자.

그 외 기능은 기존과 같게 동작하도록 `SavedRequestAwareAuthenticationSuccessHandler` 를 상속받는다.

```java
@Slf4j
@Component
@RequiredArgsConstructor
public class OAuthSuccessHandler implements SavedRequestAwareAuthenticationSuccessHandler {
    private final TokenService tokenService;
    private final ObjectMapper objectMapper;

    @Override
    public void onAuthenticationSuccess(HttpServletRequest request, HttpServletResponse response, Authentication authentication) throws IOException {
        OAuth2User principal = (OAuth2User) authentication.getPrincipal();
        Map<String, Object> attributes = principal.getAttributes();

        // CustomOAuth2UserService 에서 UserDto.toMap 해서 넘겼기 때문에 키 값이 고정이다.
        UserDto userDto = UserDto.builder()
                .registrationId((String) attributes.get("registrationId"))
                .oAuthId(String.valueOf(attributes.get("id"))) // Integer
                .name((String) attributes.get("name"))
                .email((String) attributes.get("email"))
                .image((String) attributes.get("image"))
                .build();

        Token token = tokenService.generateToken(userDto.getRegistrationId(), userDto.getOAuthId(), Role.ROLE_USER);
        log.info(token.getToken());

				Cookie jwtCookie = new Cookie("jwt", token.getToken());
        jwtCookie.setMaxAge(-1); // 음수이면 브라우저를 닫으면 날아간다.
        jwtCookie.setPath("/");
        response.addCookie(jwtCookie);
        
        // 기존의 redirect 수행
        super.onAuthenticationSuccess(request, response, authentication);
}
```

구현한 핸들러를 등록한다.

- `config/SecurityConfiguration.java`

```java
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfiguration {
    private final CustomOAuth2UserService customOAuth2UserService;
    private final OAuthSuccessHandler oAuthSuccessHandler;
		@Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        // @formatter:off
        http
								...
								.oauth2Login(o -> o
                        .successHandler(oAuthSuccessHandler)
                        .userInfoEndpoint()
                        .userService(customOAuth2UserService));
        // @formatter:on
        return http.build();
		}
		...
}
```

여기까지 잘 되었는지 테스트 : 로그인 시 쿠키에 jwt가 저장된다. 콘솔 로그와 비교하여 같은지 확인한다.

로그인 후 콘솔 : 개발자 도구(F12) > Application > Cookies > [localhost:8080](http://localhost:8080) > jwt

![13_browser_console_jwt.png](/assets/images/2022-06/27/13_browser_console_jwt.png)

콘솔 로그

![14_server_console_jwt.png](/assets/images/2022-06/27/14_server_console_jwt.png)

### 3. 토큰 인증 필터 구현

**jwt 인증 필터**

- `jwt/JwtFilter.java`

쿠키에 담긴 jwt 값을 가져와 검증하고, 가입한 사용자인지 검사한 후 인증해준다.

JwtFilter를 지나가면 UsernamePassword를 패스하도록 UsernamePasswordAuthenticationToken를 설정해준다.

```java
@RequiredArgsConstructor
public class JwtFilter extends GenericFilterBean {
    private final TokenService tokenService;
    private final MemberRepository memberRepository;

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        String token = null;

        Cookie[] cookies = ((HttpServletRequest) request).getCookies();
        if (cookies != null) {
            // jwt 라는 이름으로 담긴 쿠키를 찾는다.
            token = Arrays.stream(cookies).filter(c -> c.getName().equals("jwt")).findFirst().map(Cookie::getValue).orElse(null);
        }

        if (token != null && tokenService.verifyToken(token)) {
            JwtSubject jwtSubject = new JwtSubject(tokenService.getClaimsSubject(token));
            // 회원가입이 되어있는 사용자인 경우에만 인증
            memberRepository.findByRegistrationIdAndOAuthId(jwtSubject.getRegistrationId(), jwtSubject.getOAuthId())
                    .ifPresent(m -> {
                        Authentication authentication = new UsernamePasswordAuthenticationToken(m, "",
                                List.of(new SimpleGrantedAuthority(m.getRole().getKey())));
                        SecurityContextHolder.getContext().setAuthentication(authentication);
                    });
        }

        chain.doFilter(request, response);
    }
}
```

만든 필터를 등록하자

- `config/SecurityConfiguration.java`

session이 필요가 없으므로 STATELESS 하게 변경한다.

JwtFilter 를 UsernamePasswordAuthenticationFilter 앞에 붙인다.

```java
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfiguration {
    private final CustomOAuth2UserService customOAuth2UserService;
    private final OAuthSuccessHandler oAuthSuccessHandler;
    private final TokenService tokenService;
    private final MemberRepository memberRepository;
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        // @formatter:off
        http
					...
								.sessionManagement(s -> s
                        .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                )
					...
				// @formatter:on

        http.addFilterBefore(new JwtFilter(tokenService, memberRepository), UsernamePasswordAuthenticationFilter.class);

        return http.build();
		}
		...
}
```

**user endpoint 수정**

이제 OAuthUser 가 아니라 Member 를 사용하기 때문에 controller를 수정해야 한다.

- `PrototypeOauthJwtApplication.java`

@AuthenticationPrincipal 의 자료형이 바뀌었다.

```java
@RestController
@SpringBootApplication
public class PrototypeOauthJwtApplication {

    @GetMapping("/user")
    public Map<String, Object> user(@AuthenticationPrincipal Member principal) {
        return Collections.singletonMap("name", principal.getName());
    }

    public static void main(String[] args) {
        SpringApplication.run(PrototypeOauthJwtApplication.class, args);
    }

}
```

여기까지 잘 되었는지 테스트 : 로그아웃을 제외한 모든 기능이 정상 동작한다.

- JWT를 쓰면 stateless 한 것이 목표이기 때문에 로그아웃 구현할 수 없습니다. 억지로 구현한다면 jwt를 사용하는 목적과 많이 벗어납니다.
- 로그인, 개발자 도구의 쿠키, 로그인 시 이름 출력이 모두 정상적으로 동작해야 합니다.
