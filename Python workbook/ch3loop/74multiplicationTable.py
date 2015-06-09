line = input("Enter n:")
while line != "":
	n = int(line)

	for i in range(0,n+1):
		print(i," ",end="")
		for j in range(1,n+1):
			if i ==0:
				i = 1
			print(j*i," ",end="")
		print("")


	line = input("Enter n:") 

print("method 2| better way:")
MIN = 1
MAX = 10
print("    ", end ="")
for i in range(MIN, MAX +1):
	print("%4d" %i ,end="")
print()

for i in range(MIN, MAX+1):
	print("%4d" %i, end="")
	for j in range(MIN, MAX+1):
		print("%4d" %(i * j),end="")
	print()