from random import randrange


	
def round():
	value = randrange(0,38)
	if value == 37:
		print("THe spin results in 00...")
	else:
		print("result %d ..." % value)

	if value == 37:
		print("pay 00")
	else:
		print("pay ", value)

	if  value % 2 ==1 and value >=1 and value <= 9 or \
		value % 2 ==0 and value >=12 and value <= 18 :
		print("pay red")
	elif value == 0 or value == 37:
		pass
	else:
		print("pay black")

	if value >=1 and value <=36:
		if value % 2 ==1:
			print("odd")
		else:
			print("even")

	if value >= 1 and value <= 18:
		print(" 1- 18")
	elif value >= 19 and value <= 36:
		print(" 19 - 36")


for i in range(1, 5):
	print("round --> ", i)
	round()
	print()