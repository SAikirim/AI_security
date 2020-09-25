#
# 4칙연산 계산기 5대 운영(1,2,3,4,5)
# sub
# 

class Calculator:
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
		#cal = {'1':'+', '2': '-', '3':'*', '4': '/', '5': '**'}
		if num2 == 0 and cal_s == '/':
			return 0
		return eval(f"{self.num1} {self.cal_s} {self.num2}")
