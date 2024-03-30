driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = int(input('請問你的年齡：'))
if driving == '有':
	if age >= 18 :
		print('你通過測驗了')
	else:
		print('18歲還不能開車喔，不要犯法了')
elif driving >= '沒有':
	if age >= 18:
		print('你可以去駕照囉，快去考吧')
	else:
		print('很好，再過幾年就可以考駕照了')