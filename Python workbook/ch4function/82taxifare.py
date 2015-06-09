import math
def fare(distance):
	return 0.25 *  (distance/140) + 4

line = input("Enter distance:(km):")
while line != "":
	distance = float(line)
	print('distance fare=%0.2f' % fare(distance*1000))


	line = input("Enter distance:")
