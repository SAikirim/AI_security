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
## bash completion 설정!
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
* '-' : 배열의 의미(리스트)

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

#### 쿠버네티스 오브젝트
* 클러스터의 상태를 나타내기 위한 개체

=======================================
### 명령형 명령 사용 애플리케이션 사용 예 (교재 실습 참고)

1) 컨트롤러 생성
* 레플리케이션(Replication) 컨트롤러 
    - 파드(Pods)의 기본 동작 규칙을 설정한 오브젝트
    - 컨트롤러 규칙에 따라 파드를 자동으로 관리  
* `kubectl run myweb-1st-app --image=c1t1d0s7/myweb --port=8080 --generator=run/v1`  
    - ReplicationController 타입의 컨트롤러 생성

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
## 오브젝트 리소스 문서 확인 명령  
`kubectl explain [리소스]`
```bash
kubectl explain pod
kubectl explain pod.spec
kubectl explain pod.spec.containers
kubectl explain pod.spec.containers.name
kubectl explain pod.spec.containers.image
kubectl explain pod.spec recursive
```

---
### vagrant로 구동한 시스템 일괄 통제

- 전체 종료 : vagrant halt
- 전체 일시정지 : vagrant suspend
- 일시정지 후 전체 재시작 : vagrant resume

---
## 파드(pod,pods)
* 컨테이너의 모음
* 파드 별로 IP가 할당
* 모든 컨테이너가 파드의 IP를 공유함
* 자원을 공유 (볼륨)
* 파드 내에 들어가는 컨테이너는 단일 노드에 위치

======================================================
### 파드 구성 YAML 파일
```yaml
apiVersion: 오브젝트 사용시 필요한 API 버전정보
kind: 오브젝트의 종류 (Pod)
metadata: 파드의 기본 속성 (이름, 레이블, 네임스페이스 등)
  name: 파드 이름
  namespace: 파드를 배치할 네임스페이스 지정
  labels: 파드를 식별하기 위한 레이블 (키-값의 쌍)
spec: 파드의 구체적인 구성 설정 (파드 내 컨테이너 설정)
  containers: 컨테이너 구체적인 설정 (복수의 컨테이너 기술 가능)
    image: 기본이 되는 이미지
    name : 컨테이너 이름 (파드 이름과 다름)
    ports: 네트워크를 통해 서비스를 제공하는 컨테이너의 정보
```

---
### 레이블
* 쿠버네티스에서 레이블은 오브젝트를 식별할 수 있는 중요 항목
    - 레이블은 반드시 키-값 형태로 작성
    - 키는 영문자,숫자,일부특수문자(- _ .)만 사용하여 63자 이내로 작성

* 전체 파드 레이블 정보 확인  
`$ kubectl get pods --show-labels`  
`$ kubectl get pods -L [키],[키]....`  

* 특정 파드의 레이블 정보 확인  
`$ kubectl get pods [파드명] -o yaml`  
`$ kubectl describe [파드명]`  

==========================================
### 셀렉터
- 레이블의 키/값을 기준으로 오브젝트를 선택
- 키의 존재 유무 / 키=값의 일치여부

#### 셀렉터 유형
- = : 균등 기반 셀렉터
- in, notin : 집합기반 셀렉터
- ! : not의 의미를 가짐

ex) 
```
app		// app 키를 가진 오브젝트
app=myapp	// app 키에 myapp 값이 들어있는 오브젝트
!app		// app 키를 가지고있지 않은 오브젝트
app!=myapp	// app 키가 있으며, 키의 값이 myapp이 아닌 오브젝트
app in (myapp, yourapp)	// app 키가 있으며, 값이 myapp, yourapp 중 하나인 오브젝트
app notin (myapp, yourapp)	// app 키가 있으며, 값이 myapp, yourapp 중 하나에 해당하지 않는 오브젝트
```
=========================================
### 어노테이션 Annotation (주석)
- 파드에 대한 부가적인 설명
- 레이블과 달리 오브젝트 식별용도로 사용하지는 않음
- 키/값 구성으로 작성하여야 함

#### pod.metadata.annotations 항목에 작성하거나  
`$ kubectl annotate pod [파드명] [키]=[값]` 형태로 작성

