#http://stackoverflow.com/questions/17140408/if-statement-to-check-whether-a-string-has-a-capital-letter-a-lower-case-letter
from random import randint
import string, random

def checkWhetherGoodPass(pwd):
	
	flag = True
	if len(pwd) <8:
		flag = False
	if not any(x.isupper() for x in pwd):
		flag = False
	if not any(x.islower() for x in pwd):
		flag = False
	
	return flag

def main():
	line = input("input password:")
	print("Your random pass is:", checkWhetherGoodPass(line))

if __name__ == "__main__":
	main()