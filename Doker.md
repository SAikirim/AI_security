
# 4차 산업 관련 기반 지식
* 로봇
* 인공지능
* 클라우드
* 빅데이터
* 사물인터넷
##### => 융합

---
### 클라우드 기본
* 클라우드 기본 개념
    - 클라우드 : 원하는 자원을 빌려와서 사용하는 것

### 클라우드 서비스
* 네이버 클라우드
* 아이폰: iCloud
* Google Drive, One Drive
* Google Document

* 퍼블릭 클라우드
    - AWS, GCP, Azure, Naver Cloud
* 프라이빗 클라우드
    - 클라우드의 장점을 온프레미스와 결합

### 클라우드 유형
IaaS : Infrastructure as a Service
PaaS : Platform as a Service
SaaS : Software as a Service  
참고 : https://wnsgml972.github.io/network/2018/08/14/network_cloud-computing/

Cloud <==> On-Premises(온프레미스, 온프렘)

### 클라우드 서비스의 장점
* 초기비용이 저렴
    - 직접 하드웨어 및 인프라를 갖풀 필요가 없음
* 확장성이 뛰어남
* 자동적인 백업 구현
    - 동시메 여러 곳에 인프라 구축 가능
* 빠른 대응 등이 가능

### 클라우드 서비스보다 온프레미스가 유리한 경우
* 클라우드 서비스보다 높은 가용성 요구
    - SLA (Service Level Agreement)
        + 서비스 가용 계약
* 중요 데이터에 대한 기밀성 보장
* 특수한 요구사항이 있는 서비스

---
## 가상화(Virtualization)
* 자원을 가상으로 분할  
참고 : https://tech.cloud.nongshim.co.kr/2018/09/18/%EA%B0%80%EC%83%81%ED%99%94%EC%9D%98-%EC%A2%85%EB%A5%983%EA%B0%80%EC%A7%80/
    - 호스트 기반 가상화
    - 하이퍼 바이저 기반 가상화
    - 컨테이너 기반 가상화


### 컨테이너 (Contaner)
* 격리성

#### 격리의 필요성
* 하나의 물리 머신에 다수의 서비스를 가동하면, 하나의 서비스에 문제가 생길 시 다른 서비스에도 영향을 끼칠 수 있음
* 종속 항목의 충돌이나 리소스 경합을 걱정할 필요 없음

---
* IaC : Infrastructure as a Code
    - 인프라 관리를 코드로 수행

---
### 소프트웨어 설치 방법
1. 소스코드 컴파일
    - gcc 등의 컴파일러를 사용하여 일일히 컴파일
2. 사전에 정의된 설정에 따라 컴파일
    - Makefile 파일이 존재
* 설치 과정
    ```
    # configure
    # make
    # make install
    ```
3. 패키지 파일 형태로 된 파일을 설치
    - CentOS : xxx.rpm 
    - Ubuntu : xxx.deb
4. yum을 사용한 레포지토리 설치
    - 기본 제공 레포지토리
    - epel-release : Extra Package for Enterprise Linux
    - `# yum install epel-release`
        + 새로운 레포지토리를 추가
5. 별도의 레포지토리를 추가
도커 설치 매뉴얼 : https://docs.docker.com/
    1) 필요한 기본 패키지 설치  
    `$ sudo yum install yum-utils device-mapper-persistent-data lvm2`
    2) docker 설치를 위한 repository 추가  
    `$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`
    3) 레포지토리 추가확인  
    `$ yum repolist`
    4) Docker 설치  
    `$ yum -y install docker-ce docker-ce-cli containerd.io`
    - docker-ce : Docker 엔진
    - docker-ce-cli : 커맨드라인 도구
    - containerd.io : 컨테이너 실행 도구
    5) Docker 서비스 시작  
    `$ sudo systemctl start docker.service`
    `$ sudo systemctl enable docker.service`
    6) docker 사용자 권한 추가  
    `$ sudo usermod -aG docker $USER`
    => 현재 쉘에 로그인되어 있는 사용자($USER)의 보조그룹으로 docker 추가

---
## 도커 이미지 빌드 원리와 Overayfs
* https://www.44bits.io/ko/post/how-docker-image-work
    - 추천 정보

---
### docker 명령어
* `docker serarch <검색어>`  
* `docker pull <repository>:<tag>`  
* `docker create <option> --name <name> <image-file>` 
* `docker images` or `docker image ls` 
* `docker image rm` or `docker rmi`
    - `docker system prune`
    - `docker rm $(docker ps -aq)`
