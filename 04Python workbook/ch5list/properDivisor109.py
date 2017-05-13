def findallDivisors(n):
	values = []
	for i in range(1,n):
		if n % i == 0:
			values.append(i)
	return values

def main():
	
	s = input("Enter first(blank line to quit):")
	while s != "":
		num = int(s)

		print(findallDivisors(num))
	
		s = input("Enter(blank line to quit):")

	
	

        
if __name__ == "__main__":
    main()