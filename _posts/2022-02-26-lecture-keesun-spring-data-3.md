---

layout: single
title: \[강의요약\] 스프링부트 개념과 활용 - 스프링 데이터 (3/3)
date: 2022-02-24 23:28:00 +0900
categories: lecture_summary springboot springboot_getting_started
toc: true
toc_sticky: true
toc_label: Contents

---

개인적인 학습을 위한 [Inflearn - 스프링부트 개념과 활용](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8/dashboard)(백기선) 강의 요약입니다.

개념과 원리 위주로 요약합니다.

[이전 글](https://cherrue.github.io/springboot/springboot_getting_started/study/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8-%EC%9B%90%EB%A6%AC/) 에서 이어집니다.

# 4부. 스프링 부트 활용 - 스프링 데이터

---

## 9. Redis

신규 프로젝트 생성 : springbootredis (spring-boot-starter만 추가)

pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>me.cherrue</groupId>
    <artifactId>springbootredis</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>

    <parent>
        <artifactId>spring-boot-starter-parent</artifactId>
        <groupId>org.springframework.boot</groupId>
        <version>2.2.0.RELEASE</version>
    </parent>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
    </dependencies>

</project>
```

**9-1. 의존성 추가**

```xml
		<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
```

**9-2. Redis 설치 (docker)**

```bash
# terminal
$ docker run -p 6379:6379 --name redis_boot -d redis
$ docker exec -i -t redis_boot redis-cli
127.0.0.1:6379> keys *
(empty array)
```

**9-3. Redis 사용하기**

9-3-1. StringRedisTemplate : 문자열 특화

```java
// RedisRunner.java
@Component
public class RedisRunner implements ApplicationRunner {

    @Autowired
    StringRedisTemplate redisTemplate;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        ValueOperations<String, String> values = redisTemplate.opsForValue(); // redis operations class
        values.set("cherrue", "chen"); // key, value
        values.set("springboot", "2.0");
        values.set("hello", "world");
    }
}
```

**결과**

```java
// docker redis cli console
127.0.0.1:6379> keys *
1) "springboot"
2) "hello"
3) "cherrue"

127.0.0.1:6379> get cherrue
"chen"
```

9-3-2. CrudRepository : db 사용하듯 Repository로 접근

```java
// account.Account.java
@RedisHash("accounts")
public class Account {
    @Id private String id;

    private String username;

    private String email;
}
```

```java
// account.AccountRepository.java
public interface AccountRepository extends CrudRepository<Account, String> {
}
```

```java
// RedisRunner.java
@Component
public class RedisRunner implements ApplicationRunner {

    @Autowired
    StringRedisTemplate redisTemplate;

    @Autowired
    AccountRepository accountRepository;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        ValueOperations<String, String> values = redisTemplate.opsForValue(); // redis operations class
        values.set("cherrue", "chen"); // key, value
        values.set("springboot", "2.0");
        values.set("hello", "world");

        Account account = new Account();
        account.setEmail("cherrue@email.com");
        account.setUsername("cherrue");

        accountRepository.save(account);

        Optional<Account> byId = accountRepository.findById(account.getId());

        System.out.println(byId.get().getUsername());
        System.out.println(byId.get().getEmail());
    }
}
```

**결과**

뒤에 랜덤 값이 붙은 키가 생기는데 이건 get() 으로 읽을 수 없다

```java
127.0.0.1:6379> keys *
1) "springboot"
2) "hello"
3) "cherrue"
4) "accounts:5ef82c90-976a-4be3-b9e1-94270bb70c5f"
5) "accounts"

127.0.0.1:6379> get accounts:5ef82c90-976a-4be3-b9e1-94270bb70c5f
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```

hget(hash get) 으로 호출, 뒤에 필드명을 적어주어야 한다.

모두 가져오고 싶다면 hgetall 명령어를 사용한다.

```java

127.0.0.1:6379> hget accounts:5ef82c90-976a-4be3-b9e1-94270bb70c5f email
"cherrue@email.com"

127.0.0.1:6379> hgetall accounts:5ef82c90-976a-4be3-b9e1-94270bb70c5f email
(error) ERR wrong number of arguments for 'hgetall' command

