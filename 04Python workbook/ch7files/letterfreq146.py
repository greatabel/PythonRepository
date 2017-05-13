import sys

NUM_LIMTES = 10



#启动参数 python3 concatFile143.py data/test.txt data/test1.txt

def main():

	#检查  python3 headOffile141.py 后门有没有文件名
	if len(sys.argv) < 2:
		print("提供文件名!")
		quit()

	try:
		filenames = sys.argv[1:]
		print(filenames)

		
		
		fname = sys.argv[1]
		inf = open(fname,"r")
		mydict = {}
		for line in inf:
			for c in line:
				if c.isalpha():
					# 如果是字母
					c = c.upper()
					if c in mydict.keys():
						mydict[c] += 1
					else:
						mydict[c] = 1

			
		inf.close()
		print('-'*30)
		print(mydict)


	except IOError:
		print("获取文件时候出错")
		quit()


        
if __name__ == "__main__":
    main()
