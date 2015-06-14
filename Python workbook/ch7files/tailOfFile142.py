import sys

NUM_LIMTES = 10




def main():

	#检查  python3 headOffile141.py 后门有没有文件名
	if len(sys.argv)!= 2:
		print("提供文件名!")
		quit()

	try:
		inf = open(sys.argv[1], "r")

		# 读取文件，保存最多10行
		lines = []
		for line in inf:
			lines.append(line)
			if len(lines) > NUM_LIMTES:
				lines.pop(0)

		inf.close()

	except IOError:
		print("获取文件时候出错")
		quit()

	for line in lines:
		print(line, end = '')

	


        
if __name__ == "__main__":
    main()
