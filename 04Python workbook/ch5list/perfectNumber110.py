from properDivisor109 import findallDivisors
def isPerfectNumber(n):
	divisors = findallDivisors(n)
	print("divisors=",divisors)
	flag = False
	if sum(divisors) == n:
		flag = True
	else:
		flag = False
	return flag

def main():
	
	s = input("Enter first(blank line to quit):")
	while s != "":
		num = int(s)

		if isPerfectNumber(num):
			print("Is true")
		else:
			print("Wrong")
	
		s = input("Enter(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()