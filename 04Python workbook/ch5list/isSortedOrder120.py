def countElementIn(ilist):
	if ilist == sorted(ilist):
		return True
	else:
		return False

def main():
	
	s = input("Enter sentences(blank line to quit):")
	while s != "":
		mylist = []
		for item in s.split(','):
			mylist.append(int(item))
		print('mylist=',mylist)
		print("is sorted:",isSortedList(mylist))

		s = input("Enter sentences(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()