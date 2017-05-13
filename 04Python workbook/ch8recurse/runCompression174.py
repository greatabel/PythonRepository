#不明白题意

def loadNames():
	return "AAABBC"

def RunEncode(data):
	if len(data) == 0:
		return []

	index = 1
	while index < len(data) and data[index] == data[index -1]:
		index = index +1
	current = [data[0],index]

	return current + RunEncode(data[index:len(data)])

	

def main():
	
	sequence = RunEncode(loadNames())
	print(sequence)

if __name__ == "__main__":
    main()



