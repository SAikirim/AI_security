
# lambda 실습
print("--------------------------------"*3)
print("\n# lambda 실습")

list1 = [1,2,3]
list2 = [3,4,5]

test = lambda x,y:[ i*j for i in x for j in y ]
print(test(list1,list2))
test1 = [ i*j for i in list1 for j in list2 ]
print( test1)