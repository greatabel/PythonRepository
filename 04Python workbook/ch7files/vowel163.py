import sys
sys.path.insert(0,'../ch5list')
from onlywords111 import findwords

def main():


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
		
		for word in words:
			count = 0
			origin = word
			if 'a' in word:
				count += 1
				index = word.find('a')
				word = word[index:]
				print('w=',word)
			if 'e' in word:
				count += 1
				index = word.find('e')
				word = word[index:]
				print('w=',word)
			if 'i' in word:
				count += 1
				index = word.find('i')
				word = word[index:]
				print('w=',word)
			if 'o' in word:
				count += 1
				index = word.find('o')
				word = word[index:]
				print('w=',word)
			if 'u' in word:
				count += 1
				index = word.find('u')
				word = word[index:]
				print('w=',word)
			if 'y' in word:
				count += 1
				index = word.find('y')
				word = word[index:]
				print('w=',word)
			if count == 6:
				print("the one is:",origin)


		

	except IOError:
		print("获取文件时候出错")
		quit()


        
if __name__ == "__main__":
    main()
