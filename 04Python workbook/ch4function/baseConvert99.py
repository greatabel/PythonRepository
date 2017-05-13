from hexAndDec98 import *

def dec2n(num, new_base):
	result = ""
	q = num

	r = q % new_base
	while q > 0:
		r = q % new_base
		result = dec2hex(r) + result
		q = q // new_base

	return result

def n2dec(num, b):
	decimal = 0
	power = 0
	for i in range(len(num)):
		decimal = decimal * b
		decimal = decimal + hex2int(num[i])

	return decimal


def main():
	from_base = int(input("Enter base from:"))
	from_num = input("Enter digits in that base:")
	dec = n2dec(from_num,from_base)
	print(" Tha's %d in base 10  " % dec)

	to_base = int(input("enter base to convert to:"))
	to_num = dec2n(dec, to_base)

	print("That's %s in base %d " %(to_num, to_base))

if __name__ == "__main__":
	main()