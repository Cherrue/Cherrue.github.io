---
layout: single
title: [강의요약] MS Learn - Azure 네트워킹 서비스 살펴보기
date: 2021-11-24 23:55:00 +0900
categories: Azure azure_fundamentals
---

자격증 AZ-900 : Azure Fundamentals 취득을 위한 학습 과정 요약입니다.

https://docs.microsoft.com/ko-kr/learn/modules/azure-networking-fundamentals/

# Azure Fundamentals part 2: Describe core Azure services

---

## Explore Azure networking services

##### Azure Virtual Network(VNets) 기본 사항

> Azure 리소스 간 통신이 가능하고, 온 프레미스 클라이언트와 통신 가능

1. 제공 기능

1-1. Isolation and segmentaion : 격리된 가상 네트워크를 만들어 private ip 공간을 정의할 수 있고, 각 주소 공간을 서브넷에 할당이 가능함.

1-2. Internet communications : public ip를 붙여서 외부 인터넷에서 연결이 가능하게 설정 가능

1-3. Communicate between Azure resources

`Virtual Network`를 이용해 모든 Azure 리소스 간 연결 가능

`Service endpoints` 를 이용하여 엔드포인트를 지정해 보안성 강화 가능

1-4. Communicate between on-premises resources : 사내망과 Azure망 연결 방법 3가지

`Point-to-site virtual private networks` : 암호화된 VPN 연결을 통해 외부망과 사내망을 연결. 

`Site-to-site virtual private networks` : 온 프레미스의 VPN 디바이스나 게이트웨이를 Azure VPN 게이트웨이에 연결. Azure까지 사내망으로 보임

`Azure ExpressRoute` : Azure 전용 프라이빗 연결. 인터넷이 아님. 큰 대역폭과 높은 수준의 보안이 필요한 경우 사용

1-5. Route network traffic

`Route tables` : 트래픽 전달 규칙 사전 정의

`Border Gateway Protocol` : Azure VPN 게이트웨이나 ExpressRoute로 작업해 온 프레미스 BGP 라우팅을 Azure에 전달

1-6. Filter network traffic

`Network security groups` : 인바운드/아웃바운드 규칙

`Network virtual appliances` : Firewall, WAN 최적화 등을 수행하는 특수 VM

1-7. Connect virtual networks : `peering` 을 통해 가상 네트워크간 연결

1-8. User Defined Routing : 더 세부적으로 설정 가능한 사용자 정의 라우팅

---

### Azure Virtual Network setting

1. 가상 네트워크 만들기

1-1. Network name : 구독 내 unique

1-2. Address space : `CIDR`(Classless Interdomain Routing) 형식. 모든 네트워크에서 유일해야 함.

10.0.0.0/24 : 10.0.0.1 ~ 10.0.0.254

10.0.0.0/16 : 10.0.0.1 ~ 10.0.255.254

10.0.0.0/8 : 10.0.0.1 ~ 10.255.255.254

1-3. Subscription / Resource group

1-4. Location : region 지정

1-5. Subnet : 네트워크 주소 공간을 분할. 서브넷 간의 라우팅은 default traffic routes 을 따른다. 

1-6. DDoS protection

1-7. Service endpoints : Azure Cosmos DB, Azure  Service Bus, Azure Key Vaults 등

2. 추가 설정 정의

2-1. Network security group

2-1. Route table

3. 구성

Azure portal, PowerShell, Cloud Shell 에서 작업 가능

3-1. 추가설정 : IP address spaces, Connected devices, Subnets, Peerings

3-2. 네트워크 모니터링 및 가상화 네트워크 생성 자동화 스크립트 생성 가능

---

### Azure VPN Gateway 기본사항

VPN은 암호화된 터널을 사용하여 공격 방지 가능

1. VPN 게이트웨이

- site-to-site : 온 프레미스 - virtual network 연결
- point-to-site : 개인 device - virtual network 연결
- network-to-network : virtual network - virtual network 연결

모든 데이터는 인터넷을 통과할 때 private tunnel 에서 암호화.

virtual network는 하나의 VPN 게이트웨이만 갖지만, 게이트웨이 간 연결을 통해 통신 가능

VPN Gateway는 VPN type으로 policy-based와 route-based에서 선택함. 둘 다 공개키 암호화인데, 어떤 트래픽을 암호화할 것인가 선택하는 거임

1-1. Policy-based VPN : 암호화할 패킷의 IP주소를 정적으로 지정. IKEv2로 암호화. 기존 VPN과의 호환 등에 사용

1-2. Route-based VPN : 그냥 라우트만 보고 VPN 태우기. 어떤 터널을 태울지 정함. IKEv2. 동적 라우팅 지정도 가능

- 사용하는 경우 : 가상 네트워크 간 연결. 지점-사이트 간 연결. 다중 사이트 연결. ExpressRoute 게이트웨이와 사용

2. VPN Gateway 크기

| 종류   | 벤치마크 |
| ------ | -------- |
| 기본   | 100Mbps  |
| VpnGw1 | 650Mbps  |
| VpnGw2 | 1Gbps    |
| VpnGw3 | 1.25Gbps |

3. VPN Gateway 배포

3-1. 필요한 Azure 리소스

- Virtual Network
- GatewaySubnet : 적어도 27 주소 마스크 사용
- public IP address
- local network gateway : 온프레미스쪽 게이트웨이
- Virtual Network gateway : 애져 쪽 게이트웨이
- 연결 : local 게이트웨이 - 가상 네트워크 게이트웨이 연결

3-2. 필요한 온프레미스 리소스

- VPN 디바이스
- public IPv4 address

4. 안전한 게이트웨이 만들기

4-1. 두 개의 게이트 웨이 사용(활성/대기, 활성/활성)

4-2. failover 사용 : ExpressRoute의 기능

4-3. zone-redundant gateways : 게이트웨이 끼리 영역이 겹치게 구성

---

### Azure ExpressRoute 기본사항

1. ExpressRoute : 온프레미스 네트워크와 Microsoft Cloud 간 3 layer dusruf

Microsoft 서비스니까 다 됨. region 상관 없고, 동적 라우팅도 되고, peer가 많아서 안전하고, 보장도 함. 스카이프도 함

용어 : layer 3, built-in redunduncy, MS cloud service, global reach, 동적 라우팅, cloudExchange/point-to-point/any-to-any



지식점검

암시적 FTP over SSL /  / 가상 네트워크 피어링 / 암호화된 네트워크 통신