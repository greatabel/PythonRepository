line = input("Enter n:")
while line != "":
	line = line.lower()
	line = line.replace (" ", "")
	print("line=",line)
	reverse = ""
	isP = True
	i = 1
	for c in line:
		if( line[len(line) -i] != line[i-1]):
			print("not palindrom")
			isP = False
			break
		i = i+1
	if isP:
		print("is palindrom")


	line = input("Enter n:") 

