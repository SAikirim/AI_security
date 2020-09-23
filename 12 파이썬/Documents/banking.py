# 은행 잔고

money = 10000 
while True:
	if money <= 0:
		break
	first = input("입금? 출금? : ")
	if first not in ['입금', '출금']:
		print("잘못입력하였습니다!")
		continue
	price = int(input("금액: "))
	
	if first == '출금' and money >= price:
		money = money - price
		print(f"{price}원이 출금되었습니다. 현재 잔고는 {money}입니다.")
	elif first =="입금":
		money = money + price
		print(f"{price}원이 입금되었습니다. 현재 잔고는 {money}입니다.")
	else:
		leck = price - money
		print(f"현재 잔고 부족입니다. {leck}가 부족합니다. 현재 잔고는 {money}입니다")

print(f'통장잔고가 {money}원이 되면 "통장을 파기합니다"') 