#
# 자판기
#
menu='''
라떼 (1 shot)
아메리카노 (2 shot)
에스프레소 (3 shot)

**************************************

메뉴 

아메리카노(A를 눌러주세요.)
라떼(L를 눌러주세요.)
에스프레소(E를 눌러주세요.)

**************************************
'''
total = 10
menu1 = {'L':'라떼','A':'아메리카노','E':'에스프레소'}
menu2 = {'L':1,'A':2,'E':3}
while True:
	print("total :", total,"shot")
	pick = input(f"{menu} total : {total}shot\n 선택: ")

	if pick not in ['A', "L", 'E']:
		print("No Menu")
		continue

	if total-menu2[pick] >= 0:
		total -= menu2[pick]
		print("{} 를 선택하셨습니다. {} shot 남았습니다.".format(menu1[pick],total))
	else:
		print("재료가 부족해서 주문 불가합니다")

	if total == 0 :
		print('마감합니다')
		break
'''	
	if  pick == 'E' and total >= 3:
		total -= 3
		print("에소프레소를 선택하셨습니다.")
	elif  pick == 'A' and total >= 2:
		total -= 2
		print("아메리카노 선택하셨습니다.")
	elif pick == 'L' and total >= 1:
		total -= 1
		print("라떼를 선택하셨습니다.")
	else:
		print("재료가 부족해서 주문 불가합니다.")
		continue
'''
