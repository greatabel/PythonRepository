# from collections import Counter
# mylist = [20, 30, 25, 20,20,30]
# [print(k) for k,v in Counter(mylist).items() if v>1]

my_dict = {1:'George Washington', 
2:'Thomas Jefferson'}

def get_input(msg):
	while True:
		try:
			line = input(msg)
			return int(line)
		except:
			# print("unexpected error:",sys.exc_info()[0])
			return None



while True:
	iN = get_input("What's your domination?(enter 'enter' to exit) ")
	if  iN is not None:
		# print(iN)
		if  iN in my_dict.keys():
			print(my_dict[iN])
		else:
			print("don't konw what it is! ")
	else:
		break