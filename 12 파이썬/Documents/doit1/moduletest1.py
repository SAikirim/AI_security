#
# moduletest1.p
# 계산기
# fourcal 모듈의 numfind, add, mul 함수만 import 시켜서 해당 내용을 코
#
from fourcal import numfind, add, mul
from fourcal1 import Morefourcal

menu='''
계산기
A.계산하기
B.나가기
'''

def sub(a,b,c):
	return a-b-c


def div(a,b,c):
	return a/b/c

while True:
	print(menu)
	m_choice = input("선택: ")
	if m_choice not in 'AaBb':
		continue
	
	if m_choice in 'Aa':
		num1 = numfind()
		num2 = numfind()
		num3 = numfind()
		symbol = input("기호: ")
		if '+' == symbol:
			print("결과:",add(num1, num2, num3))
		elif '-' == symbol:
			print("결과:",sub(num1, num2, num3))
		elif '*' == symbol:
			print("결과:",mul(num1, num2, num3))
		elif '**' == symbol:
			print("결과:",Morefourcal.mul2(num1, num2, num3))
		else :
			if num2 == 0 or num3 == 0:
				print('0')
			else:	
				print(div(num1, num2, num3))
	else:
		break