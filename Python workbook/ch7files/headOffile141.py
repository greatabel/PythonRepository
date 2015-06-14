import sys

NUM_LIMTES = 10

def demo_rstrip():
	str = "     this is string example....wow!!!     ";
	print(str.rstrip())
	str = "88888888this is string example....wow!!!8888888";
	print(str.rstrip('8'))
	print('-'*20)

def main():
	demo_rstrip()
	#检查  python3 headOffile141.py 后门有没有文件名
	if len(sys.argv)!= 2:
		print("提供文件名!")
		quit()

	try:
		inf = open(sys.argv[1], "r")

		line = inf.readline()

		count = 0
		while count < NUM_LIMTES and line != "":
			line = line.rstrip()
			count += 1
			print(line)
			#读取下一行
			line = inf.readline()

		inf.close()

	except IOError:
		print("获取文件时候出错")

	


        
if __name__ == "__main__":
    main()
