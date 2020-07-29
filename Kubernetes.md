# Kubernetes
* 컨테이너 오케스트레이션 도구

* 실습환경
    - kube-master1
    - kube-node1
    - kube-node2
    - kube-node3

* 설치과정을 간소화
    - vagrant : VirtualBox 등 가상화 이미지 배포 자동화
    - kubespray : Kubernetes 설치 간소화

==============
### vagrant 설치 후

Vagrantfile 지정된 위치에 복사 (C:\Vagrant)

다음 명령 실행하여 플러그인 설치  
`vagrant plugin install vagrant-hostmanager`  
`vagrant plugin install vagrant-disksize`

VM 설치에 사용할 VM 이미지 다운로드  
`vagrant box add ubuntu/bionic64`  

============================
### vagrant를 통한 VM 설치

`vagrant up`  
* 현재 Vagrantfile 내용을 참고하여 시스템을 구동
* VM이 생성되지 않았을 경우 Vagrantfile 설정에 따라 VM 생성

kube-master1 : 쿠버네티스 마스터. 192.168.56.11
kube-node1~3 : 쿠버네티스 노드. 192.168.56.21~23

#### 네트워크 인터페이스 확인
* VM - 설정  
    - 네트워크어댑터1 : NAT (10.0.2...)  
    - 네트워크어댑터2 : 호스트 전용 네트워크 (192.168.56...)

=============================
### Vagrant로 설치된 시스템 SSH 접근
1) vagrant 에서 제공되는 SSH 기능 사용
`vagrant ssh [시스템이름]`

2) 별도의 SSH 클라이언트 사용
`ssh vagrant@192.168.56.11 (마스터 서버 연결)`
    - vagrant 계정의 암호 : vagrant

=============================
### master에서 각 노드에 연결할 수 있도록 SSH 키 복사
`ssh-keygen`  
    - SSH 키 기반 인증에 필요한 키 생성  
`ssh-copy-id vagrant@[노드이름]`  
    - 위에서 생성한 키를 각 노드에 배포

==============================
### 패키지 설치 (모든 작업은 마스터에서, 계정은 vagrant로)

1) 필요 패키지 설치를 위한 기본  
`sudo apt update`  
`sudo apt install python3 python3-pip git`
    - 패키지 정보 업데이트 후 python3, pip, git 설치

2) kubespray 다운로드  
`cd`  
`git clone --single-branch --branch v2.12.3 https://github.com/kubernetes-sigs/kubespray.git`  
`cd kubespray`  

3) kubespray 실행을 위한 필요 패키지 설치  
`sudo pip3 install -r requirements.txt`  

=================================
### 인벤토리 파일 설정  
* 인벤토리 파일 : Ansible 에서 사용하는 대상 호스트 정보
* Ansible : SSH, Python을 사용하여 다수의 호스트 관리

1) 인벤토리 샘플 복사  
`cp -rfp inventory/sample inventory/mycluster`  

2) 샘플 인벤토리 수정  
`vi inventory/mycluster/inventory.ini`  
=> 이 파일에 공유폴더의 inventory.txt 파일의 내용을 입력

3) 인벤토리 설정 후 테스트  
`ansible all -i inventory/mycluster/inventory.ini -m ping`  
    - 각 노드의 ping/pong 요청/응답 상태 확인
    - 이상 발생시 /etc/hosts 파일 확인

4) 패키지 리포지토리 업데이트
`ansible all -i inventory/mycluster/inventory.ini
 -m apt -a 'update_cache=yes' --become`

======================================  
5) kubespray 설정 파일 수정 - 필요한 모듈 추가
```bash
vi inventory/mycluster/group_vars/k8s-cluster/addons.yml
  metrics_server_enabled: true
  ingress_nginx_enabled: true
```

=====================================  
6) ansible 플레이북 실행 - kubespray를 통한 kubenetes 설치
    - 플레이북 : 단일 명령이 아닌, 실행할 작업의 목록  
`ansible-playbook -i inventory/mycluster/inventory.ini cluster.yml  --become`  