127.0.0.1:6379> hgetall accounts:5ef82c90-976a-4be3-b9e1-94270bb70c5f
1) "_class"
2) "me.cherrue.springbootredis.account.Account"
3) "id"
4) "5ef82c90-976a-4be3-b9e1-94270bb70c5f"
5) "username"
6) "cherrue"
7) "email"
8) "cherrue@email.com"
```

**9-4. Redis 커스터마이즈**

application.properties에서 spring.redis.* 변경

- spring.redis.port=6379
- spring.redis.url={{ remote ip }}

---

## 10. MongoDB

프로젝트 생성 : springbootmongo (starter 의존성만 추가)

MongoDB : json 기반의 도큐먼트 단위로 동작하여 스키마가 없다.

**10-1. 의존성 추가**

```xml
		<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>
```

10-2. MongoDB 설치(DB)

참고) 도커 run 스크립트 알아내기 : dockerhub 사이트에서 검색 ([https://hub.docker.com/_/mongo](https://hub.docker.com/_/mongo))

```bash
$ docker run -p 27017:27017 --name mongo_boot -d mongo

$ docker exec -i -t mongo_boot bash                                                                                             37s 00:01:31
root@15df444c4b3d:/# mongo
MongoDB shell version v5.0.6

> db
test

> use test
switched to db test

> db.accounts.find({})
>
```

10-3. 사용하기

엔티티에 @Document(collection={{ 원하는 컬렉션 명 }}) 사용

- collection = RDB의 테이블명과 유사 개념

자동설정

10-3-1. MongoTemplate

```java
// account.Account.java
@Document(collection = "accounts")
public class Account {
    @Id
    private String id;

    private String username;

    private String email;

... (getter setter)
}
```

```java
// SpringbootmongoApplication
@SpringBootApplication
public class SpringbootmongoApplication {

    @Autowired
    MongoTemplate mongoTemplate;

    public static void main(String[] args) {
        SpringApplication.run(SpringbootmongoApplication.class, args);
    }

    @Bean
    public ApplicationRunner applicationRunner() {
        return args -> {
            Account account = new Account();
            account.setEmail("aaa@bbb");
            account.setUsername("aaa");

            mongoTemplate.insert(account);

            System.out.println("finished");
        };
    }
}
```

**결과**

```java
> db.accounts.find({})
{ "_id" : ObjectId("62179fe4bbfb0c61921005b7"), "username" : "aaa", "email" : "aaa@bbb", "_class" : "me.cherrue.springbootmongo.account.Account" }
```

10-3-2. MongoRepository

```java
// account.AccountRepository.java
public interface AccountRepository extends MongoRepository<Account, String> {
}
```

```java
// SpringbootmongoApplication
@SpringBootApplication
public class SpringbootmongoApplication {

    @Autowired
    MongoTemplate mongoTemplate;

    @Autowired
    AccountRepository accountRepository;

    public static void main(String[] args) {
        SpringApplication.run(SpringbootmongoApplication.class, args);
    }

    @Bean
    public ApplicationRunner applicationRunner() {
        return args -> {
            Account account = new Account();
            account.setEmail("cherrue@ccc");
            account.setUsername("ddd");

//            mongoTemplate.insert(account);
            accountRepository.insert(account);

            System.out.println("finished");

        };
    }
}
```

**결과**

```java
> db.accounts.find({})
{ "_id" : ObjectId("62179fe4bbfb0c61921005b7"), "username" : "aaa", "email" : "aaa@bbb", "_class" : "me.cherrue.springbootmongo.account.Account" }
{ "_id" : ObjectId("6217a0abdab0e12e46f3bc81"), "username" : "ddd", "email" : "cherrue@ccc", "_class" : "me.cherrue.springbootmongo.account.Account" }
```

**10-4. 내장형 mongoDB와 테스트**

운영용 mongo db 를 사용하면 번거롭다. 내장 mongodb를 사용해 테스트하자

10-4-1. 의존성 추가

```xml
		<dependency>
            <groupId>de.flapdoodle.embed</groupId>
            <artifactId>de.flapdoodle.embed.mongo</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
