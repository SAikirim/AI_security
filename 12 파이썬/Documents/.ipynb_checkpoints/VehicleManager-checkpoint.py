#
# 차량 등록, 검색
#

#import pickle

menu= '''
A.차량등록
B.차주검색
C.나가기
'''

class CarMaker:
	def __init__(self, owner, color, kind):
		self.owner = owner
		self.color = color
		self.kind = kind 
	
	def kinds(self):
		if self.kind == 'sports' :
			self.cc = '5000cc'
			self.drive = '후륜'
			self.m_speed = '300km/h'
		elif self.kind == 'suv':
			self.cc = '3000cc'
			self.drive = '4륜'
			self.m_speed = '200km/h'
		elif self.kind == 'truck':
			self.cc = '6000cc'
			self.drive = '4륜'
			self.m_speed = '200km/h'
		else:
			print("차종이 잘못 되었습니다.")
			return False
	
	def show(self):
		print('''
차량주인 : {}
차량색깔 : {}
차종 : {}
배기량 : {}
구동 : {}
최고속도 : {}
'''.format(self.owner, self.color, self.kind, self.cc, self.drive, self.m_speed))

car_list = {}
#with open('test.p', 'rb') as file:
#	car_list = pickle.load(file)

while True:
	print(menu)
	m_choice = input("선택: ")
	if  m_choice not in "ABabCc":
		continue
	
	if m_choice in "Aa":
		car_owner = input("차주: ")
		car_list[car_owner] = len(car_list)
		#obj = [car_owner]
		car_color = input("색깔: ")
		car_kind = input("차종(sports,suv,truck 중 택일): ")
		car_list[car_owner] = CarMaker(car_owner, car_color, car_kind)	# obj[0] =
		if False == car_list[car_owner].kinds():
			continue
		car_list[car_owner].show()
		print(car_list)
	elif m_choice in "Bb":
		car_owner = input("차주 검색: ")
		if car_owner not in car_list:
			print("차주가 없습니다.")
			continue
		#obj = [car_owner]
		car_list[car_owner].show()
	else:
		#with open('test.p', 'wb') as file:
		#	pickle.dump(car_list, file)
		break