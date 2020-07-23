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

### root hint name server
* 라운드 트리 타임으로, 라운드 로빈을 함
* 라운드 트리 타임이 낮으 쪽으로 호출을 해줌

## DNS 서버는 restart를 하지 않음, reload함! 
* 실제 DNS 서버는 restart를 하는데 오래 걸림

`/etc/rndc.conf`
* DNS 캐시에 관련된 설정 파일
    - rndc 관련 패키지가 없어서 그런지, 파일이 존재하지 않음

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
    - allow-recursion { none; };        # { trust; };
    - acl trust { 127.0.0.1/24; };    # option 밖에 설정
    - recursion no;

---
---
## 프로그램 동작 확인
* systemctl -a | grep httpd
* ss -tanp | grep :80
* ps -ef | grep http[d]

```bahs
# ps aux |head -2
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.3 128608  7084 ?        Ss   08:52   0:01 /usr/lib/systemd/systemd
```
* cpu, mem 점유율 확인 가능

```bash
# ps -ef | head -2
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 08:52 ?        00:00:01 /usr/lib/systemd/systemd --switched-root -
```
* PID 확인 가능


### 의심 프로세스 확인 흐름
```bash
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
HTTP 0.9, 1.0, 1.1, 2.0  
method : GET, POST

* http status code
    - 참고 : https://developer.mozilla.org/ko/docs/Web/HTTP/Status

### web 서버 종류
* apache
* iis
* nginx 
    - apache가 가지고 있는 문제점을 해결

* tomcat 
    - 단독 web server (jsp 환경 제공) : WAS
    - 기존 web server + tomcat 구성 가능 : WEB

#### WAS
* jeus  - 티맥스
* weblogic - Oracle
* WebSphere - IBM사

## java
* 프로그램은 컴파일함
    - 호환성이 떨어짐
* 호환성을 위해 만들어짐
* jsp도 비슷함

#### jsp 사용 이유
* ERP 사업에 유용했음
    - ERP(Enterprise Resource Planning)
        + 기업 내 생산, 물류, 회계, 영업, 구매, 재고 등 경영 활동을 통합적으로 관리하는 프로그램
        + 기업에서 발생하는 정보를 통합적으로 실시간 공유할 수 있는 프로그램 = 전사적자원관리시스템 or 전사적통합시스템

#### .htaccess
* 설정을 잘못하면 망함

### 서버 관리자가 꼭 해야하는 설정
* 서버 정보는 노출되지 않게 설정
* Indexes, ExecCGI, FollowSymLinks, Includes 설정 하지 않기(잘 확인하기)
* 에러 출력은 통일해서 사용

### HSTS
* 처음부터 HTTPS(443)를 사용, 암호화
* http로 풀리지 않게 방지, 잠금

###  QUIC(HTTP/3)
* udp 사용(빠름)
* 암호화 기능




----
----
# DB 
* 무겁고, 외부 노출 위험 때문에 로컬 호스트로 웹 서버하고만 통신함


---
---
# FTP
* 인증 : 21/tcp
* 데이터 전송 연결(Active) : 20/tcp
    - 공유기(NAT 네트워크)가 있으면 데이터 전송 안됨 안됨
    - 다수의 클라이언트가 20/tcp에 연결

* Passive 모드
    - 포트 낭비가 심함
    - 클라이언트가 연결 요청

`ss -tan |grep .74`
* *.74의 주소의 ftp 서버의 '데이터 전송'을 확인

#### 유용한 ftp 명령어
```bash
ftp> binary         # data를 스트림으로 받음, 큰 데이터를 나누어서 받음
ftp> hash           # 해시출력으로 다운로드 상태 확인 가능
ftp> lcd            # 자신의 다운로드 위치 변경
```

## !시스템 계정으로 로그인!
* 소유자 권한으로 업로드 가능 - 장점
* 시스템의 계정으로 로그인하기 때문에 위험함! - 단점
    - 가상 계정으로 만들어 사용 권장

## FTP 방화벽!
* 방화벽 포트는 21/tcp만 열어줌
* 20번 포트는 왜 없음?
    - 메모리에 ESTABLISHD한 소캣은 바이패스(bypass)
    - stateful inspection
        + role 정책을 줄일 수 있음
    


#### TFTP
- udp를 사용(69/udp)
- 빠른 업데이트를 위해 사용
- 로그인 절차 없음

---
## user를 신뢰할 수 있는가?
* 로그인이 안되는 only 데몬을 동작시키기 위한 user를 생성하고 그 생성된 user로 데몬을 동작시킴
    - 보안 관점에서는 권장
* 0 ~ 1023 프로세스(admin/root 권한으로 실행한) 중에서 하나를 이용하여 client가 접근하면 1024 ~ 49151 사이의 포트로 접근 할 수 있는 정보를 제공
    - rpc 사용
    - `rpcinfo -p`
        + 111 => 1024 ~ 49151 : 포트를 맵핑
    - rpc는 접근 제어가 힘듬
        + 보안 위험
    - 개발자 입장에서는 사용하기 편함

* 상대방이 접속할때 user권한은 믿을 수 없음
    - shell을 못 사용하게 함
        + NFSv4가 사용(서비스 계정 사용)
    - root 권한으로 user계정(포트)으로 서비스을 사용할 수 있게함
        + NFSv3이 사용

---
---
# 문서 편집 명령어
### cut
* -d " " : 공백을 기준으로 필드 설정
* -f : 필드 선택
    - `cut -d " " -f 1,3 data.txt`

### paste
* 형식 paste [옵션] “파일이름” “파일이름”
* 사용 예) # paste –d : exam1 exam2
* 옵션
    - -s 한 파일의 내용을 한 줄로 보여준 후 다른 파일의 내용을 한 줄로 덧붙인다.
    - -d 출력되는 내용의 구분자를 지정한다

### diff
* 형식 diff [옵션] “파일이름” “파일이름”
* 사용 예) # diff exam1 exam2
* 옵션
    - -b space를 무시하고 비교한다.

### grep
* i, b, v, l, c
    - -l : 파일 명
    - -c : 카운트
    - -b : 바이트 오프셋
    - -n : 텍스트 라인

### sort
* <fort color="red">-r, -t, -k</fort>


### uniq
* 중복 제거
* -c

### sed
* `sed  '3q' data.txt`
* `sed  '4,$d' data.txt`
* `cat -n data.txt |sed -n '2,5p'`
* `cat -n data.txt |sed -n '1,$s/japan/bosung/gp'`
* `cat -n data.txt |sed -e 's/us/bosung/g' -e '/japan/d'`
    - ` sed -f sedfilter data.txt`
    ```
    # cat sedfilter
    s/us/bosung/g
    /japan/d
    ```

### awk
* `df -hT | awk -F " " '$2 == "xfs"{print $1,"사용량 :",$6}'`
* `df -hT |sed 's/%//g' |awk -F " " '$2 == "xfs" && $6 > 10{print $1,"사용량:",$6"%"}'`

* `cat lastb.txt | awk '{ print $3 }' |grep ^ip- | sort |uniq | sed -e 's/ip-//g' -e 's/-/./g' -e 's/\.$//g'`
* `awk 'BEGIN { sum=0; line = 0} { sum += $2; line ++;} END { average = sum /line; print "나이의 평균:" average "세";}' data.txt`


---
# iscsi 블록 스토리지

### DAS

### NAS

### SAN
* FC-SAN
* IP-SAN

#### SCSI(Small Computer System Interface)
- 저장장치에 작은 첨퓨터를 넣어 입출력을 컨트롤하게 만듦
- 컨트롤러가 여러 저장장치를 관리함
- 속도 빠름, 안정성 높음(핫 스왑핑)

### 파티션은 실린더 단위로 함!

---
# NFS 스토리지
* fstab 잘 설정하기
    - nfs 서버가 작동중이지 않으면, 스킵하도록 설정!

---
<!--https strict
    http3
    stateful inspection
    ftp 가상 유저추가
    rpc -->


