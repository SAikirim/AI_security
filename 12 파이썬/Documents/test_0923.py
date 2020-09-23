subject = ['국어', '영어', '수학', '과학', '사회']
record = [ {0:j} for i, j in enumerate(subject)]
print(record)

# input() 실습
print("--------------------------------"*3)
print("\ninput() 실습")

#data = [ int(input(f"{i}번째 숫자를 입력하시요: ")) for i in range(1, 6)]
data = [1,2,3,4,5]
print(f"모든 숫자를 더한 값은 {sum(data)}이고 평균 {sum(data)/5}입니다.")

# 튜플 실습
print("--------------------------------"*3)
print("\n튜플 ")
tu1=('a1','b1','c1')
tu2=('a2','b2','c2')

tu3 = tu1 + tu2
print(tu3)
print(tu3[3])
print(tu3[2:6])
tu4 = tu3 * 3
print(tu4) 
print(tu4.count('a1'))
print(tu4.index('b2'))
tu5 = tu4 + ([1,2,3],['a','b','c'])
print(tu5)
tu5[-2][0] = 5
tu5[-1][1] = 'd'
print(tu5)

# 딕셔너리 실습
print("--------------------------------"*3)
print("\n딕셔너리 실습 ")
dic={"a":1,"b":2,"c":3,"d":4}

a = [ i for i in list(dic.keys())]
print(a)
print(dic.values())

print( "e" in dic.keys())
print( 5 in dic.values())

#info = {}
#for i in range(5):
#	x, y = input().split()
#	info[x] = y

'''
elements = ['group ', 'name ', 'age', 'area']
info = { i:input(f"{i}:") for i in elements}

for key, value in info.items():
	if key == 'age':
		print(f"내 {key}은 {value}이며 {int(value)//10*10}대입니다.)")
	print(f"내 {key}은 {value} 입니다.)")
'''

# 집합 실습
print("--------------------------------"*3)
print("\n# 집합 실습")

s1= {'a','c','e','b','d','f',1}
s2={1,2,3,'b','d','f'}
string1 = "BOYS, BE AMBITIOUS"
s3 = set(string1.lower())
print(s3)
t1 = s1 & s2
print(t1 & s3)
print(s1 | s2 | s3)
print( s3 - s2 - s1)
s1.update('g','h')
print(s1)
s2.add('A')
print(s2)

# if & while & for
print("--------------------------------"*3)
print("\n# if & while & for")

# 함수 실습
print("--------------------------------"*3)
print("\n# 함수 실습")

test2 = lambda a,b,z : (a+b/z)
print("lambda:",test2(1,2,3))

# 입출력 실습
print("--------------------------------"*3)
print("\n# 입출력 실습")

#1
f1 = open("gu1.txt", 'w')
for i in range(2, 10):
	for j in range(1, 10):
		#print("%d * %d = %d" % ( i, j, i*j), end=" ")
		data = "%d "%(i*j)
		f1.write(data)
f1.close()

#2
f2 = open("gu2.txt", 'w')
for i in range(2, 10):
	for j in range(1, 10):
		print("%d" % (i*j))
		f2.write("%d\n" % (i*j))
f2.close()	

#3
with open('gu1.txt', 'r') as f1:	 
	data1 = f1.readline()
	data2 = data1.split()
print(data2, type(data2))

#4	
#test1 = ".".join(map(str, data2))
print(".".join(data2).split())
#print(test1,type(test1))

