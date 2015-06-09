line = input("Enter n:")
import math
while line != "":
	n = int(line)
	total = 3
	for i in range(1,n+1):

		odd =  4/((2*i)*(2*i+1)*(2*i+2))
		if i%2 == 0:
			odd = odd * (-1)
		

		print("i=",i,"odd=",odd)
		total += odd
	print('total=',total)
	line = input("Enter n:") 

