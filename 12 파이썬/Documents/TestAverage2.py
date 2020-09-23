#
# 평균 성적2
#


record = {}
add_input = 'Y'
while True:
	if  add_input == 'n':
		print(f"모든 과목의 평균 : {sum(record.values())/len(record)}점")
		break
	x,y = input("과목과 점수를 입력하세요: ").split()
	try:
		record[x] = int(y)
	except:
		print("잘못입력하였습니다.")
		continue
	
	while True:
		add_input = input("과목과 점수를 추가하겠습니까? (y/n)")
		if add_input in ['y','n']:
			break
