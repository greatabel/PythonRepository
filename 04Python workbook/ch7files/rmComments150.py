import sys





#启动参数 python3 concatFile143.py data/test.txt data/test1.txt

def main():

	#检查  python3 headOffile141.py 后门有没有文件名
	if len(sys.argv) < 2:
		print("提供文件名!")
		quit()

	try:
		filenames = sys.argv[1:]
		print(filenames)

		with open('data/removedComments.py','w') as outfile:

			#方法2:官方
			for i in range(1,len(sys.argv)):
				fname = sys.argv[i]
				inf = open(fname,"r")
				for line in inf:
					if not line.lstrip().startswith('#'):
						outfile.write(line)
				inf.close()
				outfile.write("\n\n")


	except IOError:
		print("获取文件时候出错")
		quit()

	inf = open('data/removedComments.py', "r")

	# 读取文件，保存最多10行
	lines = []
	for line in inf:
		lines.append(line)		
	inf.close()

	for line in lines:
		print(line, end = '')


	


        
if __name__ == "__main__":
    main()
