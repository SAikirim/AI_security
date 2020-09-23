#
# 평균 성적
#

subject = ['국어', '영어', '수학', '과학', '사회']
record = {i:int(input(f"{i}:")) for i in subject} 
print(record)
print("60점 이상 점수: ", end=" ")
for i, j in record.items():
	if j >= 60 :
		print(i, end=" ")
print("\n")
print( sum(record.values())/len(subject))		