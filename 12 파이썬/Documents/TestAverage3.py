#
# 평균 성적3
# 함수 사용
#

def num_check(num):
	for i in num:
		if i not in "0123456789" :
			print("숫자가 아닙니다. 다시 입력해주세요.")
			return 1
	return int(num)

def avr(nums):
	print(f"모든 과목의 평균 : {sum(record.values())/len(record)}점")
	return
	
record = {}
add_input = 'Y'
while True:
	if  add_input == 'n':
		avr(record)
		break
	x,y = input("과목과 점수를 입력하세요: ").split()
	num = num_check(y)
	if 1 == num :
		continue
	record[x] = int(y)
	
	while True:
		add_input = input("과목과 점수를 추가하겠습니까? (y/n)")
		if add_input in ['y','n']:
			break
