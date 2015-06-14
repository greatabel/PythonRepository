def sieveMethod(n):
	nums = []
	rm = []
	for i in range(1,n+1):
		nums.append(i)
#删除1
	nums.remove(1)
	
	p = 2
	while p < n:
		print('-'*10,'p=',p)
		#从第二个p开始是 第一个p 如果满足条件应该保留
		for i in range(p*2, n+1, p):
			print("i=",i)
			if i in nums:
				nums.remove(i)
				print('removed:',i)
		p += 1
	print('remaining:',nums)
	# print(myarray)

def main():
	

	n = input("Enter n (blank line to quit):")

	

	while n!="":
		n = int(n)
		alllist = sieveMethod(n)
		print('alllist ','-'*20)
		print(alllist)

		n = input("Enter n (blank line to quit):")

		n = int(n)

	
	

        
if __name__ == "__main__":
    main()