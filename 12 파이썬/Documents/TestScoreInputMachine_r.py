#
# 시험성적 입력 프로그램 코딩
# 파일 읽기
#

exam='''
성적확인

1.시험별 성적
2.시험별 평균
3.과목별 점수
4.나가기
'''

f = open("exam.txt", "r")
lists = [ i.split() for i in f.readlines()]
print(lists)


while True:
	print(exam)
	e_item = input("원하는 목록을 숫자로: ")
	if not e_item in ['1', '2', '3', '4']:
		continue

	if e_item == '1':
		seasion = input("확인하고자 하는 시험은?: ")
		for list in lists: 
			if seasion == list[0]:
				for i in range(1,len(list)):
					print(f"{lists[0][i]}: {list[i]}")
	if e_item == '2':	
		seasion = input("평균을 내고자하는 시험은?: ")
		for list in lists: 
			if seasion == list[0]:
				sum = 0
				for i in range(1,len(list)):
					sum = sum + int(list[i])
				print(f"{seasion}의 평균은 %.2f입니다." % (sum/len(list)))
	if e_item == '3':	
		subject = input("검색하고자하는 과목: ")
		index = lists[0].index(subject)
		for i in range(1, len(lists)):
			print(lists[i][0],":",lists[i][index])
	else:
		f.close()
		break