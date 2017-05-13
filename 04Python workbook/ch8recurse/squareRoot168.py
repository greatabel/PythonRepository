def sqroot(n,guessed=1.0):

	if abs(guessed**2 - n) <= 1e-12 or n == 1:
	    return guessed
	else:
	    guessed = (guessed+ (n/guessed))/2
	    return sqroot(n,guessed)
# 输入例子：10003
def main():
	ilist = input("enter n:")
	while ilist!="":
		
		total = sqroot(int(ilist))
		print(total)
		ilist = input("enter n:")

if __name__ == "__main__":
    main()
