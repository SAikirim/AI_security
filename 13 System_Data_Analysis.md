# 13 System Data Analysis

### var, tmp 디렉터리 차이
* var : system이 저장하는 장소
* tmp : 사용자가 저장하는 장소
	
	
## Linux
* ubuntu
	- 데비안 - ubuntu(데비안에서 독립, 아키텍처가 다름)
	- init : 조상 프로세스
	- SYSTEMD
	
* RHEL 
	- centos, fedora
	- 6.init(init 관련 command), 7.systemd(init,systemd 관련 command 둘다 존재, 선택적 셋팅을 통해 혼란 가중), 8.systemd 관련된 command만 존재
	- systemd
		+ runlevel
			init runlevel -> /etc/inittab
			systemd runlevel -> systemctl -a | grep multi-user
		+ service(데몬: runlevel O, runlevel X, standalone)
				RHEL 6 이하 : chkconfig --list
						(/etc/init.d/ 또는 /etc/rc.d/init.d/)
				RHEL 7 이상 : systemctl -a
				```
				== 참고 ==
				[root@localhost 바탕화면]# chkconfig --list sshd
				sshd           	0:해제	1:해제	2:활성	3:활성	4:활성	5:활성	6:해제
				[root@localhost 바탕화면]# ls -l /etc/rc.d/rc*.d/*sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc0.d/K25sshd -> ../init.d/sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc1.d/K25sshd -> ../init.d/sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc2.d/S55sshd -> ../init.d/sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc3.d/S55sshd -> ../init.d/sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc4.d/S55sshd -> ../init.d/sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc5.d/S55sshd -> ../init.d/sshd
				lrwxrwxrwx. 1 root root 14 2013-03-14 00:47 /etc/rc.d/rc6.d/K25sshd -> ../init.d/sshd
				[root@localhost 바탕화면]# head /etc/rc.d/init.d/sshd 
				#!/bin/bash
				#
				# sshd		Start up the OpenSSH server daemon
				#
				# chkconfig: 2345 55 25   <--- 이 부분이 chkconfig --list sshd 했을때 on/off 선언
				# description:    <--- 설명
				```
				```
				== RHEL 6 이하 런레벨(unlevel) 의존 서비스 등록 방식 ==
				[root@localhost init.d]# cat aaa
				#!/bin/bash
				#
				# 
				#
				# chkconfig: 345 66 26
				# description: test
				#
				# processname: sshd
				[root@localhost init.d]# chkconfig --list aaa
				aaa 서비스는 chkconfig를 지원하지만 어떠한 런레벨에도 등록되지 않았습니다 ( 'chkconfig --add aaa'를 실행하십시오)
				[root@localhost init.d]# chkconfig --add aaa
				[root@localhost init.d]# chkconfig --list aaa
				aaa            	0:해제	1:해제	2:해제	3:활성	4:활성	5:활성	6:해제
				[root@localhost init.d]# ls -l /etc/rc.d/rc*.d/*aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc0.d/K26aaa -> ../init.d/aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc1.d/K26aaa -> ../init.d/aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc2.d/K26aaa -> ../init.d/aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc3.d/S66aaa -> ../init.d/aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc4.d/S66aaa -> ../init.d/aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc5.d/S66aaa -> ../init.d/aaa
				lrwxrwxrwx. 1 root root 13 2020-10-05 10:51 /etc/rc.d/rc6.d/K26aaa -> ../init.d/aaa
				```
				
			+ runlevel X : 슈퍼데몬 사용 = inetd -> xinetd
				RHEL 6 이하 : chkconfig --list xinetd
							(/etc/xinetd.d 디렉터리를 가짐)
				RHEL 7 이상 : 기본적으로 존재하지 않고 추천하지 않음, 만약존재하면 /etc/xinetd.d 디렉터리를 가짐
			
			+ standalone
				/etc/rc
				
			+ RPC
		
	- network
		+ network.service VS NetworkManager
		+ netstat VS ss
		+ ifconfig VS ip a
		+ ifcofig VS nmcli
	- 방화벽
		+ netfilter 기반의 iptables
		+ iptables VS firewalld
	

