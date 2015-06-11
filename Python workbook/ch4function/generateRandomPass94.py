from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

def randomPasword():
	randomLength = randint(SHORTEST,LONGEST)
	print("randomLength=",randomLength)
	result = ""
	for i in range(randomLength):

		randomChar = chr(randint(MIN_ASCII,MAX_ASCII))
		# print('randomChar=',randomChar)
		result = result + randomChar

	return result

def main():
	print("Your random pass is:", randomPasword())

if __name__ == "__main__":
	main()