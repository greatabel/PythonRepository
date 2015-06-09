import math
def computeHypo(a,b):
	return math.sqrt(a**2 + b**2)

line = input("Enter a,b of 2 sides of right triangle:")
while line != "":
	ilist = line.split(',')
	a = int(ilist[0])
	b = int(ilist[1])
	print(a,b)
	print(computeHypo(a,b))


	line = input("Enter a,b of 2 sides of right triangle:")
