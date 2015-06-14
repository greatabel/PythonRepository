# [1,2,3]
# [1],[2],[3]
# [1,2],[2,3]
# [1,2,3]
mydic = {1:"one test",2:"two",3:"three",4:"test",5:"test"}
def ReverseLoop(theDict,thevalue):
	mykeys = []
	# for k,v in theDict.items():
	# 	print(k,"=",v)
	# 	if v == thevalue:
	# 		mykeys.append(k)


	# 答案中的方法
	for key in theDict:
		if theDict[key] == thevalue:
			mykeys.append(key)
	return mykeys
	# return returnlist


def main():
	
	thevalue = input("Enter the value you want to reverse loop (blank line to quit):")

	

	while thevalue!="":
		

		theResult = ReverseLoop(mydic,thevalue)
		print('theResult ','-'*20)
		print(theResult)

		thevalue = input("Enter the value you want to reverse loop (blank line to quit):")


	
	

        
if __name__ == "__main__":
    main()
