#密碼重試程式
#預設密碼'a123456'，使用者有三次輸入的機會
#輸入錯誤時，印出：密碼錯誤，還有x次機會
#正確時，印出：登入成功

password = 'a123456'

chance = 3
while chance >= 1:
	user_password = input('請輸入密碼：')
	if user_password == password:
		print('登入成功！')
		break
	elif chance == 1:
		print('你沒機會了')
		break
	else:
		chance = chance - 1
		print('密碼錯誤，還有', chance, '次機會')
print('程式結束')
