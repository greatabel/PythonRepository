import math



def IntToOrdinal(iN):
	my_dict = {1: 'first', 2: 'second',3:'third',4:'fourth'}
	if  iN in my_dict.keys():
		return my_dict[iN]
	else:
		return ""
if __name__ == "__main__":
	line = input("Enter a number:")
	while line != "":
		iN = int(line)
		myout = IntToOrdinal(iN)
		if myout !="":
			print(myout)
		else:
			print("I don't know")


		line = input("Enter a number:")

