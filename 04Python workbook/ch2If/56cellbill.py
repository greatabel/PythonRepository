#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None
import math


# 4e12 输入例子
while True:
	iN = get_input("input minutes of air time,message count (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		ilist = iN.split(',')
		airtime = float(ilist[0])
		messagecount = int(ilist[1])
		try:
			
			if airtime <= 50 and messagecount <=50:
				air_fee = 15
			else:
				air_fee = 15 + 0.25 * (airtime - 50) + 0.25 * (messagecount - 50) 

			total = 1.05 * (air_fee +0.44 )
			print("total=$",total)
		except:
			print('error input')
			# break
	else:
		break