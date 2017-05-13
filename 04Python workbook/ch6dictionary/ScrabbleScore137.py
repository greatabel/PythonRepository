mydict = {
	'AEILNORSTU':1,
	'DG':2,
	'BCMP':3,
	'FHVWY':4,
	'K':5,
	'JX':8,
	'QZ':10
}

def score(theInput):
	total = 0
	for c in theInput:
		for key in mydict:
			if c in key:
				total += mydict[key]
	return total

def main():
	
	theinputA = input("Enter the messageA (blank line to quit):")
	
	

	while theinputA!=""  :
		result = score(theinputA.upper())
		print("%s" % result)
		# print('-'* 20)
		
		theinputA = input("Enter the messageA (blank line to quit):")


        
if __name__ == "__main__":
    main()