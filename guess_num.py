import random

r = random.randint(1, 10)
while True:
	num = input('請猜數字：')
	num = int(num)
	if num == r :
		print('猜中了！')
		break
	elif num > r :
		print('再小一點')
	elif num < r :
		print('再大一點')

