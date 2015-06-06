FOOT_PER_INCHES = 12
INCH_PER_CM = 2.54
print("What's your height?")
feet  = int(input("foot:"))
inchs = int(input("inchs:"))
total = (feet*FOOT_PER_INCHES + inchs) * INCH_PER_CM
print("total: %.2f" %total )