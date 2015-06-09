from random import randrange
line = input("Enter how many times:")
while line != "":
	ilist = []
	for rand in range(0,int(line)):
		myrandom = randrange(0,2)
		ilist.append(myrandom)
		if myrandom == 0:
			print('T')
		else:
			print('H')
	print(ilist)

	from itertools import groupby
	grouped_L = [(k,sum(1 for i in g)) for k,g in groupby(ilist)]
	print(grouped_L)
	for item in grouped_L:
		# print(item)
		if(item[1]>=3):
			print(item[0], "show up ", item[1],"times")
	line = input("Enter how many times:")