==========================================
### 네임스페이스
* 독립적으로 작업할 수 있는 이름 공간
* 리눅스에서 컨테이너 격리를 위해 활용하는 네임스페이스와는 다름
* 별도로 지정하지 않을 경우 기본 네임스페이스는 default
* 기본으로 생성되어 있는 네임스페이스
	- kube-system : 쿠버네티스 구성을 위해 작성된 네임스페이스
	- kube-public : 모든 사용자가 읽기 가능한 네임스페이스. 미사용
	- kube-node-lease: 쿠버네티스 노드의 가용성 체크를 위한 용도
	- default : 기본 네임스페이스
* 네임스페이스는 오브젝트를 논리적으로 격리함
    - 네임스페이스가 다르면 같은 이름의 오브젝트도 생성 가능

#### 네임스페이스 지정
- 오브젝트 생성시 -n / --namespace 옵션으로 지정
- YAML 파일 내 metadata.namespace 부분에 작성

==========================================
### 컨트롤러(Controller)
* 배치된 리소스의 결과로 실제 작업을 수행하는 활성된 쿠버네티스 컴포넌트
* 파드의 동작 규칙을 정의함
* 다양한 유형이 있음 
    - ReplicationController, ReplicaSet, DaemonSet, Job, CronJob

==========================================
### 라이브니스 프로브(Liveness Probe)
- 기본적으로 쿠버네티스는 파드가 구동하고 있는지 아닌지 만을 확인함
- 정상적으로 서비스를 제공하지 못하는 파드의 경우도 구동되고 있으면 RUNNING
- 파드의 동작상태를 확인하기 위하여 사용하는 것이 `Liveness Probe`

#### Liveness Probe 유형
- httpGet : 웹서비스를 제공하는 파드의 경우, 웹 요청의 응답으로 확인
- tcpSocket : 네트워크 특정 포트 연결 시도의 응답으로 확인
- exec : 컨테이너에 명령을 실행하고 실행결과로 확인

#### 작성방식
* pod.spec.containers.livenessProbe 항목에 작성

#### 동작방식
- Liveness Probe는 설정된 주기에 따라 동작상태를 확인
- 동작이 비정상일 경우 컨테이너를 재시작
- 컨테이너 재시작 후 비정상동작이 기준치 이상 발생할 경우, 해당 파드를 종료

==========================================
### 레플리케이션 콘트롤러 (ReplicationController)
- apps/v1 API 버전 사용
- 지정된 개수만큼의 복제본 파드를 유지시키는 용도로 사용
	파드 부족시 : 파드 복제 생성
	파드 과다시 : 파드 제거
- 파드 개수를 확인하는 기준 : 레이블 셀렉터
- 파드 복제시 템플릿 사용 : 파드 작성요령과 유사함 (metadata.name은 뺌)

#### 복제 개수 지정 : spec.replicas

#### 셀렉터 : spec.selector
- 키/값을 모두 사용하여야 함.
- 단일 항목만 적용 가능

---
## 레플리카셋 (ReplicaSet)
* apps/v1 API 버전 사용
* 레플리케이션 콘트롤러와 동일한 기능이나, 셀렉터 자유도가 높음
	- 다중 레이블 지원
	- 키 존재 유무로만 식별 가능

### 레플리카셋 셀렉터 유형
* spec.selector.matchLabels : 레플리케이션 콘트롤러와 동일한 구성
* spec.selector.matchExpressions : 다양한 레이블 선택옵션 사용가능  
    ```
	key: [키]
	operator: <In | NotIn | Exist | DoesNotExist >
	values:
	- 값1
	- 값2
	// In / NotIn : values 항목 필요
	// Exist / DoesNotExist : values 항목 불필요 (키 존재여부만 확인)
    ```

Ex) 레플리카셋, matchExpression(mynapp-rs-exp.yml)  
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: mynapp-rs-exp
spec:
  replicas: 3
  selector:
    matchExpressions:
    - key: app
      operator: In
      values: 
      - mynapp-rs-exp
  template:
    metadata:
      labels:
        app: mynapp-rs-exp
    spec:
      containers:
      - name: mynapp
        image: c1t1d0s7/myweb
        ports:
        - containerPort: 8080
