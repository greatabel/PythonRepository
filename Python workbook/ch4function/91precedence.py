# from isStringInteger90 import CheckStringIsInteger
def Precedence(s):
	p = 0
	if s =="+" or s == "-":
		p = 1
	elif s == "*" or s == "/":
		p = 2
	elif s == "^":
		p = 3
	return p


def main():
	line = input("Enter digital expression(1+2*3):")
	while line != "":
		for c in line:
			if c in ('+','-','*','/','^'):
				print(Precedence(c))

		line = input("Enter sentence:")

main()
