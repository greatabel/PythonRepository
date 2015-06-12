def countElementInRange(ilist,maxV,minV):
	count = 0
	for item in ilist:
		if item > minV and item < maxV:
			count += 1
	print(count)
	return count

def main():
	
	s = input("Enter array (blank line to quit):")

	while s != "":
		mylist = []
		# print('s=',s)
		for item in s.split(','):
			mylist.append(float(item))
		imax = float(input("max:"))
		imin = float(input("min:"))
		print('mylist=',mylist,'max=',imax,'min=',imin)
		print("range count:",countElementInRange(mylist,imax,imin))

		s = input("Enter sentences(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()