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

### 08/27(금요일) 수업 공유 링크
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