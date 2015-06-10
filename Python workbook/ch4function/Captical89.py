def Capitalize(s):
	result = s.replace(" i ", " I ")
	
	if len(s) > 0:
		result = result[0].upper() +\
				result[1:len(result)]

	#captial first character of string follow  . ! ?
	pos = 0
	while pos < len(s):
		if result[pos] == "." or result[pos]=="!" or result == "?":
			pos = pos + 1

			while pos < len(s) and result[pos] == " ":
				pos = pos + 1

			if pos < len(s):
				result = result[0 : pos]+\
						result[pos].upper()+\
						result[pos+1 : len(result)]

		pos = pos + 1

	return result

def main():
	line = input("Enter sentence:")
	while line != "":
		
		print(Capitalize(line))

		line = input("Enter sentence:")

main()
