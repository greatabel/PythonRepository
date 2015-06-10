from NumberPrime92 import is_prime

def nextprime(a):
    while not is_prime(a):
    	a = a + 1
    return a 

def main():
	line = input("Enter number test:")
	while line != "":
		print("next prime =", nextprime(int(line)))

		line = input("Enter number:")

main()