* `docker start <option> <container-name>`  
* `docker stop <container-name>`  
* `docker run <oprion> <image-file> <container-commend>`  
* _**`docker history <image or container>`**_
* _**`docker inspect <image or container>`**_
* _**`docker commit $(docker ps -alq) ubuntu:git`**_
    - 실행 중인 컨테이너를 이미지 파일로 만듦
    - 주요 옵션
    ```
    --author, -a 	: 작성자를 지정 Ex)Hong ShiHo<ShiHo@hong.seoul>  
    --message, -m 	: 메시지 지정  
    --change, -c 	: 커미트 시 Dockerfile 명령을 지정  
    --pause, -p		: 컨테이너를 일시정지하고 커미트
    ```
* _**`docker save <option> <image>`**_
    - `docker image save -o export.tar nginx`
    - 이미지를 아카이브 파일로 복사
* _**`docker load <option> <아카이브 파일>`**_
    -  `docker image load -i export.tar `

* `docker run [옵션] --name [컨테이너 이름] [이미지 이름] [실행명령]`
* `docker stats`
    - 전체 구동중인 컨테이너의 상태 확인
    - -a : 구동중이지 않은 컨테이너의 상태 포함
    - --no-stream : 지속해서 상태정보를 갱신하지 않고 한번만
    - cpu 사용률 정보의 100%는 cpu 한개를 최대한 사용하고 있다는 의미 (CPU 개수에 따라 사용률이 더 올라갈 수 있음)  
* `docker restart [컨테이너명]`
* `docker rm [컨테이너명]`
    - -f : 구동중인 컨테이너도 강제 삭제
* `docker run -e [환경변수설정]`  
* `docker run --cpus [CPU사용률을 숫자로]`
    - cpu 사용률 제한
    - 사용률 1=100%
    - CPU 개수에 따라 최대 사용률 변화 
    - 기본값은 1
* `docker run --memory [메모리용량]`
    - 컨테이너 생성시 메모리 용량 제한
    - 기본값은 무제한 (호스트의 메모리 용량)
* `docker update [사양변경옵션]`
    - 구동중인 컨테이너의 CPU, 메모리 등 제한조건 변경가능
    - 메모리 제한을 기본값(무제한)으로 설정한 컨테이너의 경우 --memory-swap 옵션을 -1로 설정하여야 메모리 제한 변경 가능  
* `docker attach [컨테이너명]`
* `docker exec <container> <command>` 
* `docker top <컨테이너 이름, ID> <ps 옵션>`
* __*`docker logs`*__
* `docker cp`
* `docker diff`
    - 기준 이미지와 컨테이너 간 파일 변화 비교
        + A : 추가된 파일
        + C : 변경된 파일
        + D : 지워진 파일

##### docker save, load & docker export, import 비교하기
참고 : https://waspro.tistory.com/584

---
## Docker Volume
* 기본적으로 컨테이너는 내부적으로만 데이터를 저장
* 컨테이너가 삭제될 경우 내부 데이터도 함께 삭제
    -Stateless

컨테이너에서 저장한 데이터를 영구보관하기 위해서는 별도의 위치에 저장 필요

1. Bind mount
* 호스트의 경로를 지정하여 컨테이너로 마운트
* 호스트의 파일에 변화를 줄 수 있으므로 사용에 주의 필요  
`$ docker run ... -v [호스트경로]:[마운트위치]...`

2. Volume
* 데이터 저장용 볼륨을 따로 생성하여 저장  
`$ docker volume create [볼륨명]`
`$ docker run .... -v [볼륨명]:[마운트위치]`

---
## Docker Network

1. Bridge Network
* 사설 네트워크를 생성하여 내부 컨테이너 통신 및 NAPT를 통한 외부 통신이 가능한 네트워크
* NAPT
  - Network Address Port Tanslation
  - 호스트OS가 보유하고 있는 공용 IP를 컨테이너가 통신할 때 공유하기 위한 방법
    + 통신이 브리지를 통과할 때 IP, Port 등의 정보를 변경시킴

#### 네트워크 생성
docker network create -subnet [서브넷정보] --gateway [게이트웨이정보] [네트워크이름]

2. Host Network
* 원래 호스트의 NIC 정보를 공유하는 네트워크
* 호스트가 사용중인 포트를 함께 사용할 경우 비정상 동작 (80 포트 등)

3. null(none)
* 네트워크 연결이 없는 네트워크(?)
* 통신 연결이 필요없는 컨테이너에서 사용

4. Overlay Network
* Docker Swarm 등 클러스터링 등 목적으로 사용

5. macvlan Network
* 호스트의 물리적인 NIC의 네트워크 대역과 동일한 네트워크대역의 IP를 부여하여 사용
* Proimiscuous Mode 설정 필요
    - Promiscuous mode : 무차별 모드
    => MAC Address가 맞지 않는 패킷도 모두 전달
    `$ sudo ip link set [인터페이스명] promisc on`

#### 네트워크 생성
* `docker network create -d macvlan -subnet [서브넷정보] --gateway [게이트웨이정보] -o [호스트인터페이스명] [네트워크이름]`


