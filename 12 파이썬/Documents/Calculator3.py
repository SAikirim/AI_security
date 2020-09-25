#
# 4칙연산 계산기 5대 운영(1,2,3,4,5)
# 딕션너리를 이용해 개체(인스턴스)를 5개 만듦
# 다른 방법으로는 개체를 하나 만들고, 클래스 내부에 리스트르 생성하여 값을 저장할 수 있음
#

menu='''
-----------------
메뉴
1. 계산하기
2. 각 계산기의 마지막 결과 확인
3. 나가기
-----------------
'''
class Calculator:
	# 내부에 리스트를 만들어 객체하나로 계산기 여러대 만들기 가능
	# list_c = [0, 0, 0, 0, 0]
	def __init__(self):
		self.result = 0
	def num_check(self, num):
		self.num = num
		try:
			return float(self.num)
		except:
			print(f"{self.num}은 숫자가 아닙니다. 다시 입력해주세요.")
			return 1

	def cal(self, num1, num2, cal_s):
		self.num1 = num1
		self.num2 = num2
		self.cal_s = cal_s
		print(self.num1, self.num2, self.cal_s)
		#cal = {'1':'+', '2': '-', '3':'*', '4': '/', '5': '**'}
		return eval(f"{self.num1} {self.cal_s} {self.num2}")

class DivCalculator(Calculator):
	def cal(self, num1, num2, cal_s):
		self.num1 = num1
		self.num2 = num2
		self.cal_s = cal_s
		print(self.num1, self.num2, self.cal_s)
		#cal = {'1':'+', '2': '-', '3':'*', '4': '/', '5': '**'}
		if num2 == 0 and cal_s == '/':
			return 0
		return eval(f"{self.num1} {self.cal_s} {self.num2}")
	
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
		print(c_choice)
		
		num1 = input("계산할 숫자 num1: ")
		num2 = input("계산할 숫자 num2: ")
		print(num1,type(num2))
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