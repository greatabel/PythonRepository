my_dict = {3: 'triangle', 4: ' rectangle',5:'pentagon'}

iN = int(input("enter your x's sides? "))
# print(iN)
if  iN in my_dict.keys():
	print(my_dict[iN])
else:
	print("don't konw what it is! ")