FEET_PER_INCH = 12
YARD_PER_INCH = 36
MILE_PER_INCH = 63360

inches = int(input("Enter the number of inches:?"))
print( inches // MILE_PER_INCH , "mile")
inches = inches % MILE_PER_INCH

print( inches // YARD_PER_INCH , "yard")
inches = inches % YARD_PER_INCH

print( inches , "feet")