### 프로세스 실행 과정
* 조상프로세스 -> 부모프로세스 -> 자식프로세스
* fork() -> RUN() - interrupt-> 대기(sleep)상태 - interrupt -> 종료
	- 오류, 에러 : 디펑트(Defunct)
	
* exit() -> swap in -> 종료
	- PPID -> PID -> PPID : 종료 과정
	- 고아프로세스	: 종료시 발생 가능 문제
		+ PPID 선 종료를 통한 exit() 단계 진행 오류
	- 좀비프로세스	: 종료시 발생 가능 문제
		+ 종료 오류로 인한 생성
		
* signl -> pid에게 신호를 보냄 'kill -l'

---
## rsyslog
* syslog의 옆그레이드 버전
	- 원래 syslog는 remote log 수신을 위해 데몬실행 시 옵션을 변경해서 재실행했다.
	- rsyslog는 위 부분만 해결해서 remote log 수신을 위해 프로세스를 죽이고, 다시 옵션을 선언해서 실행하는 부분을 하지 않고 그냥 되도록 변경함
	```
	== 기본 정보 ==
	rsyslogd               rsyslog-recover-qi.pl  
	[root@localhost ~]# which rsyslogd
	/usr/sbin/rsyslogd
	[root@localhost ~]# rpm -qf /usr/sbin/rsyslogd
	rsyslog-7.4.7-6.el7.x86_64
	[root@localhost ~]# rpm -ql rsyslog
	.....
	/etc/rsyslog.conf
	/etc/rsyslog.d
	/etc/sysconfig/rsyslog
	/usr/bin/rsyslog-recover-qi.pl
	/usr/lib/systemd/system/rsyslog.service
	.....
	==================================

	[root@localhost ~]# more /etc/rsyslog.conf 
	# rsyslog configuration file

	# For more information see /usr/share/doc/rsyslog-*/rsyslog_conf.html
	# If you experience problems, see http://www.rsyslog.com/doc/troubleshoot.html

	#### MODULES ####

	# The imjournal module bellow is now used as a message source instead of imuxsock.
	$ModLoad imuxsock # provides support for local system logging (e.g. via logger command)
	$ModLoad imjournal # provides access to the systemd journal
	#$ModLoad imklog # reads kernel messages (the same are read from journald)
	#$ModLoad immark  # provides --MARK-- message capability

	# Provides UDP syslog reception
	#$ModLoad imudp
	#$UDPServerRun 514

	# Provides TCP syslog reception
	#$ModLoad imtcp
	#$InputTCPServerRun 514
		======== 참조 =====
		[root@localhost ~]# grep 514 /etc/services 
		shell           514/tcp         cmd             # no passwords used
		syslog          514/udp
		==================

	#### GLOBAL DIRECTIVES ####

	# Where to place auxiliary files
	$WorkDirectory /var/lib/rsyslog

	# Use default timestamp format
	$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat

	# File syncing capability is disabled by default. This feature is usually not required,
	# not useful and an extreme performance hit
	#$ActionFileEnableSync on

	# Include all config files in /etc/rsyslog.d/
	$IncludeConfig /etc/rsyslog.d/*.conf

	# Turn off message reception via local log socket;
	# local messages are retrieved through imjournal now.
	$OmitLocalLogging on

	# File to store the position in the journal
	$IMJournalStateFile imjournal.state

	#### RULES ####    <--- 기존 syslog 는 이 부분부터 존재

	# Log all kernel messages to the console.
	# Logging much else clutters up the screen.
	#kern.*                                                 /dev/console

	# Log anything (except mail) of level info or higher.
	# Don't log private authentication messages!
	*.info;mail.none;authpriv.none;cron.none                /var/log/messages

	# The authpriv file has restricted access.
	authpriv.*                                              /var/log/secure

	# Log all the mail messages in one place.
	mail.*                                                  -/var/log/maillog


	# Log cron stuff
	cron.*                                                  /var/log/cron

	# Everybody gets emergency messages
	*.emerg                                                 :omusrmsg:*

	# Save news errors of level crit and higher in a special file.
	uucp,news.crit                                          /var/log/spooler

	# Save boot messages also to boot.log
	local7.*                                                /var/log/boot.log


	# ### begin forwarding rule ###
	# The statement between the begin ... end define a SINGLE forwarding
	# rule. They belong together, do NOT split them. If you create multiple
	# forwarding rules, duplicate the whole block!
	# Remote Logging (we use TCP for reliable delivery)
	#
	# An on-disk queue is created for this action. If the remote host is
	# down, messages are spooled to disk and sent when it is up again.
	#$ActionQueueFileName fwdRule1 # unique name prefix for spool files
	#$ActionQueueMaxDiskSpace 1g   # 1gb space limit (use as much as possible)
	#$ActionQueueSaveOnShutdown on # save messages to disk on shutdown
	#$ActionQueueType LinkedList   # run asynchronously
	#$ActionResumeRetryCount -1    # infinite retries if host is down
	# remote host is: name/ip:port, e.g. 192.168.0.1:514, port optional
	#*.* @@remote-host:514
	# ### end of the forwarding rule ###
	```

