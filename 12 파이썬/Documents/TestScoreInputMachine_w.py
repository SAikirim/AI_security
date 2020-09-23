#
# 시험성적 입력 프로그램 코딩
# 파일 입력
#

score_season = ['1학기중간', '1학기기말', '2학기중간', '2학기기말']
subject = ['국어', '영어', '수학', '과학', '사회']
subs = []
subss = []
scores = [] 
answer ='y'
#answerr ='y'
f = open("exam.txt", "w")
while True:
	if answer == 'n':
		f.close()
		break
	season = input("입력할 시험 종류 입력 : ")
	i = 0
	while True:
		if not subss:
			sub = input('입력할 과목 : ')
		else:
			print("과목:",subss[i])
		score = input('성적 : ')
		if not subss:
			while True:
				answerr = input('추가로 성적을 입력하시겠습니까?(y or n) : ')
				if answerr in ['y','n']:
					break
		else:
			if i == len(subss)-1:
				answerr = 'n'
			else:
				answerr = 'y'
		subs.append(sub)
		scores.append(score)
		i += 1
		if answerr == 'n':
			if not subss:
				subss = ' '.join(subs)
				f.write("시험 "+ subss +"\n")
				subss = subss.split()
			f.write(season + ' '  + ' '.join(scores) + '\n')
			scores = []
			break
	answer = input('추가로 시험 종류를 입력하시겠습니까?(y or n) : ')
	