#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None





import datetime
from datetime import timedelta
# 4e12 输入例子
while True:
	iN = get_input("input year-month-day (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		ilist = iN.split('-')
		idate = datetime.date(int(ilist[0]),int(ilist[1]),int(ilist[2]))
		print(idate)
		print('next day is:',idate + timedelta(days=1))
	else:
		break