### rsyslog.conf 설정 이해
```
대상.위험도									저장위치(파일경로, 호스트네임, ip, user name, broadcast, terminal)
facility.priority(Severity); 			action
------------------------------------------------------------------
kern.*                                  /dev/console
```
#### 참고
* RHEL은 https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-viewing_and_managing_log_files
```
kern (0)
user (1)
mail (2)
daemon (3)
auth (4)   <---  auth은 인가에 대한 로그다. 
syslog (5)
lpr (6)
news (7)
cron (8)
authpriv (9)  <--  로그인은 '인증-> 식별-> 인가' 인데 authpriv는  인증 - 식별 에 관한 로그다.
ftp (10)         
local0 through local7 (16 - 23)
```
* auth (4) <== auth는 __인가__에 대한 로그임
* authpriv(9) <== 로그인은 '인증 -> 식별 -> 인가' 인데 authpriv는 __인증__에 관한 로그임
	- 타입 1 에러 : 인증받아야 하는데, 인증 못 받음
	- 타입 2 에러 : 인증되면 안 되는데, 인증이 됨

* https://wiki.gentoo.org/wiki/Rsyslog
```
=======대상 (facility)========
Numerical Code	Facility	Description
0	kern	kernel messages
1	user	user-level messages
2	mail	mail system
3	daemon	system daemons
4	auth	security/authorization messages
5	syslog	messages generated internally by syslogd
6	lpr	line printer subsystem
7	news	network news subsystem
8	uucp	UUCP subsystem
9	cron	clock daemon
10	security	security/authorization messages    <----  운영체제 마다 차이가 있다. 
11	ftp	FTP daemon
12	ntp	NTP subsystem
13	logaudit	log audit
14	logalert	log alert
15	clock	clock daemon (note 2)
16	local0	local use 0 (local0)
17	local1	local use 1 (local1)
18	local2	local use 2 (local2)
19	local3	local use 3 (local3)
20	local4	local use 4 (local4)
21	local5	local use 5 (local5)
22	local6	local use 6 (local6)
23	local7	local use 7 (local7)
================================
```

* 위험도 (priority 또는 Severity )
```
==Severity==
Numerical Code	Severity	Description
			0	emerg	system is unusable
			1	alert	action must be taken immediately
			2	crit	critical conditions
			3	error,err	error conditions
			4	warning	warning conditions
			5	notice	normal but significant condition
			6	info	informational messages
			7	debug	debug-level messages
emerg (0)
alert (1)
crit (2)
err (3)
warning (4)
notice (5)
info (6)
debug (7)
```
* ex)   kernel.alert    kernel 대상로그 중 alert 이상의 로그를 ...

```
*.info;mail.none;authpriv.none;cron.none		/var/log/messages
	- info info 레벨부터 상위 위험도를 포함해서
	- *.=info : info 레벨만
```

