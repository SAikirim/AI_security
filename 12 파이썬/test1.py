import copy

list1=[]
dic1={}
i=0
while i<5:
    for i in [1,2]:
        key1=input("{}key를 입력하시오. : ".format(i))
        value1=input("{}value를 입력하시오. : ".format(i))
        dic1[key1]=value1
    dic2=dic1.copy()
    list1.append(dic2)
    print(list1)
    i=i+1