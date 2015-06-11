from random import randint
import string, random

def randomPlate():
	
	result = ""
	# for i in range(3):
	# 	print(ord('A'),ord('z'))
	# 	randomChar = chr(randint(ord('A'),ord('z')))

	# 	print('randomChar=',randomChar)
	# 	result = result + randomChar
	result = ''.join(random.choice(string.ascii_lowercase) for x in range(3))
	myintrange = 0
	myrandomtype = randint(0,1)
	# print('myrandomtype=',myrandomtype)
	if myrandomtype%2==0:
		myintrange = 3
	else:
		myintrange = 4
	for j in range(myintrange):
		randomNum = str(randint(0,9))
		result = result + randomNum
	return result

def main():
	print("Your random pass is:", randomPlate())

if __name__ == "__main__":
	main()