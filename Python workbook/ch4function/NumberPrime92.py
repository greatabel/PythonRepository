# from isStringInteger90 import CheckStringIsInteger
def is_prime(a):
    x = True 
    for i in range(2, a):
       if a%i == 0:
           x = False
           break # ends the for loop
    return x

def main():
	line = input("Enter number:")
	while line != "":
		if is_prime(int(line)):
			print("is prime")
		else:
			print("not prime")

		line = input("Enter number:")
if __name__ == '__main__':
	main()