* 저장위치는 어떻게 표기 할 수 있나 (action)
```
*.info;mail.none;authpriv.none;cron.none		/var/llog/messages 절대경로 표현하면 파일로 저장
*.emerg											:omusrmsg:*
*.emerg											*	모든터미널(remote terminal에게 전송이 제한됨)
```
* /etc/hosts <-- hostname에 대해 정의 할 수 있는 파일
	- 매번 모르는 domain 혹은 hostname을 요청할 때마다 외부 dns에게 요청을 한다면 어마어마한 네트워크 대역폭을 소비하게 될 것이다.
	- 이는 회사입장에서 통신에 기본적인 요소인 DOMAIN, IP 매핑 과정을 어쩔수 없이 계속 대역폭을 소모하면서 동작을 해야하고 broadcast 사용하는 IPv4는 고질적인 네트워크 병목현상에 놓이게 될 것이다.

	- cache -> hosts -> 외부 DNS
	- DNS -> DNS caching name server
	
	- ip > domian
	- ip > hostname 내부 네트워크에서 사용, local network에서 IP 할당된 장치를 domain server에 등록하지 않고 file로 등록해서 처리
	- /etc/hosts  <  /etc/nsswitch.conf 
	```
	[root@localhost rsyslog]# grep hosts  /etc/nsswitch.conf
	#hosts:     db files nisplus nis dns
	hosts:      files dns

		hosts  : file (/etc/hosts) dns (/etc/resolv.conf)
	[root@localhost rsyslog]# cat /etc/hosts
	127.0.0.1   localhost	  
	192.168.100.10	serverA
	192.168.100.20 	ftp_server
	*.emerg										@serverA
	*.*											@@remote-host:514
	```



---
## logrotate 이해
* errors mail_admin	: 에러발생시 어드민에게 메일
* mail mail_admin	: logrotate할 때, 파일을 어드민에게 메일 보내기
```
[root@localhost ~]# rpm -qa | grep logrotate
logrotate-3.8.6-4.el7.x86_64
[root@localhost ~]# rpm -ql logrotate 
/etc/cron.daily/logrotate
/etc/logrotate.conf     <-------
/etc/logrotate.d        <-------
/usr/sbin/logrotate
/usr/share/doc/logrotate-3.8.6
/usr/share/doc/logrotate-3.8.6/CHANGES
/usr/share/doc/logrotate-3.8.6/COPYING
/usr/share/man/man5/logrotate.conf.5.gz
/usr/share/man/man8/logrotate.8.gz
/var/lib/logrotate.status
```
------------------------------------------
* /etc/cron.daily/logrotate   <--- logrotate 를 시스템 crontab 의 daily 목록에 등록 해둠 
* /etc/logrotate.conf     <---  설정파일 ( 어떤 기준을 가지고 log 파일을 rotate 시킬것인가 설정)
* /etc/logrotate.d      <--- logrotate.conf 설정과 관련된 디렉토리


