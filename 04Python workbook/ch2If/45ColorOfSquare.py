#http://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python
def get_input(msg):
	
		try:
			line = input(msg)
			return line
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None



while True:
	iN = get_input("input a1,b2 things (enter 'enter' to exit) ")
	if  iN is not None and iN !="":
		
		try:
			column = ord(iN[0] ) -ord('a')+1
			row = int(iN[1])
			print(column,row)
			if(((column % 2 == 1 )and ( row %2 ==1)) or (column % 2 == 0) and (row % 2 == 0) ):
				print('black')
			else :
				print('white')
		except:
			print('error input')
			# break
	else:
		break