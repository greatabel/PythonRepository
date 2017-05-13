iInt = int(input("Enter presure per 1unit : "))
i = 0
mylist = []
while(iInt>0):
	
	mylist.append(int(iInt%10))
	iInt = int(iInt/10)
	i+=1

print("mylist:%s" %str(mylist))
def listsum(inputlist):
	if len(inputlist) == 1:
		return inputlist[0]
	else:
		return inputlist[0] + listsum(inputlist[1:])

print(listsum(mylist))
print(sum(mylist))