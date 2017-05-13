import random
def getRandomFromRange(min,max):
	return random.randint(min,max)





def CreateBingoCard():
	returnlist = []

	for i in range(0 , 5):
		mydict = {
	'B': getRandomFromRange(10,15),
	'I': getRandomFromRange(16,30),
	'N':getRandomFromRange(31,45),
	'G':getRandomFromRange(46,61),
	'O':getRandomFromRange(62,77)
				}
		returnlist.append(mydict)
	return returnlist

def main():
	
	returnlist = CreateBingoCard()
	print(returnlist)

        
if __name__ == "__main__":
    main()