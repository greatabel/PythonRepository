import math
def shippingCharge(num):
	total = 0
	if num ==1:
		total = 10.95
	else:
		total = 10.95 + 2.95*(num -1)
	return total

line = input("Enter number of items:")
while line != "":
	num  = int(line)
	print('distance fare=%0.2f' % shippingCharge(num))


	line = input("Enter items num:")