```

10-4-2. 슬라이싱 테스트 구현

내장 MongoDB를 사용하면 슬라이싱 테스트가 가능

- @DataMongoTest : Mongo 관련 Repository만 생성

```java
// account.AccountRepository.java
public interface AccountRepository extends MongoRepository<Account, String> {
    public Optional<Account> findByEmail(String email);
}
```

```java
@RunWith(SpringRunner.class)
@DataMongoTest
public class AccountRepositoryTest {
    @Autowired
    AccountRepository accountRepository;

    @Test
    public void findByEmail() {
        Account account = new Account();
        account.setUsername("cherrue");
        account.setEmail("cherrue@email.com");

        accountRepository.save(account);

        Optional<Account> byId = accountRepository.findById(account.getId());
        assertThat(byId).isNotEmpty();

        Optional<Account> byEmail = accountRepository.findByEmail(account.getEmail());
        assertThat(byEmail).isNotEmpty();
        assertThat(byEmail.get().getUsername()).isEqualTo("cherrue");
    }
}
```

---

## 11. Neo4j

Neo4j : 노드 간 연관 관계를 표현할 때 다양한 기능과 속도가 빠른 그래프 데이터베이스

신규 프로젝트 생성 : springbootneo4j (starter 의존성만)

**11-1. 의존성 추가**

neo4j 의존성 버전이 올라가면서 template 빈이 사라짐. SessionFactory나 Repository를 사용.

```xml
		<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-neo4j</artifactId>
        </dependency>
```

**11-2. Neo4j 설치**

```bash
$ docker run -p 7474:7474 -p 7687:7687 -d --name neo4j_boot neo4j
```

[http://localhost:7474/browser/](http://localhost:7474/browser/) 에 접속하면 데이터를 웹브라우저에서 볼 수 있다.

- 기본 로그인 계정은 id = neo4j / password = neo4j
- 서버에 연결 시 초기 비번을 변경하라고 시킨다. 1111로 바꾸었다.

**11-3. 사용하기**

바꾼 비번 적용

```bash
# application.properties
spring.data.neo4j.password=1111
spring.data.neo4j.username=neo4j
```

엔티티에 @NodeEntity 사용

```java
@NodeEntity
public class Account {
    @Id
    @GeneratedValue
    private Long id;

    private String username;

    private String email;
... (getter, setter)
}
```

Runner 작성 (Session Factory 사용) 

```java
@Component
public class Neo4jRunner implements ApplicationRunner {
    @Autowired
    SessionFactory sessionFactory;

    @Override
    public void run(ApplicationArguments args) throws Exception {

        Account account = new Account();
        account.setEmail("cherrue@email.com");
        account.setUsername("cherrue");

        Session session = sessionFactory.openSession();
        session.save(account);
        sessionFactory.close();

        System.out.println("finished");
    }
}
```

인데, neo4j 버전이 수업과 달라서인지 접속이 안 된다. 

old 버전 syntax라는 것 같다.

```java
Caused by: org.neo4j.ogm.exception.CypherException: Cypher execution failed with code 'Neo.ClientError.Statement.SyntaxError': The old parameter syntax `{param}` is no longer supported. Please use `$param` instead (line 1, column 8 (offset: 7))
"UNWIND {rows} as row CREATE (n:`Account`) SET n=row.props RETURN row.nodeRef as ref, ID(n) as id, {type} as type"
        ^.
```

난 neo4j에는 관심이 없어서 강의 내용만 듣고 넘어간다.

---

## 12. 스프링 데이터 정리

12-1. SQL database

spring jdbc → JdbcTemplate으로 쉽게 사용

DataSource 객체의 Connection

12-2. embedded database : h2. 설정없이 바로 사용 가능 + dev-tools h2 console

12-3. DBCP : Hikari db connection pool

12-4. RDB : mysql, mariaDB

12-5. spring data jpa 사용 방법 : Entity와 Repository

12-6. db 초기화

spring.jpa.hibernate.ddl-auto = create-drop, update, validate 등

spring.data.generate-ddl = true

12-7. NoSQL : redis, mongo, neo4j

- template 또는 Repository로 연동하여 사용
- 커스텀은 application.properties에서 작성하거나, 직접 Bean을 등록