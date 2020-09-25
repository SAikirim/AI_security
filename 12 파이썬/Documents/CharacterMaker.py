#
# 캐릭터 만들기
#

menu1='''1. {}
2. {}
3. {}'''

pow = 10
dex = 10
inte= 10

class Maker:
	def __init__(self, name, pow, dex, inte, job, skill):
		self.name = name
		self.pow = pow
		self.dex = dex
		self.inte = inte
		self.job = job
		self.skill = skill
	
	def show(self):
		print('''
캐릭터명:{}
직업:{}
힘:{}
민첩:{}
지능:{}
스킬:{}'''.format(self.name,self.job,self.pow,dex,self.inte,self.skill))
		
jobs = {'전사':1, '도적':2, '마법사':3,}
skills = [{1:'베기', 2: '찌르기', 3: '대쉬'},	# 전사
		{1:'암살', 2: '은신', 3: '훔치기'},	# 도적
		{1:'불', 2: '물', 3: '바람'}]		# 마법사
		

while True:
	name = input("캐릭터 이름: ")
	obj=[name]

	while True:
		pow = int(input("캐릭터 힘: "))
		dex = int(input("캐릭터 민첩: "))
		inte = int(input("캐릭터 지능: "))
		if (pow + dex + inte) > 30:
			print("수치의 총합이 30이하로 되게하세요!")
			continue
			
		if pow > dex and pow > inte:
			job = '전사'
		elif dex > pow and dex > inte:
			job = '도적'
		else:
			job = '마법사'
		
		if job:
			print(f"\n당신은 {job}입니다.") 
			print(menu1.format(skills[jobs[job]-1][1], skills[jobs[job]-1][2], skills[jobs[job]-1][3]))
			skill = int(input('스킬을 선택하세요: '))
			skill = skills[jobs[job]-1][skill]
			print(skill)
		obj[0] = Maker(name, pow, dex, inte, job, skill)
		obj[0].show()
		break
		