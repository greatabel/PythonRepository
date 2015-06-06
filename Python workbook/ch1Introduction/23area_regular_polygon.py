import math

n = float(input("n:"))
s = float(input("s:"))
area = n * s**2/ (4 * math.tan(math.pi/n))
print("erea is :%.02f" %area)