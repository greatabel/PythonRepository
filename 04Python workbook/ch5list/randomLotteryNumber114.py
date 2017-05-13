import random
def generateLotteryNumber():
	result = ""
	mylist = []
	for i in range(6):
		myrandomInt = random.randint(1,49)
		mylist.append(myrandomInt)

	return ' '.join(str(x) for x in sorted(mylist))

def main():
	
	# s = input("Enter sentences(blank line to quit):")
	for i in range(10):
		print(generateLotteryNumber())
	
		# s = input("Enter sentences(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()