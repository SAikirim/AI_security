#
# 계산기(Calculator)
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
cal = {'1':'+', '2': '-', '3':'*', '4': '/', '5': '**'}
while True:
	print(menu)
	option = input("항목을 고르세요: ")
	if option not in ['1','2','3','4','5','6']:
		continue
	if option == '6':
		break
	try:	
		num1, num2 = map(int, input("계산할 숫자 2개: ").split())
	except:
		print("숫자가 아닙니다. 다시 입력해주세요.")
		continue

	result = eval(f"{num1} {cal[option]} {num2}")
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