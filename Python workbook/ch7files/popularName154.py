import sys





#启动参数 python3 concatFile143.py data/test.txt data/test1.txt

def main():



	try:
		boylines = []
		girllines = []
		for i in range(2000,2012):
			filenameB = 'BabyNames/'+str(i)+"_BoysNames.txt"
			filenameG = 'BabyNames/'+str(i)+"_GirlsNames.txt"

			with open(filenameB) as infile:
				line = infile.readline().strip()
				boylines.append(line)
				print(line)

			with open(filenameG) as infile:
				line = infile.readline().strip()
				girllines.append(line)
				print('line=',line)




	except IOError:
		print("获取文件时候出错")
		quit()

	print("-"*20)
	print(boylines,girllines)

	

	


	


        
if __name__ == "__main__":
    main()
