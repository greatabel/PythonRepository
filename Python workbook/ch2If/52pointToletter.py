#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

while True:
	iN = get_input("input magnitude (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		
		try:
			scale =float(iN)
			if(scale > 4):
				print("A+")
			elif(scale ==4):
				print("A")
			elif(scale<4 and scale>3.7):
				print("A-")
			else:
				print("other")
		except:
			print('error input')
			# break
	else:
		break