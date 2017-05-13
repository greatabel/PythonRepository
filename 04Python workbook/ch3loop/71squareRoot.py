import math
line = input("Enter n:")


while line != "":
	n = float(line)
	guess = n/2 
	
	while guess**2 - n > 1e-12:		
		guess = (guess + n/guess)/2
	print("guess=",guess)
	line = input("Enter n:") 

