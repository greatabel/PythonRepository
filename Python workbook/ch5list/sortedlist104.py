line = input("Enter number:")
ilist = []
while line != "":
	n = int(line)
	ilist.append(n)
	if n == 0:
		break
	else:
		line = input("Enter number:")

# print(sorted(ilist))
for item in sorted(ilist):
	print(item, end=" ")