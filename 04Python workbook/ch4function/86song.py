from conertIntToOrdinal85 import IntToOrdinal

def displayVerse(n):
	print("One the", IntToOrdinal(n),"day of Christmas")
	if n >= 3:
		print("Three hens,")
	if n >= 2:
		print("Two turtle,")
	if n == 1:
		print("A", end=" ")
	else:
		print("And a",end=" ")
	print()

def main():
	for verse in range(1,4):
		displayVerse(verse)
#cal main function
main()