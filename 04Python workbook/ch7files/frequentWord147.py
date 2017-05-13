#http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
#怎么添加别的文件夹
import sys
sys.path.insert(0,'../ch5list')
from onlywords111 import findwords

def main():
	print(findwords("test it"))
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
			for word in findwords(line):
				
				c = word.lower()
				if c in mydict.keys():
					mydict[c] += 1
				else:
					mydict[c] = 1

			
		inf.close()
		print('-'*30)
		print(mydict)
		import operator
		thekey = max(mydict.items(), key = operator.itemgetter(1))[0]
		print("mydict[",thekey,"]=",mydict[thekey])


	except IOError:
		print("获取文件时候出错")
		quit()


        
if __name__ == "__main__":
    main()
