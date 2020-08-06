# 데이터베이스 서비스

## 데이터베이스
* 여러 사람에 의해 공유되어 사용될 목적으로 통합되여 관리되는 데이터의 집합
* 데이터를 저장하는 곳

DBMS : 데이터베이스를 관리하는 것

### 종류
* MYSQL(MriaDB), ORACLE, MSSQL(SQL Server)

### 방식
* RDBMS(관계형 데이터베이스 관리 시스템)
    - relational database management system
    - 데이터를 Row, Column이라는 형태로 저장

### 요소, 정의
* 데이터 : 하나한의 자료
* 테이블 : 테이터를 표형식으로 만든 것
* 레코드 : 테이블의 가로, 이름이 없음
* 컬럼(열, 필드) : 테이블의 세로, 이름이 있음, 데이터 타입이 설정됨 (숫자, 문자)
* PK(Primary Key) = 주요키 : 레코드를 식별하는 유일한 값을 갖고 있는 비어있지 않은 컬럼
* FK = 외래키 : 다른 테이블의 주요키와 대응되는 컬럼
* SQL : 관계형 데이터베이스를 이용하기 위한 표준 언어(구조화된 질의 언어)
    - DB에서 정보를 얻거나, 조작하거나, 갱신하는 등의 역할을 하는 언어
    - Structured Query Language

---
### SQL 명령어

#### 데이터베이스 관련 SQL

`SHOW DATABASES;`  
데이터베이스들 이름 조회

`USE [데이터베이스이름];`  
사용할 DB 선택


`CREATE DATABASE [데이터베이스이름];`  
`DROP DATABASE [데이터베이스이름];`  
DB 생성, 삭제 

==============================================
#### 테이블 관련 SQL

`SHOW TABLES;`  
테이블 조회

`EXPLAIN [테이블이름];`  
`DESCRIBE [테이블이름];`  
`DESC [테이블이름];`  
테이블 정보 확인

`CREATE TABLE [테이블이름] (필드이름1 필드타입 필드이름2 필드타입2 .....);`  
테이블 생성

```
예시 :
CREATE DATABSE member_db;

USE member_db;

CREATE TABLE member (
id varchar(12) NOT NULL PRIMARY KEY,
name NVARCHAR(5),
age int,
address NVARCHAR(5) );
```
* NVARCHAR : 유니코드 지원 가변 문자 속성

* 테이블 삭제  
`DROP TABLE [테이블이름];` 

* 테이블 수정  
`ALTER TABLE <Table Name> <option>;`  
Ex) ALTER TABLE <Table Name> ADD [컬럼이름] [타입];  

    - ALTER TABLE member ADD COLUMN memberidx INT;

==============================================
#### 데이터 형의 종류
* VARCHAR(n) : 가변 길이 문자열
* CHAR(n): 고정 길이 문자열
* INT : 정수형 숫자
* FLOAT : 실수형 숫자
* DATE : 날짜를 저장함
* TIME : 시간을 저장함

==============================================
#### 레코드 삽입/삭제/수정

* 삽입  
`insert into <table name> values (value1, value2,...);`  
예 : insert into member values('hong','홍길동',22,'경기');

* 수정  
`update 테이블이름 set 필드이름1=수정값, 필드이름=수정값.... where 필터링조건;`  
예 : update member set age =50 where id = 'kim';

* 삭제  
`delete from 테이블이름 where 필터링조건;`

==============================================
#### 테이블 조회

`SELECT [필드이름1], [필드이름2], ... FROM [테이블이름] WHERE [조건];`
Ex) select * from [테이블이름]

---
### Mariadb 설치  
`yum -y remove mariadb-libs`  
`yum -y localinstall MariaDB-10.0.15-centos7_0-x86_64-*.rpm`

=============================================
* 실행
```bash
systemctl restart mysql

chkconfig mysql on

firewall-cmd --permanent --add-port=3306/tcp
firewall-cmd --reload

mysqladmin -u root password '1234'

mysql -u root -p
```
* 계정 확인  
`SELECT user, host FROM user WHERE user NOT LIKE '';`  

* 원격 접속 가능 계정 생성(test)  
`GRANT ALL PRIVILEGES ON *.* TO test@'%.%.%.%' IDENTIFIED by '1234';`  

--------------------------
윈도우 클라이언트

`mysql -h 서버ip -u test -p`
Ex) mysql.exe -h 192.168.56.103 -u test -p1234

---
## 빅데이터
 
### No-SQLDB
* key : value 형태 등 있음
