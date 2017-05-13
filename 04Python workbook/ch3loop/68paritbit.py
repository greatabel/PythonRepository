line = input("Enter 8 bits:")

while line != "":
	if line.count("0") + line.count("1") != 8 or len(line )!=8:
		print("That's not 8 bit")
	else:
		ones = line.count("1")

		if ones % 2 == 0:
			print("Parit should be 0")
		else:
			print("Parit shoudld be 1")
	line = input("Enter 8 bits:") 