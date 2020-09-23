#
# 계산기(Calculator)2
#
menu='''
-----------------
메뉴
1.더하기
2.빼기
3.곱하기
4.나누기
5.자승
6.나가기
-----------------
'''
def num_check(num):
	for i in num:
		if i not in "0123456789" :
			print(f"{num}은 숫자가 아닙니다. 다시 입력해주세요.")
			return 1
	return int(num)

def cal(num1, num2, option, cal):
	print(num1, num2, option)
	#cal = {'1':'+', '2': '-', '3':'*', '4': '/', '5': '**'}
	return eval(f"{num1} {cal[option]} {num2}")
	
cal_dict = {'1':'+', '2': '-', '3':'*', '4': '/', '5': '**'}
while True:
	print(menu)
	option = input("항목을 고르세요: ")
	if option not in ['1','2','3','4','5','6']:
		continue
	if option == '6':
		break
	
	num1, num2 = input("계산할 숫자 2개: ").split()
	num1 = num_check(num1)
	num2 = num_check(num2)
	if 1 == num1 or 1 == num2 :
		continue
	
	result = cal(num1, num2, option, cal_dict)
	print(f"결과: {result}")
'''
	if option == '1':
		result = num1 + num2
	elif option == '2':
		result = num1 - num2
	elif option == '3':
		result = num1 * num2
	elif option == '4':
		result = num1 / num2
	elif option == '5':
		result = num1 ** num2
	else:
		break
	print(f"결과: {result}")
'''