def findwords(s):
	values = s.split(" ")
	newvalues = []
	for i in values:
		if i.endswith(":") or i.endswith(".") or i.endswith(",") or i.endswith("\n"):
			i = i.replace(":","").replace(".","").replace(",","").replace("\n","")
		newvalues.append(i)

	return newvalues

def main():
	
	s = input("Enter sentences(blank line to quit):")
	while s != "":
		print(findwords(s))
	
		s = input("Enter sentences(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()