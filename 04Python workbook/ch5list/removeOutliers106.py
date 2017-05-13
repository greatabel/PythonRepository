line = input("Enter number:")
ilist = []
while line != "":
	n = int(line)
	ilist.append(n)
	if n == 0:
		if(len(ilist)<=4):
			print("Please enter more than 4 ")
			line = input("Enter number:")
		else:
			break
	else:
		line = input("Enter number:")

# print(sorted(ilist))
tlist = ilist.copy()
sortedlist = sorted(ilist)
rm1 = sortedlist[0]
rm2 = sortedlist[1]
rm3 = sortedlist[len(ilist)-1]
rm4 = sortedlist[len(ilist)-2]

tlist.remove(rm1)
tlist.remove(rm2)
tlist.remove(rm3)
tlist.remove(rm4)

print(ilist)
print("After:")
print(tlist)
