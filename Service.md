# DNS 서버

### DNS 서버가 필요한 이유
* 내부에서 캐싱하여 많은 네트워크 트래픽을 제한함


### hosts 파일 확인
`# ls -l /etc/nsswitch.conf`
* 네임스위치 설정 파일
* DNS 정보를 가져오는 순서를 설정함

### DNS 확인 흐름(내부)
1. cache
2. /etc/nsswitch.net
    hosts   files dns
3. file -> /etc/hosts
4. dns -> /etc/resolv.conf

### root hint NS server
* 라운드 트리 타임으로, 라운드 로빈을 함
* 라운드 트리 타임이 낮으 쪽으로 호출을 해줌

## DNS 서버는 restart를 하지 않음, reload함! 
`/etc/rndc.conf`
* DNS 캐시에 관련된 설정 파일

`# rndc reload`
* DNS 서버 설정 재시작(리로드)

* 관용적으로 쓰는 zone 파일명
    - .zone, .rev

### 외부 호출과 내부 호출을 나누어서 DNS 서버 구성 가능(bind)

`dig @10.0.2.20 test.com axfr`
* Zone Trasfer 전송 옵션

---
## DNS 보안 설정
### DNS 서버 정보 확인
`# dig @70.12.113.74 version.bind chaos txt`
* DNS 서버 버전 정보 확인
* /etc/named.comf(버전설정 바꾸기) 
    - version    "Hello World";

### Zone Transfer 요청
`# dig @70.12.113.74 test.com axfr`
* 설정이 안되어 있으면 정보를 받아옴
* /etc/named.comf or /etc/named.rfc1912.zones
    - Allow-transfer { none; };


### 리커션 에러(Recursion error)
`dig @70.12.113.74 test.com +trace`
* 순환 질의로 요청
* /etc/named.comf
    - allow-recursion { none; };        # { trusted; };
    - acl trusted { 127.0.0.1/24; };    # option 밖에 설정
    - recursion no;

---
---
## 프로그램 동작 확인
* systemctl -a | grep httpd
* ss -tanp | grep :80
* ps -ef | grep http[d]

```
# ps aux |head -2
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.3 128608  7084 ?        Ss   08:52   0:01 /usr/lib/systemd/systemd
```
* cpu, mem 점유율 확인 가능

```
# ps -ef | head -2
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 08:52 ?        00:00:01 /usr/lib/systemd/systemd --switched-root -
```
* PID 확인 가능


### 의심 프로세스 확인 흐름
```
# ss -tanp |grep :53
LISTEN     0      10     192.168.122.1:53                       *:*                   users:(("named",pid=1471,fd=26))

# ps -ef | grep 1471
named     1471     1  0 08:53 ?        00:00:00 /usr/sbin/named -u named -c /etc/named.conf

# ls -l /proc/1471/exe
lrwxrwxrwx. 1 named named 0 Jul 22 08:53 /proc/1471/exe -> /usr/sbin/named

# rpm -qf /usr/sbin/named
bind-9.11.4-16.P2.el7_8.6.x86_64

# rpm -V bind
S.5....T.  c /etc/named.conf
S.5....T.  c /etc/named.rfc1912.zones
```
* 실제 동작 중인 파일 확인 가능
    - ss -tanp : p 옵션(pid) 
    - rpm -qf <FILE> : FILE의 무슨 패키지인지 확인
    - rpm -V bind : 무결성 확인
        + T : 해시값 확인

---
# WEB 서버
* 백엔드 : 서버 사이드
* 프런트 : 클라이언트 사이드
    - 클라이언트는 브라우저에서 해석이 되는 것만 제공 받음
    - 프런트에서만 제공 받음


### 전송에 대한 규칙
HTTP 0.9 1.0 1.1 2.0
method : GET, POST

* http status code
    - 참고 : https://developer.mozilla.org/ko/docs/Web/HTTP/Status

### web 서버 종류
* apache
* iis
* nginx

* tomcat 
    - 단독 web server : jsp 환경 제공 : WAS
    - 기존 web server + tomcat 구성 가능 : WEB

#### WAS
* jeus  - 티맥스
* weblogic - Oracle
* WebSphere - IBM사