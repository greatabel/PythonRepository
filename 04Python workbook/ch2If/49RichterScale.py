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
			if(scale < 2):
				print("Micro")
			elif(scale >=2 and scale < 3):
				print("Very minor")
			elif(scale >=3 and scale <4):
				print("Minor")
			else:
				print("other")
		except:
			print('error input')
			# break
	else:
		break