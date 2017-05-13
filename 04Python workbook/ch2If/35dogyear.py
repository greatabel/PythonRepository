iyear  = int(input("enter integer:"))
dogyear = 0
if iyear <=2:
	dogyear = 10.5*iyear
else:
	dogyear = 10.5 * 2 + 4*(iyear -2)

print("dogyear:%d" %dogyear)