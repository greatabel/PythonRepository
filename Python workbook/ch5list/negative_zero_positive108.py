negatives = []
zeros = []
positives = []

def main():
	values = []
	s = input("Enter first(blank line to quit):")
	while s != "":
		num = int(s)

		if num < 0:
			negatives.append(num)
		elif num == 0:
			zeros.append(num)
		else:
			positives.append(num)
	
		s = input("Enter(blank line to quit):")

	
	print(negatives,zeros,positives)
	print("The original data: ",values)

        
if __name__ == "__main__":
    main()