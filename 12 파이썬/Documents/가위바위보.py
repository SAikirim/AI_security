#
# 가위, 바위, 보
#

srp1=['가위','바위','바위','바위','보','가위','가위','보','가위','보']
srp_win={'가위':'바위','바위':'보','보':'가위'}
win, lose, draw = 0,0,0
for i in srp1:
	player = input("가위바위보!")

	if player == srp_win[i]:
		print("승리")
		win += 1
	elif player == i:
		print("비겼습니다")
		draw += 1
	else:
		print("잘못내셨거나 패배하였습니다.")
		lose += 1
print(f"{win}승 {lose}패 {draw}비김")