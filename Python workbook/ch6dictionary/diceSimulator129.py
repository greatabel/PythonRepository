from fractions import Fraction
import math,random

mydic = {1:"one test",2:"two",3:"three",4:"test",5:"test"}


def main():
	
	# thevalue = input("Enter the value you want to reverse loop (blank line to quit):")
	# while thevalue!="":
	propertys = {}
	for i in range(1,7):
		for j in range(1,7):
			sum = i + j
			if not sum in propertys.keys():
				propertys[sum] = 1
			else:
				propertys[sum] += 1
	print("orgin:",propertys)
	total = 0
	for key in propertys:
		total += propertys[key]	


	for key in propertys:
		propertys[key] = Fraction(propertys[key] ,total )
		# print('t=',propertys[key])
	print("after",propertys)

	realPropertys = {}
	for i in range(0,100000):
		x = random.randint(0,6)
		y = random.randint(0,6)
		rsum =  x + y
		if not rsum in realPropertys.keys():
			realPropertys[rsum] = 1
		else:
			realPropertys[rsum] +=1
	print("orgin real:",realPropertys)
	countTotal = 0
	for key in realPropertys:
		countTotal += realPropertys[key]

	for key in realPropertys:
		realPropertys[key] = Fraction(realPropertys[key], countTotal)
	print("after real:",realPropertys)

	print("-"*30,"\n Total   Simulated Percent   Excepcted Percent")

	for key in propertys:
		print("%d %0.2f %0.2f" %(key ,float(propertys[key]),float(realPropertys[key])))


		

		# thevalue = input("Enter the value you want to reverse loop (blank line to quit):")


	
	

        
if __name__ == "__main__":
    main()
