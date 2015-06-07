#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

while True:
	iN = get_input("input Rating (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		
		try:
			scale =float(iN)
			if(scale == 0):
				print("Unacceptable performance")
			elif(scale ==0.4):
				print("Acceptable performance")
			elif(scale>=0.6):
				print("Meritorious performance")
			else:
				print("other")
		except:
			print('error input')
			# break
	else:
		break