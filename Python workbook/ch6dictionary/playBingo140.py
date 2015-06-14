from bingoCard138 import CreateBingoCard
from checkwinningBingocard139 import checkWinning



def main():

	mycount = 0
	resultFlag = False
	winnings = []
	while (mycount != 10):
		returnlist = CreateBingoCard()
		print(returnlist)

		for i in range(0,len(returnlist)):
			import random
			mystr = 'BINGO'
			myr = mystr[random.randint(0,4)]
			print('i=',i,'test:',myr)
			returnlist[i][myr] = 0
		print("formated:",returnlist)
		resultFlag = checkWinning(returnlist)
		print("%s" % resultFlag)
		if resultFlag:
			mycount += 1
			winnings.append(returnlist)

	print('-'*30)
	print('count=',mycount)
	print(winnings)


        
if __name__ == "__main__":
    main()