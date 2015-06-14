# [1,2,3]
# [1],[2],[3]
# [1,2],[2,3]
# [1,2,3]

def generateAllSublist(thelist):
	returnlist = []
	for size in range(1,len(thelist)+1):
		print("size=",size)
		j = 0
		while j <= len(thelist):
			print("j=",j)
			templist = thelist[j:j+size]
			if len(templist )== size:
				print(templist)
				returnlist.append(templist)
			j = j + 1
	return returnlist


def main():
	
	thelist = input("Enter smaller list (blank line to quit):")

	thelist = thelist.split(",")

	while not (len(thelist)==0 ):
		print("the list")

		alllist = generateAllSublist(thelist)
		print('alllist ','-'*20)
		print(alllist)

		thelist = input("Enter smaller list again(blank line to quit):")
		if thelist!="":
			thelist = thelist.split(",")
		else:
			thelist = []
		

	
	

        
if __name__ == "__main__":
    main()