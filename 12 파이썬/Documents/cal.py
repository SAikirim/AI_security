#
# 4칙연산 계산기 5대 운영(1,2,3,4,5)
# main
#

from calsub import Calculator, DivCalculator
menu='''
-----------------
메뉴
1. 계산하기
2. 각 계산기의 마지막 결과 확인
3. 나가기
-----------------
'''

c_dict = {'1': 'a', '2': 'b', '3':'c', '4': 'd', '5': 'e'}
while True:
	print(menu)
	option = input("항목을 고르세요: ")
	if option not in ['1','2','3']:
		continue
	if option == '3':
		break
	
	if option == '1':
		c_choice = input("계산기선택(1,2,3,4,5): ")
		c_dict[c_choice] = DivCalculator()
		
		num1 = input("계산할 숫자 num1: ")
		num2 = input("계산할 숫자 num2: ")
		num1 = c_dict[c_choice].num_check(num1)
		num2 = c_dict[c_choice].num_check(num2)
		if 1 == num1 or 1 == num2 :
			continue
		cal_s = input("연산 기호(+,-,*,/,**): ")
		c_dict[c_choice].result = c_dict[c_choice].cal(num1, num2, cal_s)
		print(f"결과: {c_dict[c_choice].result}")
	else:
		c_choice = input("계산기선택(1,2,3,4,5): ")
		print(f"결과: {c_dict[c_choice].result}")
		