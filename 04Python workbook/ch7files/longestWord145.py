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
		longestLength  = 0
		longestItem = ''
		for line in inf:
			#http://stackoverflow.com/questions/1192881/how-to-find-the-longest-word-with-python
			theItem = max(line.split(" ") , key = len)
			
			if longestLength < len(theItem):
				longestLength = len(theItem)
				longestItem = theItem
				print('theItem=',theItem,'len=',len(theItem))
		print("%s length is %d" %(longestItem,longestLength))
		inf.close()



	except IOError:
		print("获取文件时候出错")
		quit()

	
        
if __name__ == "__main__":
    main()
