#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
		try:
			line = input(msg)
			
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None

# import calendar
LetterToPoint = {"A+":4.0,"A":4.0,"A-":3.7,
"B+":3.3, "B":3.0,"B-":2.7 } 

def to_dict(name): 
	return LetterToPoint[name] 

total = 0.00
count = 0
while True:
	iN = get_input("input Letter of point (enter 'enter' to exit): ")
	if  iN is not None and iN!="":
		iN = iN.upper()
		try:
			if(iN in LetterToPoint.keys()):
				print(LetterToPoint[iN])
				total += LetterToPoint[iN]
				count += 1
			else:
				print("don't know")
			
		except:
			print('error input')
			# break
	else:
		break

print("average = ", (total/count))