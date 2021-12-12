---
layout: single
title: [Linux] Windows PC에 Rocky Linux 설치
date: 2021-12-13 00:48:00 +0900
categories: Linux Infra
---

Linux에 이거저거 테스트 하고 싶은데, AWS에서 돈이 부과되는 걸 보고 데탑에 Linux를 올리기로 했습니다.

하지만 게임도 해야하고 문서 작업도 가끔 필요해서 Windows를 아예 버릴 순 없어서 멀티부트로 구성하기로 했습니다.

준비물은 8GB 이상의 USB입니다.

### 1. 설치할 리눅스 선택

- CentOS7 : 2024년 보증 만료 예정. RHEL의 다운스트림
- CentOS8 : 2021년 보증 만료 예정. RHEL의 다운스트림. 더이상 CentOS N은 출시되지 않음
- CentOS stream : CentOS N을 대체하는 RHEL의 업스트림. 쉽게 말하면 RHEL의 베타 버전
- Ubuntu : debian 계열의 linux
- Oracle Linux : Oracle에서 출시한 RHEL의 복제 리눅스. 무료긴 한데 오라클.
- Rocky Linux : CentOS를 주도했던 아저씨가 진행하는 프로젝트. 마찬가지로 RHEL의 복제 리눅스. stable 버전까지 출시 완료

회사에서 CentOS7을 쓰고 있어서 CentOS 계열을 사용하려는데, CentOS Stream 때문에 애매해졌다.

아무래도 Oracle은 언제 유료화 할 지 몰라서 gregory krutzer가 진행하는 Rocky를 쓰기로 했다.

### 2. 부팅 USB 만들기

2-1. 이미지 설치 : [https://rockylinux.org/download](https://rockylinux.org/download) 에서 x86_64의 minimal로 설치

2-2. rufus 설치 : [https://rufus.ie/ko/](https://rufus.ie/ko/) 에서 최신버전 설치

2-3. 설정

![bootingusb1](/assets/images/2021-12-12/bootingusb1.PNG)

파티션 방식 : 보통은 MBR / UEFI

파일시스템 : Large FAT32나 FAT32 선택

2-4. 시작 : rufus가 시키는 대로 한다(hybrid이미지를 iso로만 설정, 없는 파일 다운로드, 포맷여부 확인)

* USB 안에 필요한 파일이 없는지 확인하고 진행할 것

![bootingusb1](/assets/images/2021-12-12/bootingusb1.PNG)

![bootingusb3](/assets/images/2021-12-12/bootingusb3.PNG)

### 3. 볼륨 축소

3-1. 용량 확보

- 디스크 정리 : 시작 > 디스크 정리 > 시스템 파일 정리 > 전체 정리
- 시스템 파일 압축 : cmd 에서 CompactOs /CompactOs:query로 확인하고 CompactOs /CompactOs:always

3-2. 볼륨 축소

시작 > 파티션 검색

![partition1](/assets/images/2021-12-12/partition1.PNG)

### 4. 이미지 설치

4-1. 부팅 옵션 변경 : 재부팅 > bios 진입 > boot > 부팅 우선순위 변경(usb를 1순위)

4-2. 설치 : Install Rocky Linux 8

![rocky_install](/assets/images/2021-12-12/rocky_install.jpeg)

- 언어 설정 영어로 할 것

- keyboard, language support는 한글 추가가 가능

- software selection : Minimal Install + Development Tools 선택

  Server로 선택하면 GNOME(gui) 등을 추가 설정할 수 있다. 보통은 minimal만 해도 충분하다.

- Installation Destination : 아까 축소해준 빈 공간 선택

- Network & Host Name : 실수로 설정을 안 했는데, 이더넷 케이블이 붙어있다면 여기서 잡아주고 가자

- Root Password는 설정하지 않으면 넘어가지 않는다.

4-3. 설치 완료 확인

- linux 버전 확인

  ```bash
  $ cat /etc/*release
  Rocky Linux release 8.5 (Green Obsidian)
  NAME="Rocky Linux"
  VERSION="8.5 (Green Obsidian)"
  ID="rocky"
  ID_LIKE="rhel centos fedora"
  VERSION_ID="8.5"
  PLATFORM_ID="platform:el8"
  PRETTY_NAME="Rocky Linux 8.5 (Green Obsidian)"
  ANSI_COLOR="0;32"
  CPE_NAME="cpe:/o:rocky:rocky:8.5:GA"
  HOME_URL="https://rockylinux.org/"
  BUG_REPORT_URL="https://bugs.rockylinux.org/"
  ROCKY_SUPPORT_PRODUCT="Rocky Linux"
  ROCKY_SUPPORT_PRODUCT_VERSION="8"
  Rocky Linux release 8.5 (Green Obsidian)
  Rocky Linux release 8.5 (Green Obsidian)
  Rocky Linux release 8.5 (Green Obsidian)
  ```

- development tools

  ```bash
  $ whereis python
  python: /usr/lib/python3.6 /usr/lib64/python3.6 /usr/include/python3.6m /usr/share/man/man1/python.1.gz
  ```

  RHEL 8.4 기반이기 때문에 python3이 기본으로 설치된다.

### 5. 멀티부팅 설정

5-1. boot priority 변경 : 재부팅 > bios > 기존 하드디스크로 변경

5-2. 부팅화면에서 grub 진입 : 아래의 화면에서 "c" 입력

![select_os1](/assets/images/2021-12-12/select_os1.jpg)

5-3. windows가 깔린 파티션 이름 확인 : ls -l 입력하여 윈도우가 깔린 하드웨어에 좀 작은 파티션 이름을 기억한다

나같은 경우는 아래에서 hd,msdos01이다.

![hd_list](/assets/images/2021-12-12/hd_list.jpg)

5-4. 리눅스를 부팅해서 부트로더를 설정한다

```bash
$ sudo vi /boot/grub2/grub.cfg
### BEGIN /etc/grub.d/10_linux ###

### added by cherrue
menuentry "Windows 10" {
  insmod chain
  insmod drivemap
  set root=(hd0,msdos1)
  chainloader +1
}
```

저 BEGIN 주석 있는 블럭에 작성해주자

5-5. 재부팅하여 목록 확인

![select_os2](/assets/images/2021-12-12/select_os2.jpg)

![boot_windows](/assets/images/2021-12-12/boot_windows.jpg)

----

윈도우로 부팅했다가 리눅스로 부팅하니 괜히 팬이 좀 조용해진 것 같다.

이제 파워만 바꿔달면 피시를 안 끄고 살아도 될 것 같다.

다음 글에서 추가적인 리눅스 설정을 잡아주도록 하겠다.