#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

# import calendar
month_dict = {"Jan":1,"Feb":2,"Mar":3,"Apr":4, "May":5, "Jun":6, 
"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12} 

def to_dict(name): 
	return month_dict[name] 

while True:
	iN = get_input("input month(string) ,day(integer) (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		
		try:
			iList = iN.split(',')
			print(iList)
			mymonth = iList[0]
			myday = int(iList[1])
			print(mymonth,myday)
			if( mymonth in month_dict.keys() ):
				print(month_dict[mymonth],myday)
				mymonth = month_dict[mymonth]
				if ((mymonth < 3) or (mymonth == 3 and myday <=20)):
					print("Spring")
				elif((mymonth >=3 and mymonth < 6) or (mymonth == 6 and myday <=21)):
					print("Summer")
				elif ((mymonth >=6 and mymonth < 9) or (mymonth == 9 and myday <=22)):
					print("Fall")
				else:
					print("Winter")
			else :
				print('No such month name!')
		except:
			print('error input')
			# break
	else:
		break