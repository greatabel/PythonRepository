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
		mydict = {}
		for line in inf:
			for word in findwords(line):
				
				c = word.lower()
				if c in mydict.keys():
					mydict[c] += 1
				else:
					mydict[c] = 1

			
		inf.close()
		print('-'*30)
		print(mydict)
		for inputItem in findwords("aardvark it"):
			if inputItem not in mydict.keys():
				print(inputItem,"] is spelling error!")
		

	except IOError:
		print("获取文件时候出错")
		quit()


        
if __name__ == "__main__":
    main()
