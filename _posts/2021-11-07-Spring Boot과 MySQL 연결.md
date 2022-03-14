---
layout: single
title: \[강의요약\] 스프링부트 개념과 활용 - Spring Boot MySQL 연결
date: 2021-11-07 19:31:00 +0900
categories: project drama_vote_platform


---

# Spring Boot과 MySQL 연결

## MySQL 설정

MySQL을 설치하고(mac) 테이블을 만든 후 spring boot 에서 호출해봅시다.

### 버전 정보

|    종류     |       버전       | 비고                                     |
| :---------: | :--------------: | ---------------------------------------- |
|     OS      | mac Big Sur 11.6 | latest                                   |
|  HomeBrew   |      3.3.2       | latest                                   |
|   DBeaver   |       2.4        | latest                                   |
|    MySQL    |      8.0.27      | latest<br />5.7과 8에는 차이가 크니 주의 |
| Spring Boot |      2.5.5       | minor 버전에 따른 차이에 주의            |

### MySQL 설치

Mac에서 brew를 이용해 설치합니다. (brew가 없다면 https://brew.sh/)

```shell
$ brew update
$ brew search mysql
==> Formulae
automysqlbackup        mysql-client@5.7       mysql@5.6
mysql                  mysql-connector-c++    mysql@5.7
mysql++                mysql-sandbox          mysqltuner
mysql-client           mysql-search-replace   qt-mysql
==> Casks
mysql-connector-python            mysqlworkbench
mysql-shell                       navicat-for-mysql
mysql-utilities                   sqlpro-for-mysql

$ brew install mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To start mysql:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql/bin/mysqld_safe --datadir=/usr/local/var/mysql

$ mysql --version  32s 18:42:13
mysql  Ver 8.0.27 for macos11.6 on x86_64 (Homebrew)
```

* 특정 버전 설치는 mysql@5.7 과 같이 @버전

### 추가 설정

```shell
$ mysql_secure_installation
Would you like to setup VALIDATE PASSWORD component? No
Please set the password for root here.
New password:
Re-enter new password:

Remove anonymous users? (Press y|Y for Yes, any other key for No) : yes
Success.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : Yes
Success.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Yes
Success.

All done!
```

공부할 땐 위와 같이 설정하면 무난합니다.

### MySQL 서버 기동

```shell
$ brew services start mysql
or
$ mysql.server start
```

확인

```shell
$ ps -ef |grep mysql
$ mysql -u root -p
mysql>
mysql> show processlist;
+----+-----------------+-----------+------+---------+------+------------------------+------------------+
| Id | User            | Host      | db   | Command | Time | State                  | Info             |
+----+-----------------+-----------+------+---------+------+------------------------+------------------+
|  5 | event_scheduler | localhost | NULL | Daemon  | 1478 | Waiting on empty queue | NULL             |
| 10 | root            | localhost | NULL | Query   |    0 | init                   | show processlist |
+----+-----------------+-----------+------+---------+------+------------------------+------------------+
2 rows in set (0.00 sec)
```

### IDE 연결

편한 것을 사용하면 됩니다.

MySQL workbench, DBeaver, HeidiSQL 중에 사용하면 무난한데, 여기선 DBeaver를 사용합니다.

![dbeaver_connect_1.png](/assets/images/2021-11-07/dbeaver_connect_1.png)

![dbeaver_connect_2.png](/assets/images/2021-11-07/dbeaver_connect_2.png)

비밀번호만 입력하면 된다. 나머지는 알아서 채워준다. 안 된다면 db port 를 확인해 보자

![dbeaver_connect_3.png](/assets/images/2021-11-07/dbeaver_connect_3.png)

연결에 성공하면 초록색 체크가 표시된다.



### 테스트 테이블 생성

![dbeaver_create_1.png](/assets/images/2021-11-07/dbeaver_create_1.png)

스키마 : drama

테이블 : test

컬럼 : id, name

* id에는 auto increase와 PK를 주자

```sql
INSERT INTO drama.test (name) values('a');
INSERT INTO drama.test (name) values('b');
INSERT INTO drama.test (name) values('c');
```

확인

```sql
SELECT id, name FROM drama.test;
+----+------+
| id | name |
+----+------+
|  1 | a    |
|  2 | b    |
|  3 | c    |
+----+------+
```



## Spring Boot에 MySQL 연결

### Project 설정

1. build.gradle

   ```groovy
   dependencies{
   	implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
   	runtimeOnly 'mysql:mysql-connector-java'
   	...
   }
   ```

2. application.properties

   ```
   spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
   spring.datasource.url=jdbc:mysql://localhost:3306/drama?useSSL=false&useUnicode=true&serverTimezone=Asia/Seoul
   spring.datasource.username=root
   spring.datasource.password=123
   spring.jpa.show-sql=true
   spring.jpa.hibernate.ddl-auto=update
   spring.jpa.properties.hibernate.format_sql=true
   ```

   * datasource : localhost:3306/{DB_SCHEMA}
   * spring.jpa.* 는 로그 남겨주는 옵션들

### ORM 코드 작성

1. Entity ({PROJECT_HOME}/Entity)

   ```java
   @Getter
   @Builder
   @AllArgsConstructor
   @NoArgsConstructor(access = AccessLevel.PROTECTED)
   @Entity(name="test")
   public class Test {
       @Id
       @GeneratedValue(strategy = GenerationType.AUTO)
       private Integer id;
   
       @Column(length=200, nullable = false)
       private String name;
   }
   ```

2. Repository ({PROJECT_HOME}/repository)

   ```java
   @Repository
   public interface TestRepository extends JpaRepository<Test, Integer> {
   }
   ```

### 테스트

/test/com.awards.drama/DramaApplicationTests.java

```java
	@Autowired
	TestRepository testRepository;

	@Test
	void SelectTestTable(){
		Optional<com.awards.drama.entity.Test> result = testRepository.findById(1);
		System.out.println("===== SelectTestTable RESULT =====");
		System.out.println(result.get().getName());
		assert(Objects.equals(result.get().getName(), "a"));
	}
```

```
Hibernate: 
    select
        test0_.id as id1_0_0_,
        test0_.name as name2_0_0_ 
    from
        test test0_ 
    where
        test0_.id=?
SelectTestTable RESULT =====
a
```

### TestApi 작성

1. controller

   ```java
       @GetMapping("/drama/dbtest")
       public List<Test> findAllTest(){
           return testService.getTestAll();
       }
   ```

2. service

   ```java
   @RequiredArgsConstructor // final 객체 생성자 삽입. autowired 효과
   @Service
   public class TestService {
       private final TestRepository testRepository;
   
       public List<Test> getTestAll(){
           return testRepository.findAll();
       }
   }
   ```

확인

```shell
$ curl localhost:8080/drama/dbtest
[{"id":1,"name":"a"},{"id":2,"name":"b"},{"id":3,"name":"c"}]
```