```
/etc/logrotate.conf

[root@localhost ~]# cat /etc/logrotate.conf 
# see "man logrotate" for details
# rotate log files weekly
weekly           <---  주단위로 log 파일을 rotate 시키겠다. ( 월, 주,일 )

# keep 4 weeks worth of backlogs
rotate 4		<--- 생성되는 log 파일을 4개 단위로 남기겠다. 즉,  log0 , log1,  log2, log3 
					log0 -> log1  저장되고 log0 초기화
					log1 -> log2  저장되고 log1 은 log0의 데이터를 받음
					log2 -> log3  저장되고 log2 은 log1의 데이터를 받음
					즉, 한달 까지는 시스템에서 파일형태로 가지고 있다. 하지만 한달이 지나면 소멸하게된다. 
					그러니까 어떻게 해야한다. 한달 단위로 crontab 을 구성해서 log 파일을 백업해야 한다. 
					

# create new (empty) log files after rotating old ones
create      <--  "log0 초기화" 부분이 이에 해당한다.

# use date as a suffix of the rotated file
dateext		<--  date 를 사용해서 rotate 한다.  이 선언은  rsyslog 에 들어오면 추가된 기능이다. 보통 위 rotate 부분에
				 명시된 부분을 0 부터 숫자 만큼 열거에서 파일네이밍을 하지만  dateext 옵션이 추가되면서 
				 "PM packages drop log" 에 의한 목록이나 include 된 log  목록은 파일의 이름에 날짜가 명시된다.
				 

# uncomment this if you want your log files compressed
#compress    <---  gzip 으로 압축을 한다. 

# RPM packages drop log rotation information into this directory
include /etc/logrotate.d
============참조 ============
[root@localhost log]# rpm -qf /var/log/btmp    <--- RPM packages drop log ( btmp, wtmp, utmp)
initscripts-9.49.17-1.el7.x86_64
[root@localhost log]# rpm -ql initscripts
.......
/var/log/btmp
/var/log/wtmp
/var/run/netreport
/var/run/utmp
........
==============================

# no packages own wtmp and btmp -- we'll rotate them here
/var/log/wtmp {
    monthly
    create 0664 root utmp
	minsize 1M
    rotate 1
}
    error test1  에러를 test1 이라는 사용자에게 보냄
	mail test1	로그파일을 순환시키고 나중에 삭제해야 할 때 삭제하지 않고 메일로 보냄 
	rotate 0  

/var/log/btmp {
    missingok
    monthly
    create 0600 root utmp
    rotate 1
}
	nomissingok  기본값 이다.    로그파일이 없으면 에러를 낸다.
	missingok  로그파일이 없어도 에러를 내지 않는다. 


# system-specific logs may be also be configured here.
```

```
== RPM packages drop log 가 아닌 log 파일 rotate 설정 예제 ==

/var/log/maillog {
	weekly
	size 500k
	rotate 4
	compress
	errors mail_admin
	mail mail_admin
	nomissingok
	create 0600 root root
}

/var/log/messages {
	postrotate				# 지정된 로그파일에 logrotate작업이 끝나고 난 이후에 실행할 작업을 설정
		/usr/bin/killall -HUP rsyslogd 
	endscript
}
```

---
## 인증과 관련된 log 파일 및 동작 이해
* RPM packages drop log + rsyslog.conf 파일 둘다 존재
* /var/log/btmp , /var/log/wtmp , /var/run/netreport, /var/run/utmp , /var/log/lastlog
```
[root@localhost log]# rpm -qf /var/log/lastlog 
setup-2.8.71-4.el7.noarch
util-linux-2.23.2-16.el7.x86_64
```

### /var/run/utmp vs /var/log/wtmp 
* /var/run
	- 현재 지금것만 저장
	- /var/run/utmp : w, who : 현재 로그인한 상태 정보	
```
[root@localhost run]# rpm -qf /var/run/utmp 
initscripts-9.49.17-1.el7.x86_64
[root@localhost run]# w
 15:15:18 up  4:13,  3 users,  load average: 0.13, 0.06, 0.06
USER     TTY        LOGIN@   IDLE   JCPU   PCPU WHAT
root     :0        11:02   ?xdm?   9:45   0.17s gdm-session-worker [pam/gdm-password]
root     pts/0     11:03    6.00s  0.50s  0.06s w
root     pts/1     11:27    1:42m  0.13s  0.13s bash
[root@localhost run]# who
root     :0           2020-10-05 11:02 (:0)
root     pts/0        2020-10-05 11:03 (:0)
root     pts/1        2020-10-05 11:27 (:0)
[root@localhost run]# who -a
           system boot  2020-10-05 20:01
root     ? :0           2020-10-05 11:02   ?          9800 (:0)
           run-level 5  2020-10-05 11:02
root     + pts/0        2020-10-05 11:03  old        13123 (:0)
root     + pts/1        2020-10-05 11:27  old        13123 (:0)
```

