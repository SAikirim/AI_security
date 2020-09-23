# 7.
print("\n7.")
string ='''
이 문장은 출력이 됩니다.
주석은
실행되지 않습니다.
이 문장도 출력이 됩니다.
'''
print("--------------------------")
print(string[7:15])
print(string[7:15])
print("--------------------------")

# 8. if 실습
print("\n8. if")
srp = '가위'
for i in range(1):	
	if srp == '가위':
		print("이겼다")
	elif srp == '바위':
		print('졌다')
	elif srp == '보':
		print('비겼다')
	else:
		print('잘못냈다')		

# 9. for
print("\n9. for")
seasons =  ['봄','여름','가을','겨울']
for i in seasons:
	if seasons == '봄':
		print(f"현재 계절은 {i} 입니다")
	else:
		print(f"현재 계절은 {i}이 아닙니다.")
		
# 10. while
print("\n10. while")
num = 0
while num <= 100:
	if num == 55:
		print("일치", num)
	else:
		print("불일치", num)
	num += 5
	
# 11. 함수 실습
print("\n11. 함수 실습")
def SRP(srp):
	if srp == '가위':
		print("이겼다")
	elif srp == '바위':
		print('졌다')
	elif srp == '보':
		print('비겼다')
	else:
		print('잘못냈다')		

SRP("가위")

# ---------------------------------------------
print( "\n# 자료형 실습")
print( "17: ", bin(17), oct(17), hex(17))

print(14%10)
print(4**20)
print(132//25)

print( "\n# 자료형 실습")
a = 'abcedf'
b = '12345'

c=a+b
print(c)
print(b*3)
print(c[2])
print(c[2], c[4], c[7])
print(c[3]+c[6:8])
print(c[-4])
print(c[2:])
print(c[3:8])
print(c[-6:-2])
print(c[:])

print( "\n# 문자열 포맷팅 실습(% 를 이용한 문자열 포맷팅)")
print("나는 아침마다 %d잔의 우유를 마시고 %s를 봅니다." % (1, '네이버뉴스'))
print("=%-14s=" % 'hello')
print("=%10s=" % 'bye')
print("%0.5f" % 2.5679856)
print("=%15.3f=" % 2.5679856)

print( "\n# 문자열 함수 실습)")
string1 = "My life is mine."
string2 = string1.upper()
print(string2)
string3 = string2.lower()
print(string3)
string4 = string1.swapcase()
print(string4)
print(string2.count("m"))
print(string3.find("M"))

print( ';'.join("12345"))
string4 = string1.replace("My", "Your")
print(string4)
print("192.168.100.40".split('.'))
print(','.join("abcdef").split(","))	# 암기
print(list("abcdef"))

# ---
# 리스트 실습
print("# list 실습")
number=[1,2,3,4,5,6,7,8,9,10]
alpha=['a','b','c','d','e']
numalp = number + alpha

print(numalp)
del numalp[8:11]
print(numalp)
#numalp.insert(7,[11,12,13])
numalp[7] = [11,12,13]
#numalp.insert(7,13)
#numalp.insert(7,12)
#numalp.insert(7,11)
print(numalp)
numalp[0:3] = [21, 22, 23]
print(numalp)
numalp.append(100)
print(numalp)
number = []
print(number)
numalp = list(map(str, numalp))
numalp.sort()
print(numalp)
numalp.reverse()
print(numalp)
#numalp.insert(2, ['ㄱ','ㄴ','ㄷ'])
numalp.insert(2, 'ㄷ')
numalp.insert(2, 'ㄴ')
numalp.insert(2, 'ㄱ')
print(numalp)
print(numalp.pop(2))
print(numalp.pop(2))
print(numalp.pop(2))
print(numalp)
numalp_tmp = []
for i in numalp:
	numalp_tmp.insert(0, i)
numalp = numalp_tmp
print("reverse: ",numalp)
#print(sorted(numalp, reverse=True))
alpha3 = alpha*3
print("".join(sorted(alpha3)))

# ---

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1)

for i in array:
	count[i] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')