```

=========================================
### 데몬셋 (DaemonSet)
- apps/v1 API 버전 사용
- 복제 개수가 아닌, 모든 노드 또는 지정된 노드마다 1개씩 생성되도록 구성가능한 컨트롤러

#### 노드셀렉터 : 데몬셋이 배포될 대상 지정. 각 노드의 레이블을 사용

`spec.template.nodeSelector`
- 셀렉터 정보는 레이블과 같이 '키: 값' 형태로 작성
ex) 
```yaml
    nodeSelector:
      node: Development
```

노드 레이블 확인  
`$ kubectl get nodes --show-labels`

노드 레이블 생성  
`$ kubectl label nodes [노드이름] 키=값`

노드 레이블 값 제거  
`$ kubectl label nodes [노드이름] 키='' --overwrite`

노드 레이블 키 제거  
`$ kubectl label nodes [노드이름] 키-`

===========================================
### 잡(Job) 컨트롤러
- batch/v1 API 버전 사용
- 일회성 작업 지시를 위하여 사용
- 실행회수를 지정함 (completion)
- 동시실행회수를 지정가능 - 병렬실행 (parallelism)
- 작업마다 새로운 파드를 생성하고, 작업이 완료된 파드는 종료

#### Job
* 다중 /병렬 잡 컨트롤러
`spec.completions: 3`
    - 파드를 하나씩 만들어, 완료되면 다시 포드를 만들어 진행
* `spec.parallelism: 3`
    - 옵션을 주면 동시에 진행
    - 병렬 수행

Ex) Job Controller 예제 파일(mynapp-job.yml)  
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: mynapp-job
spec:
  # completions: 3      # 작업회수 지정
  # parallelism: 3      # 동시실행개수 지정
  template:
    metadata:
      labels:
        app: mynapp-job
    spec:
      restartPolicy: OnFailure
      containers:
      - name: mynapp
        image: busybox
        command: ["sleep","60"]
```
==========================
### 크론잡 CronJob
- batch/v1beta1 API 버전 사용
- 단일 실행이 아닌 주기적인 실행을 제공하는 컨트롤러
- 기존 crontab 작성과 동일한 작성방법 (분 시 일 월 요일)

Ex) 크론잡 예제 파일(mynapp-cronjob.yml) 
```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: mynapp-cronjob
spec:
  schedule: "*/2 * * * *"
  jobTemplate:
    spec:
      template:
        metadata:
          labels:
            app: mynapp-cronjob
        spec:
          restartPolicy: OnFailure
          containers:
          - name: mynapp
            image: busybox
            command: ["sleep","60"]
```
  
---
---
## 서비스
- 컨트롤러에 의해 생성된 파드는 생성시 임의의 IP주소 할당
- 파드는 유연하게 동작하므로, 생성/삭제가 빈번하게 발생함
- 관리자는 직접 파드의 정보에서 주소를 확인할 수 있으나, 일반적인 클라이언트는 각 파드의 주소를 확인할 수 없음
- 서비스는 컨트롤러에 의해 구성된 임의의 파드 주소 대신 고정된 진입점을 생성해 주는 오브젝트
* __*외부와의 통신하기 위한 리소스*__

