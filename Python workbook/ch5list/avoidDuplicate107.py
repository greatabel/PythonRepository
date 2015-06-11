def removeDuplicate(mylist):
	return sorted(set(mylist))

def main():
	values = []
	s = input("Enter first(blank line to quit):")
	while s != "":
		
		values.append(s)
		s = input("Enter(blank line to quit):")

	
	print("After removed :",removeDuplicate(values))
	print("The original data: ",values)

        
if __name__ == "__main__":
    main()