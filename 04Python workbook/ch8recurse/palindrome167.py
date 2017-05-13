def isP(s):
	
	if s == "":
		return True
	else:
		return s[0] == s[len(s) -1 ] and isP(s[1:len(s)-1])

def main():
	ilist = input("enter string:")
	while ilist!="":
		
		result = isP(ilist)
		print("%s " %result)
		ilist = input("enter string:")

if __name__ == "__main__":
    main()
