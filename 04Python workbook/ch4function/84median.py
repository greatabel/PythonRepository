import math
def median(a,b,c):
	total = (a + b + c)/3
	
	return total

line = input("Enter 3 values by, of items:")
while line != "":
	ilist = line.split(',')
	a = float(ilist[0])
	b = float(ilist[1])
	c = float(ilist[2])
	print('total(a,b,c) =%0.2f' % median(a,b,c))


	line = input("Enter 3 values by, of items:")