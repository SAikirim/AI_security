
## 퍼블릭클라우드
* aws, gcp, azure

## 국내 클라우드 
* 네이버
* 카카오
* KT

---
## 클라우드
* 필요한 만큼 자원을 클라우드 제공자에게 빌림
* 물리적 서버를 구입하는 대신, 클라우드 공급자로부터 필요한 컴퓨팅 파워, 스토리지, 데이터베이스 등을 빌려와 사용함

### 클라우드의 종류

#### 서비스 수준
* IaaS (Infrastructure as a Service)
* PaaS (Platform as a Service)
* SaaS (Sofrware as a Service)

#### 서비스 수준
* 퍼블릭 클라우드
* 프라이빗 클라우드

#### 서비스 특수성
* 범용 클라우드
* 전용 클라우드
    - 주식 전용, 천문 계산 전용

---
## AWS

* EC2 : 컴퓨터 자원 서비스(Compute engine)
    - 가상의 컴퓨터를 제공
* S3  : 스토리지 서비스
* Cloudfront : CDN
    - CDN(contents Delivery Network)
    - 사진, 미디어를 저장해서, 웹서비스 앞단에서 바로 전달하는 서비스
        + 웹서비스보다 비용과 속도면에서 장점
* IAM : 다른 계정도 자신의 서비스 이용 가능 서비스

```
인스턴트에 ssh 접속
chmod 400 key파일(pem파일)
ssh -i  test.pem ubuntu@13.124.111.34  (우분투)
ssh -i  test.pem ec2-user@13.124.111.34  (아마존 리눅스)
```

---
### S3
* 파일을 저장해서 보관해주는 서비스
    - 고장나지 않는 저장공간
    - 분산 저장되며 저장이 버전별로 관리된다.
    - 파일 서버로 사용가능
    - 정적 웹사이트 호스팅 지원

#### s3 용어
* 버켓 : 하나의 프로젝트
* 폴더 : 버켓안에 폴더가 있음
* 오프젝트 : 파일리아 보면 됨(파일 + 기타)

---
### CDN
* 캐시서버의 기능
* 전세계에 빠르게 데이터를 전달

origin(원본 웹서버) :  http://sshacker.s3-website.ap-northeast-2.amazonaws.com/


sshacker.s3-website.ap-northeast-2.amazonaws.com/admin/index.html
d20qucqwqd6cwl.cloudfront.net

---
GCP(구글 클라우드 플랫폼)

*  쥬피터 노트북 설치 실습  
    -  클라우드에서 머신러닝 개발환경을 뚝딱 만듦  
    - 클라우드에서 고사양의 컴퓨터를 저비용으로 사용가능
*  워드프레스 설치 실습  
    - 클라우드 환경에서 웹사이트를 뚝딱 만듦

* CMS(Contents Management System) : 게시판, 레이아웃, 모듈과 같은 기능을 모아둔 웹 프레임워크

---
### 코랩(colab)
* 머신러닝 개발 환경을 무료 제공

#### 명령어 사용법
`!cat /etc/issue.net`  
OS종류 확인

`!head /proc/cpuinfo`  
cpu 정보

`!head /proc/meminfo`  
메모리 정보

`!df -h`  

`!pwd`

`!ls -al`

#### 파일 업로드
```python
from google.comcolab import files
uploaded = files.upload()
```

#### 파일 다운로드
```python
from google.comcolab import files
files.download("file name")
```

---
* GCP SDK
    - 로컬에서 GCP 관리/사용 도구

 * Datalab
    - 데이터 탐색, 분석, 시각화, 머신러닝을 위한 간편한 대화형 도구

======================================
 ### 브라우저 콘솔로 접속

