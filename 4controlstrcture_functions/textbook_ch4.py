# -*- coding: utf-8 -*-

def product(*args):
	result = 1
	for arg in args:
		result *= arg
	return result

print(product(1,2,3))
print(product(1,2,3,4))
print(product(1,2,30))

def sum_of_powers(*args,power=1):
	result = 0
	for arg in args:
		result += arg ** power
	return result
print("sum_of_powers")
print(sum_of_powers(1,3,5,power=2))

import math
def heron2(a,b,c,*,units ="meters"):
	s = (a + b + c )/2
	area = math.sqrt(s*(s - a)*(s - b)*(s - c))
	return "{0} {1}".format(area,units)

print(heron2(25,24, 7))




Language = "en"
ENGLISH = {0:"zero",1:"one",2:"two",3:"three",4:"four",
			5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
Chinese = {0:"零",1:"一",2:"二",3:"三",4:"四",
			5:"五",6:"六",7:"七",8:"八",9:"九"}

def print_digits(digits):
	dictionary = ENGLISH if  Language =="en" else Chinese
	for digit in digits:
		# print(digit)
		print(dictionary[int(digit)], end=" ")
	print()

import sys
def main():
	# print("in main")
	if len(sys.argv) == 1 or sys.argv[1] in {"-h","--help"}:
		print("usage:{0}[en|zh] number".format(sys.arg[0]))
		sys.exit()

	args = sys.argv[1:]
	if args[0] in {"en","zh"}:
		global Language
		Language = args.pop(0)
	print_digits(args.pop(0))

main()