* /var/log
	- /var/log/wtmp : last, lastlog : 로그인한 IP와 시간, 재부팅 날짜 정보
		+ 사용자들의 로그인인/아웃 정보, 시스템 관련 정보 기록
	```
	[root@localhost run]# rpm -qf /var/log/wtmp 
	initscripts-9.49.17-1.el7.x86_64
	[root@localhost run]# last
	root     pts/1        :0               Mon Oct  5 11:27   still logged in   
	root     pts/0        :0               Mon Oct  5 11:03   still logged in   
	root     :0           :0               Mon Oct  5 11:02   still logged in   
	(unknown :0           :0               Mon Oct  5 11:01 - 11:02  (00:00)    
	reboot   system boot  3.10.0-123.el7.x Mon Oct  5 20:01 - 15:17  (-4:-43)   
	user     pts/0        :0               Mon Jun 15 11:29 - 11:30  (00:01)    
	user     :0           :0               Mon Jun 15 11:29 - 11:30  (00:01)    
	(unknown :0           :0               Mon Jun 15 11:27 - 11:29  (00:01)    
	reboot   system boot  3.10.0-123.el7.x Mon Jun 15 20:27 - 11:31  (-8:-56)   

	wtmp begins Mon Jun 15 20:27:10 2015

	== /var/log/lastlog ==

	[root@localhost run]# ls -l /var/log/lastlog 
	-rw-r--r--. 1 root root 292292 Oct  5 11:02 /var/log/lastlog
	[root@localhost run]# file  /var/log/lastlog 
	/var/log/lastlog: data
	[root@localhost run]# lastlog 
	Username         Port     From             Latest
	root             :0                        Mon Oct  5 11:02:05 +0900 2020
	bin                                        **Never logged in**    <--  /etc/passwd 의 마지막 필드가 shell이다
	daemon                                     **Never logged in**         이중 nologin 되어진 shell 항목은 
	adm                                        **Never logged in**			로그인을 위해서 존재하는 계정아닌 시스템을 
	lp                                         **Never logged in**			운영하기 위한 계정 이다.
	sync                                       **Never logged in**			결국 정리하면 /etc/passwd 에 nologin 
	shutdown                                   **Never logged in**			되어진 shell 가진 사용자는 반드시
	halt                                       **Never logged in**			lastlog 결과에 "Never logged in" 으로 
	mail                                       **Never logged in**			체크되어 있어야 한다. 
	operator                                   **Never logged in**
	games                                      **Never logged in**
	ftp                                        **Never logged in**
	nobody                                     **Never logged in**
	dbus                                       **Never logged in**
	polkitd                                    **Never logged in**
	unbound                                    **Never logged in**
	colord                                     **Never logged in**
	usbmuxd                                    **Never logged in**
	avahi                                      **Never logged in**
	avahi-autoipd                              **Never logged in**
	saslauth                                   **Never logged in**
	qemu                                       **Never logged in**
	libstoragemgmt                             **Never logged in**
	rpc                                        **Never logged in**
	rpcuser                                    **Never logged in**
	nfsnobody                                  **Never logged in**
	rtkit                                      **Never logged in**
	radvd                                      **Never logged in**
	ntp                                        **Never logged in**
	chrony                                     **Never logged in**
	abrt                                       **Never logged in**
	pulse                                      **Never logged in**
	gdm              :0                        Mon Oct  5 11:01:34 +0900 2020
	gnome-initial-setup                           **Never logged in**
	postfix                                    **Never logged in**
	sshd                                       **Never logged in**
	tcpdump                                    **Never logged in**
	user             :0                        Mon Jun 15 11:29:30 +0900 2015
	```
	- /var/log/btmp : lastb : 실패한 로그인 정보

##### w who last lastlog lastb     <---  RPM packages drop log
```
[root@localhost ~]# ls -l /etc/rsyslog.conf 
-rw-r--r--. 1 root root 3232 Mar 26  2014 /etc/rsyslog.conf
[root@localhost ~]# grep auth /etc/rsyslog.conf
......
# The authpriv file has restricted access.
authpriv.*                                              /var/log/secure
.......
```

---
user /etc/passwd 파일에 존재
나머지 계정은 존재하지 않는다.

/var/log/secure 인증, 식별 로그를 남김

