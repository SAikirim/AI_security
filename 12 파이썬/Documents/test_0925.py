
# 예외처리 실습
print("--------------------------------"*3)
print("\n# 예외처리 실습")

##
# test_0925.ipynb 참조
##


# 외장함수 실습
print("--------------------------------"*3)
print("\n# 외장함수 실습")

import os
import time
import pickle
import random
'''
#4
with open("./doit/test1/srp.txt", 'wb') as f:
	data = ['가위','바위','보']
	pickle.dump(data,f)

# 5
srp_l = [ input(f"{i+1}번째: ") for i in range(10)]
with open("./doit/test1/srpuse.txt", 'wb') as f:
	pickle.dump(srp_l,f)
'''
# 6
with open("./doit/test1/srp.txt", 'rb') as f:
	data = pickle.load(f)
	
with open("./doit/test1/srpuse.txt", 'rb') as f:
	srp_l = pickle.load(f)

srp_win={'가위':'바위','바위':'보','보':'가위'}
win, lose, draw = 0,0,0
for idx, i in enumerate(srp_l):
	t_data = random.choice(data)
	if srp_win[i] == t_data:
		print("승리")
		win += 1
	elif srp_l[idx] == t_data:
		print("비겼습니다")
		draw += 1
	else:
		print("잘못내셨거나 패배하였습니다.")
		lose += 1
print(f"{win}승 {lose}패 {draw}비김")