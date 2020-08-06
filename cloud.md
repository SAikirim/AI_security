
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

* EC2 : 컴퓨터 자원 서비스
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