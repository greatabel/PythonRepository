import math,random

mydic = {'.,?!:':1,'ABC':2,'DEF':3,
	'GHI':4,'JKL':5,'MNO':6,'PQRS':7,
	'TUV':8,'WXYZ':9, ' ':0}
def getMessageInput(theDict,thevalue):
	print('thevalue=',thevalue,theDict.keys())
	inputStr = ''
	for c in thevalue:
		for key in theDict:
			if c in key:
				print("c=",c,"key=",key,"value=",theDict[key])
				myindex = key.find(c) + 1
				print('myindex=',myindex)
				for i in range(myindex):
					inputStr += str(theDict[key])
	return inputStr
	# return returnlist

def main():
	
	thevalue = input("Enter the message (blank line to quit):")

	

	while thevalue!="":
		

		theResult = getMessageInput(mydic,thevalue.upper())
		print('theResult ','-'*20)
		print(theResult)

		thevalue = input("Enter the value you want to reverse loop (blank line to quit):")


	


	
	

        
if __name__ == "__main__":
    main()
