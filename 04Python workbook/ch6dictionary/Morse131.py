#只是例子，不想打太多
mydic = {'A':'.-', 'B':'-...','C':'-.-.'}

def getMorse(theDict,theinput):
	print('theinput=',theinput,theDict.keys())
	inputStr = ''
	for c in theinput:
		#如果字典中包含该字符
		if c in theDict.keys():
			inputStr += theDict[c]
	return inputStr
	# return returnlist

def main():
	
	theinput = input("Enter the message (blank line to quit):")

	

	while theinput!="":
		

		theResult = getMorse(mydic,theinput.upper())
		print('theResult ','-'*20)
		print(theResult)

		theinput = input("Enter the value you want to reverse loop (blank line to quit):")


	


	
	

        
if __name__ == "__main__":
    main()
