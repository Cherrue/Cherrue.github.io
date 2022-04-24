---
layout: single
title: \[강의요약\] 스프링부트 개념과 활용 - 스프링 데이터 (2/3)
date: 2022-02-23 12:53:00 +0900
categories: lecture_summary springboot springboot_getting_started
toc: true
toc_sticky: true
toc_label: Contents
show_in_home: false
---

개인적인 학습을 위한 [Inflearn - 스프링부트 개념과 활용](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8/dashboard)(백기선) 강의 요약입니다.

개념과 원리 위주로 요약합니다.

[이전 글](https://cherrue.github.io/lecture_summary/springboot/springboot_getting_started/lecture-keesun-spring-data/) 에서 이어집니다.

# 4부. 스프링 부트 활용 - 스프링 데이터

---

## 5. 스프링 데이터 JPA 소개

프로젝트 생성 : springbootjpa (web), db는 postgres 사용

**5-1. ORM : Object-Relational Mapping**

> ORM : 객체와 릴레이션을 매핑해주는 프레임워크
> 

ORM이 해결해주는 문제(불일치)들

- 제한된 크기 : DB(릴레이션)의 크기가 더 제한적
- 상속 : DB는 상속구조가 없음
- 객체 비교 : DB는 키를 비교, 객체는 구현하기에 따라 다르지만 해쉬 등을 비교

**5-2. JPA : ORM을 위한 자바 EE 표준**

spring-data-jpa : ORM을 쉽게 사용하기 위한 hibernate로 구현한 JPA 구현체

추상화 단계 : SDJ(spring-data-jpa) > Hibernate > JDBC > Datasource

SDJ의 자동설정

- Repository 빈 생성
- 쿼리 메소드 자동 구현
- @EnableJpaRepository 설정

## 6. 스프링 데이터 JPA 연동

**6-1. 의존성 추가**

```xml
<dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

**6-2. entity와 repository 추가**

```java
// account.Account.java
@Entity
public class Account {
    @Id
    @GeneratedValue
    private Long id;

    private String username;
    private String password;
// getter setter 추가
// equals hashCode 추가
}
```

```java
// account.AccountRepository.java
public interface AccountRepository extends JpaRepository<Account, Long> {
}
```

**6-3. 슬라이싱 테스트 : Repository와 관련된 빈들만 포함해서 테스트**

- @DataJpaTest 사용
- DataSource, JdbcTemplate, Repository 주입
- 슬라이싱 테스트를 할 때는 항상 인메모리 데이터베이스가 필요 → h2 의존성 test scope 주입

```xml
				<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
	      <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>test</scope>
		    </dependency>
```

```java
@RunWith(SpringRunner.class)
@DataJpaTest
public class AccountRepositoryTests {
    @Autowired
    DataSource dataSource;
    @Autowired
    JdbcTemplate jdbcTemplate;
    @Autowired
    AccountRepository accountRepository;

    @Test
    public void di() {
        // DI test
    }
}
```

**6-4. postgresql 연결**

docker로 postgresql 실행 : 방법은 [이전 글](https://cherrue.github.io/lecture_summary/springboot/springboot_getting_started/lecture-keesun-spring-data/#4-postgressql)

의존성 추가

```xml
				<dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
        </dependency>
```

연결 설정

```java
spring.datasource.url=jdbc:postgresql://localhost:5432/springboot
spring.datasource.username=cherrue
spring.datasource.password=pass
```

테스트 작성

```java
@RunWith(SpringRunner.class)
@DataJpaTest
public class AccountRepositoryTests {
    @Autowired
    DataSource dataSource;
    @Autowired
    JdbcTemplate jdbcTemplate;
    @Autowired
    AccountRepository accountRepository;

    @Test
    public void di() {
        // DI test
        try (Connection connection = dataSource.getConnection()){
            DatabaseMetaData metaData = connection.getMetaData();
            System.out.println(metaData.getURL());
            System.out.println(metaData.getDriverName());
            System.out.println(metaData.getUserName());
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

**결과 - 1 어플리케이션 실행**

```java
2022-02-23 14:12:45.091  INFO 2011 --- [           main] m.c.s.SpringbootjpaApplication           : Started SpringbootjpaApplication in 3.704 seconds (JVM running for 4.074)
2022-02-23 14:15:13.186  WARN 2011 --- [l-1 housekeeper] com.zaxxer.hikari.pool.HikariPool        : HikariPool-1 - Retrograde clock change detected (housekeeper delta=29s819ms), soft-evicting connections from pool.
```

**결과 - 2 테스트 실행**

슬라이싱 테스트에서는 기본적으로 h2를 사용함

@SpringBootTest를 붙이면 postgres를 씀. 대신 테스트 수행이 느려진다.

```java
jdbc:h2:mem:a1ecbe8d-faaa-41c1-805a-1e56f8bc42ff
H2 JDBC Driver
SA
```

**6-5. repository 함수 자동 구현**

정해진 규칙의 함수를 repository interface에 선언하면 알아서 함수를 구현해준다.

쿼리를 지정하고 싶다면 @Query 어노테이션 사용

- JPQL 문법 또는 NativeQuery = true 옵션으로 SQL 사용

```java
public interface AccountRepository extends JpaRepository<Account, Long> {
		Optional<Account> findByUsername(String username);
}
```

```java
// AccountRepositoryTests
public void di() {
        Account account = new Account();
        account.setUsername("cherrue");
        account.setPassword("pass");

        Account newAccount =  accountRepository.save(account);

        assertThat(newAccount).isNotNull();

        Account existingAccount = accountRepository.findByUsername(newAccount.getUsername());
        assertThat(existingAccount).isNotNull();Optional<Account> existingAccount = accountRepository.findByUsername(newAccount.getUsername());
        assertThat(existingAccount).isNotEmpty();
        Optional<Account> nonExistingAccount = accountRepository.findByUsername("no_data");
        assertThat(nonExistingAccount).isEmpty();
    }
```

## 7. 데이터베이스 초기화

테스트 할 때 데이터베이스를 초기화하고 초기 데이터를 삽입하는 방법

**7-1. 데이터베이스 자동 초기화**

엔티티 정보를 바탕으로 자동으로 초기화 설정

ddl-auto : 어플리케이션 시작 시 스키마 생성 설정

- update : 변화가 있으면 업데이트. 데이터 이관은 해주지 않음
- validate : 현재 릴레이션이 엔티티와 매핑이 되는 지 검증만
- create-drop : 있는 테이블을 drop 후 재생성(데이터 초기화)

generate-ddl : 처음에 ddl 실행할 것인지 설정. default false

```java
# application.properties
spring.jpa.hibernate.ddl-auto=update
spring.jpa.generate-ddl=truespring.datasource.url=jdbc:postgresql://localhost:5432/springboot
spring.datasource.username=cherrue
spring.datasource.password=pass

spring.jpa.hibernate.ddl-auto=update
spring.jpa.generate-ddl=true
spring.jpa.show-sql=true
```

**결과**

```java
// console log
Hibernate: drop table if exists account cascade
Hibernate: drop sequence if exists hibernate_sequence
Hibernate: create sequence hibernate_sequence start 1 increment 1
Hibernate: create table account (id int8 not null, password varchar(255), username varchar(255), primary key (id))

// docker bash
$ psql springboot
psql (9.6.2)
Type "help" for help.

springboot=# \dt
         List of relations
 Schema |  Name   | Type  |  Owner
--------+---------+-------+---------
 public | account | table | cherrue
(1 row)
```

**7-2. 데이터베이스 커스텀 초기화**

schema.sql 작성

- resources/schema.sql 또는 schema-{platform}.sql 작성

```java
drop table if exists account cascade
drop sequence if exists hibernate_sequence
create sequence hibernate_sequence start 1 increment 1
create table account (id int8 not null, email varchar(255), password varchar(255), username varchar(255), primary key (id))
```

data.sql : 초기 데이터 삽입

## 8. 데이터베이스 마이그레이션

spring boot 와 연동되는 도구 : Flyway, Liquibase

마이그레이션 도구 : 스키마 변경, 데이터 변경에 대한 버전관리를 SQL 파일로 차곡차곡 관리하는 도구

8-1. 의존성 추가

```xml
				<dependency>
            <groupId>org.flywaydb</groupId>
            <artifactId>flyway-core</artifactId>
        </dependency>
```

8-2. 기본 파일 작성

1. resources/db/migration 생성. 하위에 벤더별 폴더 추가 가능(mysql, postgres 등)
2. migration 하위에 V1__init.sql(**underscore 2개!**) 작성 (schema.sql 파일 복사 후 해당 언어에 맞게 수정)
    
    ```sql
    drop table if exists account cascade;
    drop sequence if exists hibernate_sequence;
    create sequence hibernate_sequence start 1 increment 1;
    create table account (id int8 not null, email varchar(255), password varchar(255), username varchar(255), primary key (id));
    ```
    
3. schema.sql 삭제
4. application.properties 수정 (ddl 검증만 하도록 수정)
    
    ```sql
    spring.datasource.url=jdbc:postgresql://localhost:5432/springboot
    spring.datasource.username=cherrue
    spring.datasource.password=pass
    
    spring.jpa.hibernate.ddl-auto=validate
    spring.jpa.generate-ddl=false
    spring.jpa.show-sql=true
    ```
    

**결과**

```sql
//console.log
2022-02-23 15:27:42.083  INFO 3473 --- [           main] o.f.core.internal.command.DbMigrate      : Migrating schema "public" to version 1 - init
2022-02-23 15:27:42.087  INFO 3473 --- [           main] o.f.c.i.s.DefaultSqlScriptExecutor       : DB: table "account" does not exist, skipping
2022-02-23 15:27:42.089  INFO 3473 --- [           main] o.f.c.i.s.DefaultSqlScriptExecutor       : DB: sequence "hibernate_sequence" does not exist, skipping
```

```sql
// docker bash
List of relations
 Schema |         Name          | Type  |  Owner
--------+-----------------------+-------+---------
 public | account               | table | cherrue
 public | flyway_schema_history | table | cherrue
```

8-3. 컬럼 추가

8-3-1. 엔티티 수정

```sql
@Entity
public class Account {
...
		private boolean active;

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
...
}
```

```sql
Caused by: org.hibernate.tool.schema.spi.SchemaManagementException: Schema-validation: missing column [active] in table [account]
```

8-3-2. 마이그레이션 쿼리 추가

🚧 절대로 V1__init.sql 과 같이 한 번 실행된 쿼리 파일은 수정하지 않는다.

V2__add_active.sql 작성

```sql
alter table account add column active BOOLEAN;
```

**결과**

```sql
// console.log
2022-02-23 15:32:46.526  INFO 3892 --- [           main] o.f.c.internal.database.DatabaseFactory  : Database: jdbc:postgresql://localhost:5432/springboot (PostgreSQL 9.6)
2022-02-23 15:32:46.576  INFO 3892 --- [           main] o.f.core.internal.command.DbValidate     : Successfully validated 2 migrations (execution time 00:00.032s)
2022-02-23 15:32:46.592  INFO 3892 --- [           main] o.f.core.internal.command.DbMigrate      : Current version of schema "public": 1
2022-02-23 15:32:46.607  INFO 3892 --- [           main] o.f.core.internal.command.DbMigrate      : Migrating schema "public" to version 2 - add active
2022-02-23 15:32:46.635  INFO 3892 --- [           main] o.f.core.internal.command.DbMigrate      : Successfully applied 1 migration to schema "public" (execution time 00:00.052s)
2022-02-23 15:32:46.715  INFO 3892 --- [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
```

```sql
// docker bash
springboot=# select * from account;
 id | email | password | username | active
----+-------+----------+----------+--------
(0 rows)
```