#http://stackoverflow.com/questions/17688587/python-get-sublists
def isSublist(smaller,larger):
	result = False
	for i in  range(len(larger) - len(smaller)):
		print("larger[",i,":i+len(smaller)]",larger[i:i+len(smaller)])
		if larger[i:i+len(smaller)] == smaller:
			result = True
			break
			# print("larger[i:i+len(smaller)",larger[i:i+len(smaller)])
	return result

def main():
	
	smaller = input("Enter smaller list (blank line to quit):")
	larger  = input("Enter larger list (blank line to quit):")
	smaller = smaller.split(",")
	larger = larger.split(",")
	while not (len(smaller)==0 and len(larger)==0):
		print('smaller=',smaller)
		print('larger=', larger)

		print("%s " % isSublist(smaller,larger))

		smaller = input("Enter smaller list (blank line to quit):")
		larger  = input("Enter larger list (blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()