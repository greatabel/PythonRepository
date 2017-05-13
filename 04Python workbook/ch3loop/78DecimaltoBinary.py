line = input("Enter n:")
while line != "":
	bN = ""
	mylist = []
	xN = int(line)
	while xN >=1:
		if xN % 2 == 0:
			reminder = 0
		else:
			reminder = 1
		print("reminder=",reminder)
		xN =xN/2
		mylist.append(reminder)

	for item in reversed(mylist):
		bN+=str(item)
	print(str(bN))


	line = input("Enter n:") 

