#
# 은행 잔고
# 함수 사용
#

def num_check(num):
	for i in num:
		if i not in "0123456789" :
			print("숫자가 아닙니다. 다시 입력해주세요.")
			return False
		else:
			break
	return int(num)

def bankbook_destruction(num):
	if num == 2:
		print(f"통장을 파기합니다")
		return True
	return 0

money = 10000 
while True:
	if money <= 0:
		print(f"통장잔고가 {money}원입니다, 계속 거래 하시겠습니까? 예:1,아니오:2")
		num = num_check(input())
		if bankbook_destruction(num) :
			break
			
	# 입금,출금 선택		
	first = input("입금? 출금? : ")
	if first not in ['입금', '출금']:
		print("잘못입력하였습니다!")
		continue
		
	# 금액 선택	
	price = input("금액: ")
	price = num_check(price)
	if not price:
		continue
	
	if first == '출금' and money >= price:
		money = money - price
		print(f"{price}원이 출금되었습니다. 현재 잔고는 {money}입니다.")
	elif first =="입금":
		money = money + price
		print(f"{price}원이 입금되었습니다. 현재 잔고는 {money}입니다.")
	else:
		leck = price - money
		print(f"현재 잔고 부족입니다. {leck}가 부족합니다. 현재 잔고는 {money}입니다")
