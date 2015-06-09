PENNIS_PER_NICKE = 5
NICKEL = 0.05

total = 0.00
while True:

	line = input("input number plate (enter 'enter' to exit): ")

	if line is not None and line !="" :
		total  =+ float(line)
		
	else:
		break

print("total %.02f" %(total))

rounding_indicator = total * 100 %PENNIS_PER_NICKE

if rounding_indicator < PENNIS_PER_NICKE /2:
	cash_total = total - rounding_indicator /100
else:
	cash_total = total + NICKEL - rounding_indicator/100

print(" %.02f " %cash_total)
