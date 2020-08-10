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
