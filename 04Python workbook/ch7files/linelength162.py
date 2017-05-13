import sys
sys.path.insert(0,'../ch5list')
from onlywords111 import findwords

def main():
	# print(findwords("aardvark it"))
	#检查  python3 headOffile141.py 后门有没有文件名
	

	try:
		fname = 'data/test.txt'
		inf = open(fname,"r")
		words= []
		for line in inf:

			for word in findwords(line):
				
				c = word.lower()
				# print(c)
				words.append(c)
		inf.close()
		print('-'*30)
		print(words)
		
		for i in (0,len(words)//5):
			print(i)
			print(words[i*5: (i*5+5)])

		

	except IOError:
		print("获取文件时候出错")
		quit()


        
if __name__ == "__main__":
    main()