=================================
### 클러스터 내부 서비스
- 클러스터 내부의 다른 오브젝트에서 접근 가능한 서비스
- 외부 진입점은 제공하지 않음
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mynapp-svc
spec:
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: mynapp-rs
```
* service.spec.ports : 서비스에서 제공할 포트의 목록 (다수의 포트 서비스 가능)
	- port: 서비스에서 오픈할 포트
	- targetPort: 컨트롤러의 파드로 연결할 포트 (파드가 열고있는 포트)

### 엔드포인트  
`$ kubectl get endpoints`  
- 서비스에서 연결한 컨트롤러로 접근시 실제 접근하는 각 파드의 주소와 포트번호 정보

#### 엔드포인트 컨트롤러
* 서비스가 추가/갱신 또는 포드 추가/갱신/삭제될 때 서비스의 포드 셀렉터와 매칭되는 포드를 선택하고 해당 IP와 포트를 엔드포인트 리소스에 추가함

=====================================
### 포트 이름 참조
- 파드의 컨테이너 설정에서 포트에 이름을 붙임
- 서비스의 targetPort에서 포트 이름을 사용가능
- 파드의 포트가 변경되더라도 서비스의 포트 변경이 불필요해짐

=====================================
### 서비스 탐색 - DNS
- 쿠버네티스 클러스터 내 오브젝트들은 이름으로 주소 획득 가능

coredns : 쿠버네티스와 함께 설치되는 DNS 기능

#### 서비스 탐색방법
1) 환경변수를 사용
  - 컨테이너 내부 환경변수에 각 호스트의 정보를 입력
  - 쿠버네티스는 클러스터 구성에 필요한 정보를 환경변수로 사용중
  - env
2) DNS 서비스 이용
  - 쿠버네티스 클러스터 내 DNS 서비스를 이용하여 탐색
  - NodeLocal DNS Cache : 모든 오브젝트에 대한 탐색이 coredns로 집중되는 것을 예방하기 위하여 요청에 대한 캐시를 노드마다 관리

##### 쿠버네티스 서비스 리소스의 FQDN  
`[서비스이름].[네임스페이스].svc.cluster.local`  
ex) mynapp-svc.default.svc.cluster.local

====================================

클러스터 외부 서비스
- 클러스터 내부가 아닌 외부로 연결되는 네트워크 제공을 위한 서비스

NodePort
- 각 노드의 포트를 사용하여 노드 내 파드의 포트를 연결
- 클러스터 전체 노드가 공유
- 30000~32767 포트 범위 내 사용가능

LoadBalancer
- 로드밸런서를 통해 외부 IP를 할당받아 External-IP로 사용
- 실습환경에서는 MetalLB 로드밸런서를 설치하여 실습 가능

---
## 로그 밸런서 설치(kubespray)
* MetalLB 설치

1. kubespry 위치로 이동  
`$ cd ~/kubespray`  

2. 설정파일 수정  
`$ vi inventory/mycluster/group_vars/k8s-cluster/k8s-cluster.yml`  
* kube_proxy_strict_arp: false
  - false => true 변경

3. 로드밸런서 할당 IP 범위 변경  
`vi contrib/metallb/roles/provision/defaults/main.yml`  
* ip_range: "192.168.56.200-192.168.56.220"

4. 설치 - Ansible  
`ansible-playbook -i inventory/mycluster/inventory.ini contrib/metallb/metallb.yml --become`

========================================
### 인그레스 
- Nginx Ingress 컨트롤러를 사용하여 웹 요청을 전달
- 전달하기 위해 판단하는 기준 : 호스트 / 경로

#### 다중경로 인그레스
- 하나의 인그레스로 다수의 서비스를 연결
- 호스트 / 경로 정보를 배열 형태로 입력

========================================
### 레디니스 프로브
- 라이브니스 프로브와 유사한 동작방식
- 파드의 재시작 등에 관여하지 않으나, 준비상태 정보를 변경
- 일시적으로 다른 작업 등으로 서비스를 할 수 없는 상황일 경우 준비 상태를 해제시켜 서비스에서 제외 (Endpoints 에서 제외됨)

========================================
### 헤드리스 서비스
- 서비스가 내부 / 외부의 IP를 할당받을 경우 공개된 IP를 통해 서비스를 대상 파드로 전달함
- 외부에서는 서비스가 전달하는 파드의 IP 정보를 인식할 수 없음
- 특정 파드와 연결이 필요한 경우에 서비스를 통해 연결하면 라운드로빈 방식으로 연결되어 다른 파드로 연결될 수 있음
- 헤드리스 서비스는 서비스 형태로 생성되어 서비스에 대한 주소 조회를 지원하지만, 서비스 자신이 IP를 가지지 않으므로 엔드포인트 파드 정보를 DNS를 통해 전달함
- 클라이언트는 파드 주소 정보를 직접 확인하고 지정한 파드로 연결

---
## 스토리지
- 파드는 기본적으로 Stateless로 데이터를 유지하지 않음
- 데이터 유지가 필요한 경우 별도의 볼륨 등을 사용하여 데이터를 저장

### 볼륨 유형
1) emptyDir : 파드 내에서만 유효한 임시 저장공간
2) hostPath : 파드가 존재하는 노드의 특정 경로 공유
3) PersistentVolume/PersistentVolumeClain : 별도의 저장소 공간을 PV로 생성하고, PVC로 PV와 연결 구성
4) 특수 볼륨 : ConfigMap, Secret
    - '저장소'같은 느낌으로 사용하지 않음 

========================================
#### EmptyDir
- 파드 생성시 컨테이너와 함께 생성
- 파드 내 컨테이너들이 공유 가능

* 선언
```yaml
volumes:
  - name : [볼륨명]
    emptyDir: {}