* 존재하는 계정
```
== /var/log/secure ==
Oct  5 17:13:42 localhost unix_chkpwd[47900]: password check failed for user (user)
Oct  5 17:13:42 localhost sshd[47897]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.110.136  user=user
Oct  5 17:13:43 localhost sshd[47897]: Failed password for user from 192.168.110.136 port 36004 ssh2
Oct  5 17:13:45 localhost unix_chkpwd[47910]: password check failed for user (user)
Oct  5 17:13:47 localhost sshd[47897]: Failed password for user from 192.168.110.136 port 36004 ssh2
Oct  5 17:13:49 localhost unix_chkpwd[47911]: password check failed for user (user)
Oct  5 17:13:51 localhost sshd[47897]: Failed password for user from 192.168.110.136 port 36004 ssh2
Oct  5 17:13:51 localhost sshd[47897]: Connection closed by 192.168.110.136 [preauth]
Oct  5 17:13:51 localhost sshd[47897]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.110.136  user=user

=== /var/log/messages ===
Oct  5 17:27:11 localhost gnome-keyring-daemon[9808]: couldn't open store file: /root/.local/share/keyrings/user.keystore: No such file or directory
Oct  5 17:27:11 localhost gnome-keyring-daemon[9808]: couldn't open store file: /root/.local/share/keyrings/user.keystore: Bad file descriptor
Oct  5 17:27:11 localhost gnome-keyring-daemon[9808]: file gkm-gnome2-storage.c: line 1380 (gkm_gnome2_storage_token_flags): should not be reached
Oct  5 17:27:11 localhost gnome-keyring-daemon[9808]: couldn't open store file: /root/.local/share/keyrings/user.keystore: No such file or directory
Oct  5 17:27:11 localhost gnome-keyring-daemon[9808]: couldn't open store file: /root/.local/share/keyrings/user.keystore: Bad file descriptor
```

* 존재하지 않는 계정
```
[root@localhost log]# grep "Failed password for invalid user" /var/log/secure 
Oct  5 16:23:11 localhost sshd[46981]: Failed password for invalid user test from ::1 port 41800 ssh2
Oct  5 16:23:16 localhost sshd[46981]: Failed password for invalid user test from ::1 port 41800 ssh2
Oct  5 16:23:21 localhost sshd[46981]: Failed password for invalid user test from ::1 port 41800 ssh2
Oct  5 16:25:20 localhost sshd[47018]: Failed password for invalid user userman from 192.168.110.136 port 35998 ssh2
Oct  5 16:25:25 localhost sshd[47018]: Failed password for invalid user userman from 192.168.110.136 port 35998 ssh2
Oct  5 16:25:29 localhost sshd[47018]: Failed password for invalid user userman from 192.168.110.136 port 35998 ssh2
Oct  5 16:25:41 localhost sshd[47025]: Failed password for invalid user userman from 192.168.110.136 port 35999 ssh2
Oct  5 16:25:46 localhost sshd[47025]: Failed password for invalid user userman from 192.168.110.136 port 35999 ssh2
Oct  5 16:26:05 localhost sshd[47025]: Failed password for invalid user userman from 192.168.110.136 port 35999 ssh2
Oct  5 16:26:44 localhost sshd[47048]: Failed password for invalid user userhat from 192.168.110.136 port 36000 ssh2
Oct  5 16:26:47 localhost sshd[47048]: Failed password for invalid user userhat from 192.168.110.136 port 36000 ssh2
Oct  5 16:26:52 localhost sshd[47048]: Failed password for invalid user userhat from 192.168.110.136 port 36000 ssh2
Oct  5 16:27:24 localhost sshd[47074]: Failed password for invalid user userhat from 192.168.110.136 port 36001 ssh2
Oct  5 16:27:36 localhost sshd[47074]: Failed password for invalid user userhat from 192.168.110.136 port 36001 ssh2
```

* 로그인 정상 관정
```
== /var/log/secure ==
Oct  5 17:25:09 localhost unix_chkpwd[48086]: password check failed for user (user)
Oct  5 17:25:09 localhost sshd[48083]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.110.136  user=user
Oct  5 17:25:11 localhost sshd[48083]: Failed password for user from 192.168.110.136 port 36005 ssh2
Oct  5 17:25:56 localhost sshd[48083]: Accepted password for user from 192.168.110.136 port 36005 ssh2
Oct  5 17:25:57 localhost sshd[48083]: pam_unix(sshd:session): session opened for user user by (uid=0)
```

