R = 8.314
p = float(input("p:"))
v = float(input("v:"))
t = float(input("t:"))

moles = p * v / (R * t)

import math

print("moles: %.02f " %(moles))