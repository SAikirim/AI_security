#
# 명부 입력
#

menu='''
---------
명부 편집
1. 정보 입력
2. 정보 확인
3. 정보 수정
4. 나가기(저장)
----------
번호를 선택하시오: '''

menu2='''
원하는 항목 선택
1.생년월일
2.전화번호
3.지역
'''

def input_list(name, sex, b_date, p_num, area):
	global lists
	lists.append({"name":name, 'sex': sex, 'b_date': b_date, 'p_num': p_num, 'area': area}) 

def sex_check(sex):
	if not sex:
		return '남'
	return sex

def age_check(age):
	tmp = []
	for i in age:
		if i in "0123456789" :
			tmp.append(i)
	tmp = ''.join(tmp)
	if len(tmp) == 8:
		b_date = tmp[0:4]+'/'+tmp[4:6]+'/'+tmp[6:8]
	elif len(tmp) == 6:
		b_date = "19"+tmp[0:2]+'/'+tmp[2:4]+'/'+tmp[4:6]
	else:
		print("잘못입력하셨습니다.")
		return False
	age = 2020 - int(b_date[0:4])
	return age, b_date

def p_num_check(p_num):		
	tmp = []
	for i in p_num:
		if i in "0123456789" :
			tmp.append(i)
	tmp = ''.join(tmp)
	if len(tmp) == 11:
		p_num = tmp[0:3]+'-'+tmp[3:7]+'-'+tmp[7:11]
	elif len(tmp) == 10:
		p_num = "19"+tmp[0:3]+'-'+tmp[3:6]+'-'+tmp[6:10]
	else:
		print("잘못입력하셨습니다.")
		return False
	return p_num

def save(list):
	with open('Info_List.txt', "w") as f:
		for i in list:
			f.write(f"{i['name']},{i['sex']},{i['b_date']},{i['p_num']},{i['area']}\n")

def load():
	global lists
	with open('Info_List.txt', "r") as f:
		for i in f.readlines():
			i = i[:-1]
			i = i.split(',')
			lists.append({"name":i[0], 'sex': i[1], 'b_date': i[2], 'p_num': i[3], 'area': i[4]}) 
	
def find_list(f_name):
	global lists
	for i in lists:
		if f_name == i['name']:
			print( '이름:',i['name'])
			print( '성별:',i['sex'])
			print( '생년월일:',i['b_date'])
			print( '전화번호:',i['p_num'])
			print( '지역:',i['area'])

def modi_list(f_name):
	global lists
	for index, i in enumerate(lists):
		if f_name == i['name']:
			print( '이름:',i['name'])
			print( '성별:',i['sex'])
			print( '생년월일:',i['b_date'])
			print( '전화번호:',i['p_num'])
			print( '지역:',i['area'])
			# 수정
			print(menu2)
			choice = input("원하는 항목 선택: ")
			if choice == '1':
				age, lists[index]['b_date'] = age_check(input('생년월일: '))
			elif choice == '2':
				lists[index]['p_num'] = p_num_check(input('전화번호: '))
			elif choice == '3':
				lists[index]['area'] = input('지역: ')
			else:
				print("잘못입력하셨습니다.")
				continue
			
lists = []
load()
while True:
	m_choice = input(menu)
	if m_choice not in '1234':
		print("잘못입력하셨습니다.")
		continue
	
	if m_choice == '1':
		name = input('이름: ')
		#sex = input('성별:')
		sex = sex_check(input('성별: '))
		#b_date = input('생년월일: ')
		age, b_date = age_check(input('생년월일: '))
		# = input('전화번호: ')
		p_num = p_num_check(input('전화번호: '))
		area = input('지역: ')
		#with open('Info_List.txt', "w") as f:
		#	f.write(f"{name},{sex},{b_date},{p_num},{area}")
		input_list(name, sex, b_date, p_num, area)
		print(lists)
	elif m_choice == '2':
		find_name = input("이름으로 검색: ")
		find_list(find_name)
	elif m_choice == '3':
		find_name = input("이름으로 검색: ")
		modi_list(find_name)
		print(lists)
	else:
		save(lists)
		break
# '서울'라인만 출력		
for index, i in enumerate(lists):
	if i['area'] == '서울':
		print(index, i)