#只是例子，不想打太多
mydic = {'A':'Newfoundland', 'B':'Nova Scotia','C':'Prince Edward Island'
	,'E':'New Brunswick','GHJ':'Oquebec','KLMNP':'Ontario','R': 'Manitoba'}


def getPostCodeAccordingAddress(theDict,theinput):
	print('theinput=',theinput,theDict.keys())
	inputStr = ''
	
	#如果字典中包含该字符
	for key in theDict:
		if theinput[0] in key:
			inputStr +='province:'+theDict[key]
	# print('theinput[1]=',theinput[1],(theinput[1]== 0))
	if int(theinput[1]) == 0:
			
			inputStr += ' rural'
	else:
			inputStr += ' urban'

	return inputStr
	# return returnlist

def main():
	
	theinput = input("Enter the message (like G2G blank line to quit):")

	

	while theinput!="":
		

		theResult = getPostCodeAccordingAddress(mydic,theinput.upper())
		print('theResult ','-'*20)
		print(theResult)

		theinput = input("Enter the value you want to reverse loop (blank line to quit):")


	


	
	

        
if __name__ == "__main__":
    main()
