def find_Anagrams(theinputA,theinputB):
	theinputA = sorted(theinputA)
	theinputB = sorted(theinputB)
	if theinputA == theinputB :
		return True
	else:
		return False

def find_Anagrams_Method2(theinputA,theinputB):
	dictA = {}
	dictB = {}
	for c in theinputA:
		if c in dictA.keys():
			dictA[c] += 1
		else:
			dictA[c] = 1
	for c in theinputB:
		if c in dictB.keys():
			dictB[c] += 1
		else:
			dictB[c] = 1

	print(dictA,dictB)

	
	if dictA == dictB :
		return True
	else:
		return False

def main():
	
	theinputA = input("Enter the messageA (blank line to quit):")
	theinputB = input("Enter the messageB (blank line to quit):")

	

	while theinputA!="" and theinputB!="" :
		
		result = find_Anagrams(theinputA,theinputB)
		print("%s" % result)
		print('-'* 20)
		result = find_Anagrams_Method2(theinputA,theinputB)
		print("%s" % result)
		theinputA = input("Enter the messageA (blank line to quit):")
		theinputB = input("Enter the messageB (blank line to quit):")

        
if __name__ == "__main__":
    main()