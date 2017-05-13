from Anagrams135 import find_Anagrams

def main():
	
	theinputA = input("Enter the messageA (blank line to quit):")
	theinputB = input("Enter the messageB (blank line to quit):")

	

	while theinputA!="" and theinputB!="" :
		theinputA = theinputA.replace(" ","")
		theinputB = theinputB.replace(" ","")
		result = find_Anagrams(theinputA,theinputB)
		print("%s" % result)
		# print('-'* 20)
		
		theinputA = input("Enter the messageA (blank line to quit):")
		theinputB = input("Enter the messageB (blank line to quit):")

        
if __name__ == "__main__":
    main()