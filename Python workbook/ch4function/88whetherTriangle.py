def checkTriangle(a,b,c):
	flag = False
	if (a+b>=c and a+c>=b and b+c>a):
		flag = True
	
	return flag

def main():
	line = input("Enter a,b,c:(triangle):")
	while line != "":
		ilist = line.split(',')
		a = float(ilist[0])
		b = float(ilist[1])
		c = float(ilist[2])
		if checkTriangle(a,b,c):
			print("Is")
		else:
			print("Not")

		line = input("Enter a,b,c:(triangle):")

main()
