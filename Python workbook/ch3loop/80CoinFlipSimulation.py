from random import randrange

CoinDic = {0:"H",1:"T"} 

def to_dict(name): 
	return CoinDic[name] 

line = input("Enter how many times:")

while line != "":
	times = 0
	total = 0
	times = int(line)
	for rand in range(0,times):
		flag = True
		ilist = []
		while flag: 
			myrandom = randrange(0,2)
			ilist.append(myrandom)

			print(to_dict(myrandom),end="")
			if(len(ilist)>=3):
				if(ilist[len(ilist)-1]==ilist[len(ilist)-2]==ilist[len(ilist)-3]):
					print(to_dict(ilist[len(ilist)-1]),"conpleted at",len(ilist),"times")
					flag = False
					total += len(ilist)
					break
		print(ilist)
	print("%d times ----average:%.02f" %(times,total/times))

	line = input("Enter how many times:")






