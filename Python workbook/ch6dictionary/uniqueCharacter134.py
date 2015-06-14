def uniqueCharInStr(theinput):

	inputStr = ''
	from itertools import groupby
	for k,g in groupby(sorted(theinput)):
		print(k,g)
		inputStr +=k

	return inputStr
	# return returnlist
def uniqueCharInStr_Method2(theinput):
	uchars = set()
	for c in theinput:
		if c in uchars:
			continue
		else:
			uchars.add(c)
	return uchars

def uniqueCharInStr_Method3(theinput):
	uchars = {}
	for c in theinput:
		if c in uchars.keys():
			uchars[c] += 1
		else:
			uchars[c] = 1
	return uchars

def main():
	
	theinput = input("Enter the message (blank line to quit):")

	

	while theinput!="":
		

		theResult = uniqueCharInStr(theinput.upper())
		print('theResult ','-'*20)
		print(theResult)
		theResult = uniqueCharInStr_Method2(theinput.upper())
		print('theResult ','-'*20)
		print(theResult)
		theResult = uniqueCharInStr_Method3(theinput.upper())
		print('theResult ','-'*20)
		print(theResult)

		theinput = input("Enter the value you want to reverse loop (blank line to quit):")


        
if __name__ == "__main__":
    main()