* Datalab 구성
```bash
$ gcloud init

1

로그인 계정선택
프로젝트 선택하고
리전선택은 no

$ datalab create test
리전 선택은 50번

$ datalab delete 인스턴스이름

$ datalab delete test
```
===========================================  
* jupyter-notebook 구성
```bash
$ gcloud init

$ gcloud compute ssh instance-1

아나콘다 설치
$$ http://repo.continuum.io/archive

$$ wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

enter
yes
enter

yes

$$ source ~/.bashrc

$$ conda install notebook

$$ jupyter notebook --generate-config

$$ nano /home/sunghoonsh34/.jupyter/jupyter_notebook_config.py

-------------------------------------
c = get_config()
c.NotebookApp.ip = '34.64.233.209'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
-------------------------------------

$$ jupyter-notebook --no-browser --ip=0.0.0.0 --port=8888

ctrl+z      # 백그라운드 실행
bg
disown -h   # 소유권 포기
```
* 실습끝났으면 인스턴스 삭제

---
## 워드프레스 설치 실습

* 웹서버 설치
```bash
$ sudo apt update
$ sudo apt install apache2
$ sudo systemctl restart apache2.service
$ sudo systemctl enable apache2.service
```

* DB 설치
```bash
$ sudo apt-get install mariadb-server mariadb-client
$ sudo systemctl restart mariadb.service
$ sudo systemctl enable mariadb.service
$ sudo mysql_secure_installation
```

* php 설치
```bash
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:ondrej/php
$ sudo apt update
$ sudo apt install php7.2 libapache2-mod-php7.2 php7.2-common php7.2-mysql php7.2-gmp php7.2-curl php7.2-intl php7.2-mbstring php7.2-xmlrpc php7.2-gd php7.2-xml php7.2-cli php7.2-zip
```

* wpuser 추가
```bash
$ sudo rm -rf /var/www/html/phpinfo.php

$ sudo mysql -u root -p1234

CREATE DATABASE wpdatabase;
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY '1234';
GRANT ALL ON wpdatabase.* TO 'wpuser'@'localhost' IDENTIFIED BY '1234' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit;
```

* wordpress 설치
```bash
$ cd /tmp
$ wget https://wordpress.org/latest.tar.gz

$ tar -xzf latest.tar.gz

$ cd wordpress/
$ cp wp-config-sample.php wp-config.php

$ vim wp-config.php
------------------
define( 'DB_NAME', 'wpdatabase' );

define( 'DB_USER', 'wpuser' );

define( 'DB_PASSWORD', '1234' );
--------------------

wordpress.org   # wdpress 암호 설정값
api.wordpress.org/secret-key/1.1/salt
============================================
define('AUTH_KEY',         'Ez+uMX^buQE*~Qu)?W(6^:FN?%w-9rI+LI}^s^s,ZQB8N/aPD@kF+L.ih-C> ,g5');
define('SECURE_AUTH_KEY',  '^Y)k]-Z|$vPmFic:T-c^@n |n),;3muXk3ez1 AdrI,=?ekV!+bG*s%k8;!KE!t$');
define('LOGGED_IN_KEY',    '>msOs=;Po4&jD3,i>)7h!FXb=Ft&!61|;e%>e)!W-J|oj]gc?NNAB`{(b;)d!raA');
define('NONCE_KEY',        'ucco&:+j$;K;4P*zN*yeS7X6>]||:rI+,(;VBh?ElUwcYj,4T|/d;JWgL#FkU9Uj');
define('AUTH_SALT',        'fb`0(Z$^wc(#; =Y.H*I)I;eWWj&M,Pr^9*#kdE4L0|Y(g2 vE8-;)]qcV3xzB#3');
define('SECURE_AUTH_SALT', ',(:9a%zmMAcW#3y&6uy;> RxA1d;c=!0CZkE@|Lj[G64JYW.iobtwHUlqH.D?>$G');
define('LOGGED_IN_SALT',   '++}uj{?J8O9*?nLmPwcQ[=BXN9Hl9FN2X&/%dMITYnGdlf{~{03J0_N*/2V.}I|`');
define('NONCE_SALT',       'ifP$,:gE3pkq%+:DShUL!$Uh(sfmZ@Co8n(r@N-wQYHI!MN/&RXcOP^baIK}mgi7');
===========================================
$ sudo mv * /var/www/html/

$ sudo chown -R www-data:www-data /var/www/html/
$ sudo chmod -R 755 /var/www/html/

$ cd /var/www/html/
$ sudo rm -rf  index.html

$ sudo systemctl restart apache2.service
```
