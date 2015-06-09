def  primefactors(x):
	factorlist = []
	fact = 2
	while fact <= x:
		if x % fact == 0:
			x = x/fact
			factorlist.append(fact)
		else:
			fact+=1
	return factorlist

line = input("Enter number you want to factor:")
while line != "":
	num = int(line)

	print("num=",num, "the factorlist=",primefactors(num))
		
	line = input("Enter n:")

