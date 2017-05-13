#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

while True:
	iN = get_input("input wavelength (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		
		try:
			scale =float(iN)
			if(scale >=380 and scale < 450):
				print("Violet")
			elif(scale >=450 and scale < 495):
				print("Blue")
			elif(scale >= 495 and scale < 570):
				print("Green")
			else:
				print("other")
		except:
			print('error input')
			# break
	else:
		break