======================================
### 플레이북을 통한 설치 완료 후 작업
* 자격증명 복사 : root 계정에 복사된 자격증명을 vagrant로 복사
    - vagrant 사용자로 수행  
```bash
cd
mkdir ~/.kube
sudo cp ~root/.kube/config ~/.kube
sudo chown vagrant:vagrant -R ~/.kube
```

====================================
### bash completion 설정
* 리눅스 패키지인 bash_completion은 명령어 및 보조명령, 옵션 등의 자동완성을 지원함  

`kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl`  
    - kubectl 명령 실행시 필요한 bash completion 정보를 설정파일로 저장  
`exec bash`  
    - 새로 추가한 bash completion 정보를 현재 쉘에 적용

---
## 쿠버네티스 기본 
* 기본 명령어 : kubectl

### 쿠버네티스 구성상태 확인
`kubectl cluster-info` : 쿠버네티스 구성요소 상태 확인
`kubectl get nodes` : 쿠버네티스에 등록된 노드 확인

### 쿠버네티스 API
* 쿠버네티스에서 사용하는 오브젝트는 API를 사용하여 동작
* 버전 구분 : 알파 / 베타 / 안정화

## YAML
* YAML Ain't Markup Language / Yet Another Markup Language
* 구조화된 데이터 정의 문서 양식
* 들여쓰기로 단계를 구분 (들여쓰기 규칙 엄수) - 일반적으로 공백2칸

#### vi 편집기에서 YAML 문서 작성시 편의 설정  
* ~/.vimrc 파일 생성 후 다음 내용 추가
```vim
syntax on
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab autoindent
```
(YAML 파일 작성시 - 탭 사용시 공백 2칸으로 대체, 탭으로 들여쓰기 후 엔터로 다음줄 작성시 자동으로 들여쓰기 적용, 탭 위치에서 백스페이스 입력시 탭 크기만큼 삭제)

---
## 쿠버네티스 오브젝트 관리

오브젝트 생성 방법
1) 명령형 명령어
    - 명령어를 통해 오브젝트 작성 및 제어
2) 명령형 오브젝트 구성
    - YAML/JSON 형태의 파일로 오브젝트를 정의
    - 오브젝트 정의 파일을 사용하여 오브젝트 관리
3) 선언형 오브젝트 구성
    - 특정 디렉토리에 오브젝트 파일을 배치
    - 디렉토리를 인수로 오브젝트 관리


=======================================
### 명령형 명령 사용 애플리케이션 사용 예 (교재 실습 참고)

1) 컨트롤러 생성
* 레플리케이션(Replication) 컨트롤러 
    - 파드(Pods)의 기본 동작 규칙을 설정한 오브젝트
    - 컨트롤러 규칙에 따라 파드를 자동으로 관리  
* `kubectl run myweb-1st-app --image=c1t1d0s7/myweb --port=8080 --generator=run/v1`  
    - ReplicationController 타입의 컨트롤러 생성

#### 컨트롤러(Controller)
* 배치된 리소스의 결과로 실제 작업을 수행하는 활성된 쿠버네티스 컴포넌트

2) 서비스 구성  
`kubectl expose relplicationcontroller myweb-1st-app --type=LoadBalancer --name myweb-svc`  
    - LoadBalance 를 통해 앞에서 생성한 컨트롤러를 서비스하도록 연결

* 확인 및 테스트  
`kubectl get service`   
    - 생성한 서비스가 파드의 포트를 어느 포트로 서비스하고 있는지 확인 후 연결 테스트
    - ex) curl http://192.168.56.11:30123

3) 스케일링
* ReplicationController는 복제 개수를 지정하여 파드를 다수 관리  
`kubectl scale replicationcontroller myweb-1st-app --replicas=3`  

* pods 한개 삭제  
`kubectl delete pods [파드명]`  

4) 서비스 및 컨트롤러 정리  
`kubectl delete replicationcontroller myweb-1st-app`  
`kubectl delete service myweb-svc`  

---
### vagrant로 구동한 시스템 일괄 통제

- 전체 종료 : vagrant halt
- 전체 일시정지 : vagrant suspend
- 일시정지 후 전체 재시작 : vagrant resume

