line = input("Enter n tearspoons:One cup is equivalent to 16 tablespoons.\
 One tablespoon is equivalent to 3 teaspoons:")
while line != "":
	n = int(line)
	cup = n//16
	tablespoon=(n%16)//3
	tearspoons=(n%16)%3
	print(cup,"cup",tablespoon,"tablespoons",tearspoons,"tearspoons")
	line = input("Enter n tearspoons:One cup is equivalent to 16 tablespoons.\
	 One tablespoon is equivalent to 3 teaspoons:")
