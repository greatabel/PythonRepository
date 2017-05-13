#http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
#怎么添加别的文件夹
import sys
sys.path.insert(0,'../ch5list')
from onlywords111 import findwords

def main():
	print(findwords("aardvark it"))
	#检查  python3 headOffile141.py 后门有没有文件名
	

	try:
		fname = 'data/test.txt'
		inf = open(fname,"r")
		words= []
		for line in inf:
			for word in findwords(line):
				
				c = word.lower()
				words.append(c)
			
		inf.close()
		print('-'*30)
		print(words)
		import collections
		duplicated = [item for item, count in collections.Counter(words).items() if count > 1]
		print('duplicated=',duplicated)

		

	except IOError:
		print("获取文件时候出错")
		quit()


        
if __name__ == "__main__":
    main()
