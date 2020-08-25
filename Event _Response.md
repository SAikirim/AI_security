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

-----------------------------------------------

 INTERNAL------------FW----------EXTERNAL(INTERNAL)
 (WIN7)		  |
		  |
		SERVERS_IN
		(CENTOS)

현재 WIN7 -> CENTOS   WEB, SSH 서비스 가능.

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