# Web Hacking

## 월드 와이드 웹(World Wide Web, WWW, W3)
*  인터넷에 연결된 컴퓨터를 통해 사람들이 정보를 공유할 수 있는 전 세계적인 정보 공간 - 일반적인 의미
* 인터넷에서 HTTP 프로토콜, 하이퍼텍스트, HTML형식 등을 사용하여 그림과 문자를 교환하는 전송방식 - 기술적 의미

---
### archive.org
* 정보 수집에 이용할 수 있음


---
### SSS(Server Side Script)
* asp, php, jsp 등

### CSS(Client Side Script)
* HTML, Javascript, 비쥬얼베이직 스크립트 등

### __*모든 보안 조치는 CSS가 아니고 SSS에서 해야함!*__

---
## HTTP 프로토콜
* Wep Proxy
    - fiddler, burp suite

### HTTP(Hyper Text Transfer Protocol)
* 인터넷에서 쓰이는 핵심 프로토콜
* 요청 응답 형식으로 동작
* 오늘날 주로 사용되는 버전은 1.1
* 비연결지향성 프로토콜

===================================
#### http 1.0
* 단순한 동작이 반복적으로 발생
* 필요없는 연결수립과 연결 종료과정발생

#### http 1.1
* 지속적인 연결의 필요성, 가상 호스트, 계층적 프록시 등등에서 HTTP 1.0 보다 개선

#### http 2.0
* 속도 개선, 다중연결, 병령 연결


### HTTP Request 구조
``` 
 Request Line(Start Line)
 Headers
 공백
 Body
```
* Request Line(StartLine:요청, Status Line: 응답)
    - 메소드 URL HTTP Version
    - POST /sam/status.cgi HTTP/1.1

* Headers에는 메타정보가 들어있음
    - Cookie : 쿠키 값
    - Host : utl주소상에 나타나는 호스트명
    - user-agent : 클라이언트가 사용하는 브라우저나 기타소프트웨어 정보
    - Referer : 접속하는데 참고한 url

===================================================
### Method
* __GET__ : 지정된 URL 정보를 요청
    - 전달해야 하는 파라메터를 URL에 포함시켜서 전달
    - GET으로 보내는 파라미터는 길이제한이 있음
        + 요즘 브라우저는 그렇게 제한되어 있지는 않음
실제로 보여주기
* __POST__ : 지정된 URL 정보를 요청 
    - 전달해야 하는 파라메터를 메시지 본문(Request Message Body) = HTTP 바디를 통해서 전달
    - 보안적으로 약간 더 안전(id,password 생각)
        + 그렇다고 보안적으로 안전한건 아님
    - POST로 보내는 파라미터는 길이제한이 없다.     
        + 그렇다고 무한정보낼수 있다는건 아님
* HEAD : HTTP Header 정보만 응답으로 요청한다.
* TRACE : 클라이언트의 요청을 그대로 응답
    - Request의 Loop Back 테스트
* DELETE : 요청하는 URL의 자원을 삭제
* OPTIONS : 서버에서 지원하는 HTTP 메소드 정보를 요청
* PUT : 요청하는 URL의 자원을 생성
    - Ex) 파일 업로드가 가능

### HTTP Response 상태 코드(웹 서버의 응답코드)
``` 
 Status Line
 Headers
 공백
 Body
```
* Status Line
    - httpVersion 상태코드 상태문구정의
    - HTTP/1.1 200 ok

```
- 100~199 : 단순한 정보
- 200~299 : Client의 요청이 정상적으로 처리됨
- 300~399 : Client의 요청이 수행되지 않아 다른 URL로 재지정
- 400~499 : Client의 요청이 불완전하여 다른 정보가 필요함
- 500~599 : Server의 오류로 Client의 요청 수행 불가
```
* 200 : OK : 클라이언트의 요청이 성공함
* 400 : Bad Request : 클라이언트가 서버에 잘못된 요청을 함
* 401 : Unauthorized : 클라이언트가 HTTP 인증을 받아야 함
* 403 : Forbidden, Server가 Client에게 권한을 주지않는 상태
* 404 : Not Found, 지정한 문서가 존재하지 않음
* 500 : Internal Server Error
        Server의 일부가 멈췄거나 설정에서 오류 발생
* 503 : Service Unavailable
        최대 Session 수를 초과하는 등 웹서비스가 불가능한 경우

상태코드는 100퍼센트 정확한 것은 아니다.

#### 메소드 실습(OPTIONS, PUT)
* options 메소드로 정보 수집
```cmd
.\nc.exe 70.12.113.49 8081
OPTIONS / HTTP/1.1
host:70.12.113.49
```
* put 메소드로 파일 생성
```
.\nc.exe 70.12.113.49 8081
PUT /chapter5/tester.html HTTP/1.1
host: 70.12.113.49
Content-length: 20
theFlower go go go!
```

---
### URL 구조  
`https://www.google.co.kr/search?source=hp&ei=TnszX9DGFIT7wQPS34vwBQ&q=adsadasd&oq=adsadasd&gs_lcp=CgZw`  
* 프로토콜 : 서버와 어플리케이션이 통신하기 위한 통신 규약
* 서버이름 : 서버의 hostname 또는 ip 주소
* 포트 : 브라우저와 통신하기 위해 열려있는 서버의 포트
* 파일경로 : 서버내에서 자원의 위치 디렉터리/파일명
* 파라미터 : 동적으로 결과를 생성하는 어플리케이션에 전달하는 값

#### URL 파라미터 메타문자
* ? : URL의 파일 경로 뒤에 붙어 파라미터를 전달할 때 사용
* = : 파라미터 항목과 값을 연결
* & : 복수의 파라미터를 연결
* % : URL인코딩
* \+ : 공백

#### 인코딩
* 내용은 같은나 데이터의 형태를 바꾸는 방식
    - 암호화는 아님
##### 웹에서 사용하는 인코딩
* URL 인코딩
    - URL 특정문자나 문자열을 표현하기 위해 %뒤에   문자의 HEX코드를 붙임
* BASE64 인코딩
    - 64 + 1개의 문자로 구성하여 인코딩
    - 2진수 데이터를 ASCII형태의 텍스트로 표현가능
    - web인증 중 기본인증에 사용
    - 끝부분에 padding(=)이 붙음, '=':2bit
    - 64개의 문자를 사용 (영문 대(26) 소(26) 숫자(10) + / )
    - 데이터를 6bit단위로 표현

---
### WebGoat 접속
* 192.168.195.132:8080/WebGoat/attack
* webgoat/webgoat

### WebGoat 테스트
* 접근제어 취약점 ( 불충분한 인증, 불충분한 인가 ...)
    - 공격 방법 : 강제 브라우징(dirbuster), 파라미터 변조, 쿠키 변조

* CRUD METRIX (웹 개발 매커니즘)    # ex) 게시판
    - CREATE : 등록, 회원가입, 쓰기 -> new, write        
    - READ :  조회, 뷰  -> read, content, view, search
    - UPDATE : 수정 -> modify, update, edit
    - DELETE : 삭제 -> del, delete, remove

* 강제 브라우징에 사용할 값
    - /admin, /manager, /configure, /conf, ....