```
* 사용
```yaml
volumeMounts:
  - name: [볼륨명]
    mountPath: [마운트할 위치]
```

========================================
#### HostPath
* 호스트의 특정 경로를 파드에서 공유
* 파드가 존재하는 노드의 경로만 사용가능
  - ex) Replicaset에 의해 여러 노드에 배포된 각 파드가 특정 노드에 있는 경로를 hostpath로 공유하는 것은 불가능함

* 선언
```
volumes:
  - name : [볼륨명]
    hostPath:
      type: [종류]
      path: [공유할 경로]
```
* type유형
  - DirectoryOrCreate : 디렉토리 / 없으면 만들어줌
  - Directory : 디렉토리 (없으면 에러)
  - FileOrCreate : 파일 / 없으면 만들어줌
  - File : 파일 (없으면 에러)

========================================
### 애플리케이션 사용자화
- 파드에서 구동되는 어플리케이션에 대한 사용자 설정 반영 방법

#### 사용자화 방법
1) args (CMD)
2) 환경변수
3) 컨피그맵
4) 시크릿

========================================
#### args를 사용한 사용자화
- 컨테이너 오브젝트 생성시 containers.args 항목을 통해 값 전달

#### 환경변수를 사용한 사용자화
- 컨테이너 오브젝트 생성시 containers.env 항목을 통해 값 전달

---
### ConfigMap
- 간단한 변수, 설정파일의 값 등을 키/값 쌍 형태로 저장하는 저장소 오브젝트
- 값을 불러오거나 볼륨 마운트 형태로 사용

#### 생성방법  
`$ kubectl create configmap [이름] --from-literal=[키]=[값]`
- 키 값을 직접 입력  
`$ kubectl create configmap [이름] --from-file=[파일명]`
- 파일명이 키 / 파일내용이 값  
`$ kubectl create configmap [이름] --from-file=[키]=[파일명]`  
- 지정한 키에 파일 내용을 값으로 저장

#### 컨피그맵 값 읽어오기
```yaml
valueFrom:
  configMapKeyRef:
    name: [컨피그맵 이름]
    key: [요청할 키]
```
#### 컨피그맵 파일로 마운트
```yaml
volumes:
- name: [볼륨 이름]
  configMap:
    name: [컨피그맵 이름]
```

======================================
### 레플리케이션 콘트롤러의 롤링 업데이트
- 레플리케이션 콘트롤러도 롤링 업데이트를 지원하나 문제점이 있음
- kubectl 클라이언트 프로그램에 의해 개별적으로 업데이트를 수행 : 프로그램이 중단되거나 연결 중단시 업데이트 중단

---
## 디플로이먼트
- 레플리카셋과 유사한 오브젝트
- 롤링 업데이트를 지원함
- 업데이트 작업 추적 가능 : --record 옵션 사용시
- 롤백 기능 지원

---
## 스테이트풀셋
- Stateless한 파드의 특성이 문제가 되는 경우 사용
- 파드 이름 : 컨트롤러 이름-랜덤문자열
- IP 주소 변경 : 파드 생성시 새로운 IP 할당
- 저장소 연결 문제 : 동일 템플릿의 파드가 PV 연결시 PVC 중복으로 에러

### 스테이트풀셋 구성시
- 파드이름 고정 : [이름]-0, [이름]-1, [이름]-2....
- IP 고정 : 파드 교체시 이전 파드와 동일한 IP 사용
- 템플릿 내 개별 저장소 설정 가능
- 헤드리스 서비스 필요 

======================================
## 오토스케일링
- 레플리케이션 컨트롤러, 레플리카셋의 고정된 설정이 아니라, 현재 상태에 따라 복제본의 개수 조정
- HorizontalPodAutoscaler(HPA) 오브젝트 사용

### 설정값
request : 최소한 요구되는 리소스
limit : 최대 사용가능한 리소스

사용 예
* cpu : 100m
  - miliCPU : CPU 사용량 0.1%
  - 100m 은 100miliCPU : 10%
* memory: 10Mi
  - Mi : 용량의 SI 단위. MiB (2^10 단위 계산)
