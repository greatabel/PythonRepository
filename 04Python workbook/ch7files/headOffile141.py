import sys

NUM_LIMTES = 10

def demo_strip():
	#http://www.crifan.com/python_detail_intro_string_strip_lstrip_rstrip/
	str = "     this is string example....wow!!!     ";
	print(str.rstrip())
	str = "88888888this is string example....wow!!!8888888";
	print(str.rstrip('8'))
	demoStr = "      hello wold !    "
	print('|'+demoStr+'|')
	print('|'+demoStr.lstrip()+'|')
	print(demoStr.rstrip()+'|')
	print('|'+demoStr.strip()+'|')

	# demoStr.lstrip() = 去除left左边的白空格  = "hello wold !    "
	# demoStr.rstrip() = 去除right右边的白空格 = "      hello wold !"

	# demoStr.strip() = demoStr.lstrip().rstrip()=去除left左边和right右边=去除首尾的白空格="hello wold !"
	print('-'*20)


def main():
	demo_strip()
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
