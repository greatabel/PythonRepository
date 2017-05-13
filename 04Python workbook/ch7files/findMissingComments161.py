import sys
sys.path.insert(0,'../ch5list')
from onlywords111 import findwords

def main():
	# print(findwords("aardvark it"))
	#检查  python3 headOffile141.py 后门有没有文件名
	

	try:
		fname = 'data/test.py'
		inf = open(fname,"r")
		words= []
		for line in inf:

			for word in findwords(line):
				
				c = word.lower()
				# print(c)
				if c == "def" and line.startswith("def") and line.find("#") < 0:
					print(line.replace("\n",""),"is missing comments")
			
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
