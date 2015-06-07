my_dict = {"Jan-01":"New year''s day",
"July-01":"Canada day",
"Dec-25":"Christmas day" }

def get_input(msg):
		try:
			line = input(msg)
			inputlist = line.split(',')
			if(len(inputlist[1]) == 1):
				inputlist[1]= '0'+inputlist[1]
			return inputlist[0]+'-'+inputlist[1]
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None



while True:
	iN = get_input("input month ,day (enter 'enter' to exit) ")
	if  iN is not None:
		# print(iN)
		if  iN in my_dict.keys():
			print(my_dict[iN])
		else:
			print("Just normal day:", iN)
	else:
		break