#### 스노트 구동 및 ELK 연동

스노트 구동

```
sudo snort -v -l /var/log/snort -A fast -c /etc/snort/snort.conf -i ens33
```



공격 패킷이 스노트에 탐지되면 /var/log/snort/에 alert 로그가 생성된다. alert 로그를 grok 필터를 이용하여 로그스태시로 수집 및 가공하여 저장한다.



스노트 로그 처리 전용 로그스태시와 파일비트 폴더를 생성

```
cd ~/ELK
cp -r filebeat-7.6.2-linux-x86_64 filebeat-snort
cp -r logstash-7.6.2 logstash-snort
```



로그스태시 사용자 패턴 저장(직접 작성한 grok 필터에 사용함)

```
## /home/hacker/patterns/custom_pattern  사용자 패턴 파일 생성

NOTCURLYOPEN [^{]+
NOTCURLYCLOSE [^}]+
NOTSQROPEN [^\[]+
NOTSQRCLOSE [^\]]+
```



로그스태시 설정 파일 생성(logstash_snort.conf)

```
# cd ~/ELK/logstash-snort/
# vi logstash_snort.conf

input {
  beats {
    port => "5044"
  }
}
filter {
    grok {
        patterns_dir => "/home/hacker/ELK/patterns"
        match => { "message" => "^%{NOTSQROPEN:[snort_timestamp]}\s+\[\*+\]\s+\[%{NONNEGINT:[gid]}:%{NONNEGINT:[sid]}:%{NONNEGINT:[rev]}\]\s+%{GREEDYDATA:[signature]}\s+\[\*+\](?:\s+\[Classification:\s+%{NOTSQRCLOSE:[class]}\])?(?:\s+\[Priority:\s+%{NONNEGINT:[priority]}\])?(?:\s+\[Xref\s+=>\s+%{NOTSQRCLOSE:[xref]}\])?\s+{%{NOTCURLYCLOSE:[proto]}}\s+%{IP:[src_ip]}(?::%{INT:[src_port]})?\s+->\s+%{IP:[dest_ip]}(?::%{INT:[dest_port]})?.*$" }
    }
if [priority] {
      translate {
        field => "[priority]"
        destination => "[log][severity]"
        dictionary => {
          "1" => "alert"
          "2" => "critical"
          "3" => "warning"
          "4" => "notice"
        }
        fallback => "warning"
      }
    } else {
      mutate {
        replace => { "[log][severity]" => "informational" }
       }
    }
if [snort_timestamp] {
      mutate {
        gsub => [ "[snort_timestamp]", "\s+$", "" ]
      }
      date {
        locale => "en"
        match => [ "[snort_timestamp]", "MM/dd-HH:mm:ss.SSSSSS", "MM/dd/yy-HH:mm:ss.SSSSSS", "EEE MMM d HH:mm:ss yyyy", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss", "MMM dd yyyy HH:mm:ss", "MMM  d yyyy HH:mm:ss", "ISO8601", "yyyy-MM-dd HH:mm:ss.SSSSSS", "MMM dd HH:mm:ss yyyy", "MMM  d HH:mm:ss yyyy" ]
      }
    }
    geoip {
        source => "src_ip"
    }
}
output {
elasticsearch {
      hosts => ["localhost:9200"]
      index => "snort-%{+YYYY.MM.dd}"
    }
}
```



filebeat-snort 폴더로 들어가서 filebeat.yml 파일 작성

```
filebeat.inputs:
- type: log
  paths:
    - /var/log/snort/alert
output.logstash:
  hosts: ["localhost:5044"]
```



파일비트와 로그스태시 실행(사전에 키바나와 엘라스틱서치 실행해야 함)

```
cd ~/ELK/logstash-snort
./bin/logstash -f ./logstash_snort.conf --path.data .

cd ~/ELK/filebeat-snort
./filebeat -e -c filebeat.yml -d "publish"

# 권한 에러가 날 경우
# 'sudo chmod 755 filebeat.yml' 와 'sudo chown root:root filebeat.yml' 실행
```



키바나 Management에서 스노트 로그 인덱스 정상 추가 확인

- Management 메뉴에서 Index Patterns를 실행한 후 '+Create Index' 버튼을 누르고 패턴 이름에 snort 문자를 입력하면 인덱스가 생성된 것을 확인할 수 있다.

- Time Filter에 @timestamp를 지정한 후 인덱스 패턴을 만들고, snort* 인덱스를 default index로 지정한다. 
- Discover 메뉴에서 확인한다.