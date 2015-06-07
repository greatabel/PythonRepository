#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None
import math



#方法2
def leapyr(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False


# 4e12 输入例子
while True:
	iN = get_input("input year (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		print(leapyr(int(iN)))
		#方法2
		import calendar
		print('method2 calendar=',calendar.isleap(int(iN)))
	else:
		break