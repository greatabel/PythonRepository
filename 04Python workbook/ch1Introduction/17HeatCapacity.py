WATER_CAPACITY = 4.186
ELECTRCIT_PRICE = 0.6
J_TO_KWH = 2.777e-7

volume = float(input("Enter amount of water in milliliters:"))
d_temp = float(input("Enter the temperature increase (degree celsis):"))

q = volume * d_temp * WATER_CAPACITY

print(" %.02f joules of energy" %q)

kwh  = q * J_TO_KWH
cost = kwh * ELECTRCIT_PRICE
print("That cost %.2f yuan" %\
	cost) 