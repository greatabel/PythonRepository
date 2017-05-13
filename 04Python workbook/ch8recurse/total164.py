def readAndTotal():
	line = input("Enter a number:")
	if line == "":
		return 0
	else:
		return float(line)+ readAndTotal()

def main():
	total = readAndTotal()
	print(total)

if __name__ == "__main__":
    main()
