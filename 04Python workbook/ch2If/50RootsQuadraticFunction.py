import math

while True:
	myinput = input("Enter the coefficients of a, b and c separated by commas: ")
	if  myinput is not None and myinput!="":
		
		try:
			ilist = myinput.split(",")
			a = float(ilist[0])
			b = float(ilist[1])
			c = float(ilist[2])
			print("The equation: ",a,"+x^2+",b,"x+",c,"=0")

			root1 = ( -b + math.sqrt( b**2 - 4 * a * c)) / 2 * a
			root2 = ( -b - math.sqrt( b**2 - 4 * a * c)) / 2 * a
			print("root1=",root1,"root2=",root2)
		except:
			print('error input')
			# break
	else:
		break