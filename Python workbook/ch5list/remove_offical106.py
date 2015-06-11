def removeOutlier(data ,num_outliers):
	retval = sorted(data)

	for i in range(num_outliers):
		retval.pop()

	for i in range(num_outliers):
		retval.pop(0)

	return retval

def main():
	values = []
	s = input("Enter first(blank line to quit):")
	while s != "":
		num = float(s)
		values.append(num)
		s = input("Enter(blank line to quit):")

	if len(values) < 4:
		print(" You did 't enter eough values")
	else:
		print("After removed :",removeOutlier(values, 2))
		print("The original data: ",values)

        
if __name__ == "__main__":
    main()