# 변수 선어
print("\n변수 선언")

name, age, birthday = "임", "10", "23"#input().split()
print(f"나의 이름은 {name}입니다.")
print(f"나의 나이는 {int(age)}이며 {int(age)//10*10}대입니다.")
print(f"나의 생일은 {birthday}입니다.")

# 요일
print("\n솔로몬 그런디!")

week=['월','화','수','목','금','토','일']
print("솔로몬 그런디는")
for day in week:
	if day == '월':
		print("월요일에 태어나서")
	if day == '화':
		print("화요일에 세례받고")
	if day == '수':
		print("수요일에 결혼하고")
	if day == '목':
		print("목요일에 병들어서")
	if day == '금':
		print("금요일에 악화되어")
	if day == '토':
		print("토요일에 눈을 감아")
	if day == '일':
		print("일요일에 묻혔다네")
print("솔로몬 그런디는")
print("그렇게 살다 갔네")

# 50
print("\n50")

for i in range(50):
	print(i, "Victory")
	
# 함수
print("\n함수")
def average(x,y,z):
	return (x+y+z)/3
print(average(1,2,3))

# num
print("\nnum")
num1 = 40
num2 = 30
print(bin(num1*num2), oct(num1*num2), hex(num1*num2))

# string
print("\nstring")
string1 = "My life"
string2 = " is mine." 
string3 = string1+string2
print(string3)
print(string3[:7])
string4 = string3[-5:-1]
print(string4)

# 문자열 포매팅 실습
print("\n문자열 포매팅 실습")
print("나는 %s %s 시험을 보았다." % ("오늘", "영어") ) 
print("나의 점수는 %d점으로 상위 %.1f%% 점수이다." % (98, 0.1))
#print('''나는 %s %s 시험을 보았다. 
#나의 점수는 %d점으로 상위 %.1f%% 점수이다.''' % ("오늘', "영어", 98, 0.1))

day = 'today'
print( "=%9s=" % day)
print( "=%-14s=" % day)

float1 = 1.2345678 
print( "=%8.5f=" % float1)
print( "=%-10.4f=" % float1)

# 문자열 함수 실습
print("\n문자열 함수 실습")
alph = "abcd efg hijk lmnop qrs tuv wxyz"
number = "1234 567 89"
boy = "BOYS, BE AMBITIOUS"
alph1 = alph.upper()
string1 = boy + alph1
print(string1)
print(string1.count("B"))
print(string1.find("A"))
string2 = boy.replace("BOYS", "girls")
print(string2)
print(string2.swapcase())
alphlist = " ".join(alph).split()
print(alphlist)

# --------------------------------
# list 실습
print("--------------------------------"*3)
print("\nlist 실습")

num1="0,1,2,3,4,5,6,7,8,9,10"
num2 = list(num1.split(','))
print(num2)
print(num2[2])
print(num2[4:8])
print(int(num2[4])*int(num2[6]))
num2[5] = '45'
print(num2)
num2[2:8] = ['31','33','34','35','36','37' ]
print(num2)
num2[8] = '33'
print(num2)
while True:
	if num2.count('33') == 0:
		break
	num2.remove('33')
print(num2)
num2.sort()
num2.reverse
num2.insert(3,['a1','b1','c1'])
print(num2)
num2[4] = ['a2','b2','c2']
print(num2)
a1 = num2.pop(num2.index(['a1','b1','c1']))
print(a1, num2)
num2.remove(['a2','b2','c2'])
print(num2)
print(list(map(int, num2)))
print( num2[num2.index('9')])

# 튜플 실습
print("--------------------------------"*3)
print("\n 튜플 실습")
a=('a1','a2','a3','a4')
b=('b1','b2','b3','b4')

q, w, e, r = a
print(q, w, e, r)
c = a + b
print(c)
print(c[2])
print(c[5:])
print(c[:3])
#del c[3] 
#c[4] = 'c1'
d = ('a','b','c',[1,2,3,4]) 
d[3][0] = '1'
d[3][1] = '2'
print(d)

# 딕셔너리 실습
print("--------------------------------"*3)
print("\n딕셔너리 실습")
srp={'가위':'보','바위':'가위','보':'바위'}

print(srp.keys())
print(srp.values())
print(srp.items())
print(srp['가위'])
test =('찌','빠'), ('묵','찌'), ('빠','묵')
#srp = {i: j for i, j in test}
for i, j in test :
	srp[i] = j
print(srp)
print( srp.get('보자기', '없음'))
print('보자기' in srp)
# '보자기' in srp.keys()
#1
print(":",list(srp.keys())[list(srp.values()).index('가위')])
#2,3
'''
for i in srp.keys():
	if srp.get(i) == '가위':
		print(i)
'''
for i, j in srp.items():
	if j == '가위':
		print(i,":",j)

Key=['a','b','c','d']
Value=[1,2,3,4]
test ={}
for i, j in enumerate(Key):
	test[j]=Value[i]
print(test)
	
# set 실습
print("--------------------------------"*3)
print("\nset 실습")
a = [1,2,3,4]
b = "aabbccddeeff"
s1 = set(a)
s2 = set(b)
print(s1,"\n",s2)
s1.update('a','b','c' )
print(s1,"\n",s2)
s2.add(1)
print(s1,"\n",s2)
print(s1&s2)
print(s1.intersection(s2))
print(s1|s2)
print(s1.union(s2))
print(s1-s2)
print(s2.difference(s1))
s2.remove(1)
print(s1,"\n",s2)

# if & for & while 실습
print("--------------------------------"*3)
print("\nif & for & while 실습")

while True:
	try:
		test = input('숫자만 입력: ')
		test2 = int(test)
		print(test2)
		break
	except:
		print("ERROR :", test )
		continue