* 인증 - 식별
```
== /var/log/secure ==
Oct  5 17:25:56 localhost sshd[48083]: Accepted password for user from 192.168.110.136 port 36005 ssh2
Oct  5 17:25:57 localhost sshd[48083]: pam_unix(sshd:session): session opened for user user by (uid=0)
Oct  5 17:27:05 localhost sshd[48098]: Received disconnect from 192.168.110.136: 11: disconnected by user
Oct  5 17:27:05 localhost sshd[48083]: pam_unix(sshd:session): session closed for user user
```

* 인가 
```
== /var/log/secure ==
Oct  5 17:28:47 localhost sshd[48146]: Accepted password for user from 192.168.110.136 port 36006 ssh2
Oct  5 17:28:47 localhost sshd[48146]: pam_unix(sshd:session): session opened for user user by (uid=0)
```

```
== /var/log/messages ==
Oct  5 17:28:47 localhost systemd: Created slice user-1000.slice.
Oct  5 17:28:47 localhost systemd: Starting Session 47 of user user.
Oct  5 17:28:47 localhost systemd: Started Session 47 of user user.
Oct  5 17:28:47 localhost systemd-logind: New session 47 of user user.
```

* centos 6, centos 7 : 존재하는 계정과 존재하지 않는 계정 만들고 로그인을 각각 실패, 성공을 테스트 후 각 각 남은 `/var/log/messages , /var/log/secure` 확인       
* 로그의  인증 - 식별 - 인가 의 단계별 로그를 남기는 파일이 같은 방식으로 로그를 남기고 있지 않다.
	- 이런 부분은 우리가 로그파일을 파싱할 때 어려움으로 남게된다. 

```
Failed password for user   존재하는 계정
Failed password for invalid user    존재하지 않는 계정
Accepted password for  존재하면서 로그인을 성공한 계정 
```
* tty 부분에		`:0	PTS (가상터미널)  TTY  (가상콘솔터미널)`
	- pts = GUI 환경에서 오픈하는 터미널  +  원격에서 접근 터미널 
	- tty = 콘솔터미널을 운영체제 안에서 지원해주고 그 가상콘솔터미널로 접근하면 tty
		+ tty 로그면 내부소행임

	- :0  시스템 운영체제가 운영체제를 동작시키기 위해 사용 

---
## WEB ATTACK과 log
* sql injection
* xss
* csrf
* file upload attack -> web shell
* file download
* 파라미터 변조
* 불층분한 인증, 인가, 직접객체 참조

* 찾기 힘든 공격
	- file download
	- 파라미터 변조
	- 잘못된 인증, 인가
	
	- sql injection, xss
		+ 기존 정보에 + 외부 유입이 들어가는 구조
		+ 외부 유입이 들어가는 부분에 대한 문자열 필터링 혹은 decode 방식을 이용하여 입력되는 값을 해석할 수 있음
		
---
### 문제 1
어떤 사용자가 몇 번 접속했는지
cat lastb.txt |  awk '{print $1}' | sort -n | uniq -c  |tail -n+3

### 문제 2
어떤 아이피 주소가 있고 각각 몇번 접속
awk '{print $2 " : " $3}' lastb.txt | sort -n | uniq -c |tail -n+4 |grep -v "localhost"

### 문제3
각 아이피별로
get, post 요청

### jc사용한 json변환 명령어
head -n10 access.log|sed 's/"//g'|tail -n+2 |awk '{printf "%s, %s, %s\n",$1, $6, $7 }' |sed -e '1 i\"IP", "METHOD", "URL"' | jc --csv -p

### awk 사용
sed 's/\"//g' access.log | grep ^[0-9]| awk '{print "\""NR"\":{\"IP\":\""$1 "\", \"METHOD\":\""$6"\"},"}'
