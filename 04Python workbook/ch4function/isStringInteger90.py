def CheckStringIsInteger(s):
	flag = True
	result = s.strip()
	for c in result:
		if( ( not c.isdigit() ) and c!="+" and c!="-"):
			flag = False
	return flag

def main():
	line = input("Enter sentence:")
	while line != "":
		if CheckStringIsInteger(line):
			print('isdigit')
		else:
			print('not')

		line = input("Enter sentence:")

main()
