import sys





#启动参数 python3 concatFile143.py data/test.txt data/test1.txt

def main():



	try:
		boylines = []
		startY = input("StartYear:")
		endY = input("EndYear:")
		for i in range(int(startY),int(endY)):
			filenameB = 'BabyNames/'+str(i)+"_BoysNames.txt"
			

			with open(filenameB) as infile:
				line = infile.readline().strip()
				boylines.append(line)
				print(line)

		




	except IOError:
		print("获取文件时候出错")
		quit()

	print("-"*20)
	print(boylines)

	

	


	


        
if __name__ == "__main__":
    main()
