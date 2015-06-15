def Euclid(a,b):
	if b == 0:
		return a
	else:
		c = a%b
		return Euclid(b,c)

def main():
	ilist = input("enter a,b:")
	while ilist!="":
		ilist = ilist.split(',')
		total = Euclid(int(ilist[0]),int(ilist[1]))
		print(total)
		ilist = input("enter a,b:")

if __name__ == "__main__":
    main()
