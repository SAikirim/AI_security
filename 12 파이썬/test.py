list1=[]
dic1={}
i=0

while i<4:
    for i in [1,2]:
        key1=input("{}key를 입력하시오. : ".format(i))
        value1=input("{}value를 입력하시오. : ".format(i))
        dic1[key1]=value1
    list1.append(dic1)
    print(list1)
    i=i+1