### NIC에 PRIMISC 모드 활성
* Promiscuous mode : 무차별 모드
    - MAC Address가 맞지 않아도 전달
* <span style="color:red">`ip link set enp0s3 promisc on`</span>

---
## 컨테이너 간 연결

1. link
* `docker run .... --link [호스트명] [이미지 이름]`
    - 컨테이너의 /etc/hosts 파일을 수정하여 이름으로 통신 가능

2. 포트포워딩
* 호스트의 특정 포트로 접근시 컨테이너의 지정한 포트로 연결
    - `$ docker run .... -p [호스트포트]:[컨테이너포트]`

=======================================
### 이미지 태그
`$ docker tag [기존이미지] [새로만들이미지]`
* 태그를 붙일 경우 기존 이미지와 동일한 항목 생성
* 새롭게 복사되는 것은 아님 - 하드링크와 비슷함

`이미지 업로드`
* docker login : docker hub 로그인
* docker push [이미지정보] : 이미지 업로드

#### 업로드 이미지명 규칙
* 계정명/이미지명:태그


=======================================

### 컨테이너를 이미지로 저장
* `docker commit [컨테이너명] [이미지정보]`
    - 지정한 컨테이너를 지정한 이름의 이미지로 저장

* `docker export`
    - 지정한 컨테이너를 하나의 아카이브파일(tart)로 저장

#### save와 차이점
* save는 이미지를 저장 / export 는 컨테이너를 저장
* save는 계층 정보를 포함 / export는 단일 계층으로 통합

---
## Dockerfile
* 이미지 제작 자동화 (IaC)
    - 지정된 지시어를 사용하여 컨테이너 실행

#### 지시어
지시어|설명
---|---
FROM | 기본 이미지 지정
MAINTAINER | 이미지 작성자 정보
RUN | 이미지 작성시 실행할 내용
CMD | 이미지로부터 만들어진 컨테이너 구동 시 실행
ENTRYPOINT | 이미지로부터 만들어진 컨테이너 구동 시 실행
EXPOSE | 컨테이너 포트 열기
COPY | 파일 복사
VOLUME | 볼륨(데이터 저장소) 지정
* ENTRYPOINT 와 CMD 동시 사용시, ENTRYPOINT는 명령어, CMD는 명령어의 인자 형태로 사용됨.
* ENTRYPOINT는 변경불가능하며, CMD는 docker run 실행시 전달하는 파라미터로 변경 가능
 
 * VOLUME
    - 특정 볼륨을 지정하여 연결은 불가
    - 특정 볼륨을 사용하고자 할 경우에는 Dockerfile이 아닌 docker run 명령어 실행의 -v 옵션을 사용하여야 함

#### Dockerfile로 부터 이미지 작성
`$ docker build -t [생성할이미지이름] [Dockerfile경로]`

---
## 로컬 도커 레지스트리 사용
* 도커 허브와 같은 공용 레지스트리에 업로드하기 꺼려지는 이미지를 업로드하기 위하여 사용 (중요 데이터 등)

### Registry 컨테이너 사용
* Docker hub에서 다운로드 가능한 registry 이미지를 사용
* 레지스트리 컨테이너의 5000번 포트를 사용하여 이미지 업/다운로드
* 실행방법  
* `$ docker run -d --name myregistry -p 5000:5000 registry:latest`
    - 이미지 업로드방법 : 이미지를 로컬레지스트리에 업로드할 수 있는 형태로 태그 생성  
* `$ docker tag [원본이미지명] localhost:5000/[이미지명]:[태그명]`
    - 업로드
* `$ docker push localhost:5000/[이미지명]:[태그명]`  

=========================================

### Docker Compose 설치
`sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

`sudo chmod +x /usr/local/bin/docker-compose`

혹시 실행 정상적으로 안되시는 분은  
`rm /usr/local/bin/docker-compose`  
실행 후 다시 다운로드 / 권한변경 해 주시기 바랍니다.

### harbor 설치  
`wget https://github.com/goharbor/harbor/releases/download/v1.10.1/harbor-offline-installer-v1.10.1.tgz`  

`tar zxf harbor-offline-installer-v1.10.1.tgz`

`cd harbor`

`vi harbor.yml`
* hostname 수정
* https 관련 항목 삭제

#### 파일 생성
```bash
sudo vi /etc/docker/daemon.json
{
"insecure-registries" : ["192.168.56.102"]
}
```

#### docker 서비스 재시작  
`systemctl restart docker`

#### insecure-registries 설정 확인  
`docker info`

#### ./install 실행
`sudo -E env "PATH=$PATH" ./install.sh`

```
ERROR: for nginx  Cannot start service proxy: driver failed programming external connectivity on 
Creating harbor-jobservice ... done userland proxy: listen tcp 0.0.0.0:80: bind: address already in use
=> 80 포트 사용중이라 발생한 문제
=> systemctl stop httpd
```
