line = input("Enter n:")
while line != "":
	total = 0
	length = len(line)
	for ch in line:

		if ch =='1':
			total += pow(2 , length -1) 
		length -=1
	print(total)

	line = input("Enter n:") 

