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
