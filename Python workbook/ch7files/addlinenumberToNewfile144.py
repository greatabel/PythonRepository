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

		with open('data/linenumber.txt','w') as outfile:
			# for fname in filenames:
			# 	with open(fname) as infile:
			# 		for line in infile:
			# 			outfile.write(line)

			#方法2:官方
		
			fname = sys.argv[1]
			inf = open(fname,"r")
			count = 1
			for line in inf:
				# 对齐问题 http://stackoverflow.com/questions/5676646/fill-out-a-python-string-with-spaces
				outfile.write("%s %s" % ( str(count).ljust(4) , line))
				count += 1
			inf.close()
			outfile.write("\n\n")


	except IOError:
		print("获取文件时候出错")
		quit()

	inf = open('data/linenumber.txt', "r")

	# 读取文件，保存最多10行
	lines = []
	for line in inf:
		lines.append(line)		
	inf.close()

	for line in lines:
		print(line, end = '')


	


        
if __name__ == "__main__":
    main()
