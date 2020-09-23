#
# 과일전문 요리점
#

menu ='''
종류        	수량        금액
사과파이		5         5000
사과쥬스		2         2000
사과			1         1000
'''
menu2='''
-----------------------------
종류        금액	사용하는 양
1.사과파이 : 5000	5
2.사과쥬스 : 2000	2
3.사과	: 1000	1
----------------------------
'''
stock = 30
store = {'1': (5000, 5), '2':(2000,2), '3': (1000,1)}

print(menu)
while True:
	print(menu2)
	print(f"사과재고:{stock}개")
	choce = input("메뉴를 선택하시오(번호를 누르시오) : " )
	if choce not in [ '1', '2', '3']:
		continue
	try:
		money = int(input("돈을 내시오 : "))
	except:
		continue
	
	if stock == 0:
		print("해당 재고가 없습니다.\n 마감합니다.")
		break
	if money < store[choce][0] or stock < store[choce][1]:
		print(f"돈 또는 재고가 부족합니다. \n남은재고:{stock}개\n요리가격:{store[choce][0]}")
		continue
	else:
		stock -= store[choce][1]
		change = money - store[choce][0]
		print(f"요리 나왔습니다. 거스름돈은 {change}입니다.")
		
	
		
	
