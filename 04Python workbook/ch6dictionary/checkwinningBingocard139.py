from bingoCard138 import CreateBingoCard

def checkWinning(returnlist):
	#测试数据
	# returnlist[0]= {"B":0,"I":0,"N":0,"G":0,"O":0}
	flag = False
	#情况1:一行都为0
	for iDic in returnlist:
		sm = 0 
		for  item in iDic:
			sm += iDic[item]
		if sm == 0:
			flag = True
	#情况2:一列为0:
	columSum = 0
	for i in {'B','I','N','G','O'}:
		print("i=",i)
		for iDic in returnlist:
			columSum += iDic[i]
		if columSum == 0:
			flag = True
	#情况3 左下对角线
	rSum = 0
	mystr = 'BINGO'
	for i in range(0,len(mystr)):
	 	
	 		print("here:",returnlist[i][mystr[i]])
	 		
	 		rSum += returnlist[i][mystr[i]]
	 		i += 1
	if rSum == 0:
  	 	flag = True

	#情况4 右下对角线
	rSum = 0
	mystr = 'BINGO'
	for i in range(0,len(mystr)):
	 	
	 		print("here 2:",returnlist[i][mystr[i]])
	 		
	 		rSum += returnlist[len(mystr)-i-1][mystr[i]]
	 		i += 1
	if rSum == 0:
  	 	flag = True
	return flag

def main():
	resultFlag = False
	while not resultFlag:
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


        
if __name__ == "__main__":
    main()