belows = []
averages = []
aboves = []



def main():
	ilist = []
	s = input("Enter first(blank line to quit):")
	while s != "":
		num = int(s)

		ilist.append(num)
	
		s = input("Enter(blank line to quit):")

	averageItem = sum(ilist)/len(ilist)
	print(averageItem)
	
	for item in ilist:
		if item < averageItem:
			belows.append(item)
		elif item == averageItem:
			averages.append(item)
		else:
			aboves.append(item)
	print("belows=",belows)
	print("averages=",averages)
	print("aboves=",aboves)

        
if __name__ == "__main__":
    main()