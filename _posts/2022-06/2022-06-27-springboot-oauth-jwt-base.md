---
layout: single
title: \[Springboot\] OAuth2 와 JWT (1) 이론
date: 2022-06-27 07:57:31.504803 +0900
categories: springboot authentication
toc: true
toc_sticky: true
toc_label: Contents
---

최근 회원 가입 대신 많이 쓰이는 OAuth2를 이용한 SNS 로그인과 로그인 상태 유지를 위해 사용하는 JWT 방식의 인증을 소개합니다.

# OAuth 2.0

OAuth 2.0은 인증을 위한 산업 표준 프로토콜입니다. ([https://datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749))

OAuth를 통하면 인터넷 사용자들이 비밀번호를 제공하지 않고 다른 웹사이트의 정보에 대한 접근 권한을 부여받을 수 있습니다.

## Protocol Flow

각 리소스 제공자는 Authorization Server를 운영하며, OAuth를 통해 인증 요청 시 Access Token을 발급합니다.

이 때 발급 받은 Access Token을 통해 각 리소스 서버의 API와 사용자 정보를 가져올 수 있습니다.

```
     +--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+

                     Figure 1: Abstract Protocol Flow
```

* [https://datatracker.ietf.org/doc/html/rfc6749#section-1.4](https://datatracker.ietf.org/doc/html/rfc6749#section-1.2)

## Authorization Code Flow

인증 과정에서 Redirect가 발생하기 때문에 CSRF 관련 처리가 필요합니다.

```
     +----------+
     | Resource |
     |   Owner  |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier      +---------------+
     |         -+----(A)-- & Redirection URI ---->|               |
     |  User-   |                                 | Authorization |
     |  Agent  -+----(B)-- User authenticates --->|     Server    |
     |          |                                 |               |
     |         -+----(C)-- Authorization Code ---<|               |
     +-|----|---+                                 +---------------+
       |    |                                         ^      v
      (A)  (C)                                        |      |
       |    |                                         |      |
       ^    v                                         |      |
     +---------+                                      |      |
     |         |>---(D)-- Authorization Code ---------'      |
     |  Client |          & Redirection URI                  |
     |         |                                             |
     |         |<---(E)----- Access Token -------------------'
     +---------+       (w/ Optional Refresh Token)

   Note: The lines illustrating steps (A), (B), and (C) are broken into
   two parts as they pass through the user-agent.

                     Figure 3: Authorization Code Flow
```

* [https://datatracker.ietf.org/doc/html/rfc6749#section-4.1](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1)

## 장단점

- **장점**

클라이언트에서의 구현이 상당히 간단합니다.

타 서비스의 로그인 정보를 이용해 내가 만든 서비스에 쉽게 회원가입하도록 활용할 수 있습니다.

- **단점**

서버에서의 구현은 복잡합니다.

인증과정에서 redirect가 발생해 CSRF 예외 처리를 해야하는데, 이로 인해 CSRF 공격을 받을 수 있습니다.

매 인증에 authentication server에 갔다오면 내 서비스의 서버에도 부하를 줍니다. (빠른 작업이 아닙니다)

 → 그렇기 때문에 OAuth 인증 정보를 내 서비스의 user 데이터를 따로 쌓아야 합니다.

# JWT

JWT는 JSON Web Token의 줄임말로 선택적 서명 및 선택적 암호화를 사용하여 데이터를 만들기 위한 인터넷 표준입니다. ([https://datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519))

JWT는 두 개의 시스템 간에 전송될 클레임을 JSON 형태로 변환하는데, JWS(JSON Web Signature) 구조의 페이로드 또는 JWE(JSON Web Encryption) 구조의 일반 텍스트 형태를 갖습니다.

이 때 클레임은 디지털 서명이 되거나 MAC(Message Authentication Code)를 통해 암호화되어 안전하게 됩니다.

## 사용하는 이유

JWT는 서명을 들고 다니기 때문에, 서버에서는 세션 저장소 없이 서버에 저장된 개인키만을 이용해 이 토큰이 정상적인 토큰인지 검사할 수 있습니다.

대용량 트래픽을 처리하는 경우 stateful 한 서버가 상당히 부담이라서 stateless 하기를 윈합니다.

JWT는 세션저장소 없이 stateless 하게 처리할 수 있어 많이 쓰이고 있습니다.

## 구조

![1_jwt_structure](/assets/images/2022-06/27/1_jwt_structure.png)

- 헤더 : 서명 생성을 위한 알고리즘
- 페이로드 : 클레임
- 서명 : 토큰에 대한 서명

각 부분은 BASE64로 인코딩 됩니다.

## 장단점

- **장점**

위에서 말했듯 stateless 한 서버 구성이 가능해 대용량 트래픽 처리에 유리합니다.

- **단점**

어쨌든 쿠키에 저장하기 때문에 탈취 당하기 쉽고, 탈취 당했을 때 서버에서 알아챌 방법이 없습니다.

→ 토큰의 만료 기한은 짧게 설정하고, Refresh Token이나 Sliding sessions 등을 적용해야 합니다.

→ 은행 업무와 같은 도메인에는 사용하면 안 됩니다. 민감한 정보의 처리 시 2차 인증 등을 요구해야 합니다.

또한, 구조에서 보이듯 PAYLOAD는 암호화되지 않기 때문에 민감한 정보를 가져서는 안 됩니다.


여기까지 oauth와 jwt 개념을 살펴보았고 다음 편부터 springboot에서 oauth와 Jwt를 이용해 인증을 구현해보도록 하겠습니다.
