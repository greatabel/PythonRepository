line = input("Enter n,m of n/m:")
while line != "":
	ilist = line.split(',')
	n = int(ilist[0])
	m = int(ilist[1])
	print(n,m)
	common = 1
	for i in range(1,n+1):
		if(n% i == 0 and m%i ==0):
			common = i
	
	print("common=",common)	
	print(n//common,"/",m//common,"is the reduced.")
	line = input("Enter n,m:")
