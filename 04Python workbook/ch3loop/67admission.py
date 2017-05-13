#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None



total = 0.00
count = 0
while True:
	price = 0
	iN = get_input("input age of guest (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		iN = int(iN)
		try:
			if(iN <= 2):
				price = 0
			elif(iN >=3 and iN <= 12):
				price = 14
			elif(iN >12 and iN < 65):
				price = 23
			else:
				price = 18
				
			print("price=",price)
			total += price
			count += 1
			
		except:
			print('error input')
			# break
	else:
		break

print("average = ", (total/count))