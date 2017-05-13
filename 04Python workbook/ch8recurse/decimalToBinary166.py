def dec2bin(n):
	if n < 0:
		return 'error input'
	elif n == 0:
		return ''
	else:
		return dec2bin(n//2) + str(n%2)

def main():
	ilist = input("enter n:")
	while ilist!="":
		
		total = dec2bin(int(ilist))
		print(total)
		ilist = input("enter n:")

if __name__ == "__main__":
    main()
