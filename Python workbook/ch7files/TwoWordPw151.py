import sys
from random import randrange

def generateWordPw(filepath):

	try:
		pwd = []
		inf = open(filepath,"r")
		for line in inf:
			line = line.replace('\n','').strip()
			if len(line) >=3 and len(line) <=7:
				pwd.append(line)

		inf.close()
		print(pwd)


		first = pwd[randrange(0,len(pwd))]
		first = first.title()

		realPwd = first
		while len(realPwd) < 8 or len(realPwd) > 10:
			second = pwd[randrange(0,len(pwd))]
			second = second.title()
			realPwd = first + second

		return realPwd

	except IOError:
		print("获取文件时候出错")
		quit()



#启动参数 python3 concatFile143.py data/test.txt data/test1.txt

def main():
	pwd = generateWordPw("data/test.txt")
	print('pwd=',pwd)
	

	

        
if __name__ == "__main__":
    main()
