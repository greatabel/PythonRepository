#不明白题意

def loadNames():
	return ["A",12,"B",4,"A",2]

def DecodeRun(ilist):
	returnStr = ''
	if len(ilist) == 0:
		return returnStr
	elif len(ilist) >=2:
		first = ilist[0]
		second = ilist[1]
		returnStr += first * int(second)
		# print(returnStr)
		return returnStr + DecodeRun(ilist[2:])

	

def main():
	
	sequence = DecodeRun(loadNames())
	print(sequence)

if __name__ == "__main__":
    main()



