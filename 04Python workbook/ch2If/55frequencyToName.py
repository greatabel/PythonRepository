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
	iN = get_input("input frequency (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		
		try:
			scale =float(iN)
			if(scale < 3 * pow(10,9)):
				print("Radio waves")
			elif(scale >=3 * pow(10,9) and scale < 3 * pow(10,12)):
				print("Microwaves")
			elif(scale >= 3 * pow(10,12) and scale < 4.3 * pow(10,14)):
				print("Infrared light")
			else:
				print("other")
		except:
			print('error input')
			# break
	else:
		break