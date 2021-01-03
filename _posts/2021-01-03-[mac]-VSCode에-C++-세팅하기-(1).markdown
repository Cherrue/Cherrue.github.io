---
layout: single
title: '[mac] VSCode에 C++ 세팅하기 (1)'
date: 2021-01-03 19:13:16 +0900
categories: mac setting
---

# VSCode로 개발환경 세팅

`Visual Studio`와 `Eclipse`, `XCode`를 사용하다보면 너무 무거운데?? 라는 생각이 듭니다.<br>
특히 알고리즘 한 두 문제 풀기 위해 main함수 이름 바꿔가면서 설정 바꿔가면서 아주 귀찮죠.<br>
dev c++도 사용해보았지만 빈약하게 느껴지는 기능들, 사용하는 언어가 늘어남에 따라 통합적으로 쓸 수 있는 ide를 찾다보니 `VSCode`에 정착하게 되었습니다.

VSCode는 가볍고 여러 운영체제와 언어에 호환 가능해 공부하는 입장에서 참 좋지만
초기 설정이 어려운 것이 단점인 ide입니다.

여기서는 VSCode를 통해 알고리즘 문제 풀이가 가능한 C++환경을 구축하는 것을 목표로 글을 작성하겠습니다.

---

### 설치 툴 설치하기

말이 이상하지만 설치하기 위한 설치 툴을 설치합니다.<br>
홈페이지에서 VSCode를 바로 설치해도 괜찮지만, 나중에 Package 관리 차원에서도, 다른 프로그램 설치할 때도 굉장히 편리하니 따라해보시기 바랍니다.<br>
명령창/쉘에서 프로그램 다운로드가 익숙해지면 편한것도 편한거지만 개발자가 되었다는 느낌이 든답니다.

mac은 `Homebrew`를 이용합니다.

-   Homebrew 설치<br/>
    terminal에서 [링크](https://brew.sh/)의 명령어를 복사하여 실행합니다.
    ```jsx
    // in terminal
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    설치 확인
    ```jsx
    // in terminal
    > brew --version
    Homebrew 2.7.1
    Homebrew/homebrew-core (git revision 7ceb74; last commit 2021-01-02)
    Homebrew/homebrew-cask (git revision a2f80; last commit 2021-01-02)
    ```

### VSCode 설치

brew는 항상 업데이트를 하고 쓰시기 바랍니다.<br>
brew cask 설치 방식이 brew cask install → brew install —cask로 바뀌었습니다.

```jsx
// in terminal
// brew update first
brew install --cask visual-studio-code
```

쉘에서 명령어 `code` 로 vscode 실행하려면<br>
vscode를 실행하고 ⇧⌘P를 입력하면 명령 팔레트가 나옵니다(명령줄>보기>명령 팔레트)
![shellcommand](/assets/images/2021-01-03/2021-01-03-shellcommand.png)
shell command라고 검색하고 PATH에 'code'명령 설치로 명령어 적용이 가능합니다.

### 컴파일러/디버거 설치

mac 이라면 컴파일러는 모두 설치 되어있습니다.

설치 확인

```jsx
// in terminal
> g++
clang: error: no input files

> g++ --version
Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/4.2.1
Apple clang version 12.0.0 (clang-1200.0.32.28)
Target: x86_64-apple-darwin20.2.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
```

디버거는 `gdb`와 `lldb` 중 `lldb`를 사용하겠습니다.<br>
lldb는 xcode를 설치한 적이 있다면 같이 딸려 들어옵니다.<br>
아래 설치 확인 명령어를 쳤을 때 lldb가 미설치 상태라면 자동으로 설치됩니다.<br>
(lldb)가 나오면 설치가 되어있는 것입니다.

설치확인

```jsx
// in terminal
> lldb
(lldb)
```

### VSCode Extension 설치

![CPPExtension](/assets/images/2021-01-03/2021-01-03-c++extension.png)

![LLDBExtension](/assets/images/2021-01-03/2021-01-03-codelldb.png)

확장프로그램 탭에서 C/C++과 lldb를 검색하여 위 확장 프로그램들을 설치합니다.

### 디버깅 환경 설정

`.vscode` 경로를 만들고 밑에 `launch.json`, `tasks.json` 파일을 만듭니다.

![filelist](/assets/images/2021-01-03/2021-01-03-filelist.png)

-   launch.json

    ```json
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "g++ - Build and debug active file",
                "type": "lldb",
                "request": "launch",
                "program": "${workspaceFolder}/compiled/${fileBasenameNoExtension}",
                "args": [],
                "preLaunchTask": "C/C++: g++ build active file",
                "stdio": [null, null, null],
                "terminal": "integrated"
            }
        ]
    }
    ```

    `name`이 vscode에 보이는 디버그 이름입니다. 원하시는대로 설정하시면 됩니다.<br>
    `preLaunchTask`는 `tasks.json`의 `label`과 일치시켜야 합니다.<br>
    `type: "lldb"`는 CodeLLDB가 깔려있어야 사용이 가능합니다.

-   tasks.json

    ```json
    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "cppbuild",
                "label": "C/C++: g++ build active file",
                "command": "/usr/bin/g++",
                "args": [
                    "-g",
                    "${file}",
                    "-o",
                    "${workspaceFolder}/compiled/${fileBasenameNoExtension}"
                ],
                "options": {
                    "cwd": "/usr/bin"
                },
                "problemMatcher": ["$gcc"],
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "detail": "compiler: /usr/bin/g++"
            }
        ]
    }
    ```

    `label`은 원하는대로 설정하시면 됩니다. 터미널에 출력되는 프로세스 이름입니다.<br>
    `groupd`의 `kind`는 `build`로 두셔야 단축키로 빌드가 가능합니다.

task에 빌드가, launch에 디버깅이 붙었다고 보시면 됩니다.<br>
이 설정은 프로젝트root/compiled/ 경로에 컴파일된 파일을 모아두는 설정입니다.<br>
저는 푼 소스코드를 github에 올릴 때 .gitignore 설정을 편하게 하기 위해 이렇게했습니다.<br>
이제 fn+F5 또는 F5 또는 메뉴바>실행>디버깅 시작으로 디버깅이 가능합니다.

### 디버깅 해보기

![LLDBExtension](/assets/images/2021-01-03/2021-01-03-debug.png)

좌측 상단 디버깅 화면에 launch.json에 적은 이름이, terminal 좌측 상단에 tasks.json에 적은 이름이 보이는 것을 확인할 수 있습니다!<br>
빌드를 실행하면 확장자가 없는 바이너리 파일과 dSYM폴더가 생기니 빌드 여부를 확인하시면 됩니다.

끝!
