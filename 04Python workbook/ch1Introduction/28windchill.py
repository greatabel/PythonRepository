input = input("Enter Ta ,V minutes separated by commas: ")

input_list = input.split(',')

ta = float(input_list[0])
v  = float(input_list[1])
import math
WCI = 13.12 + 0.6215*ta - 11.37*math.pow(v,0.16) + 0.3965*ta*pow(v,0.16)
print("WCI: %.02f" %WCI)