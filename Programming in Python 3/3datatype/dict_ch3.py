#使用方式：python3 dict_ch3.py test_article_ch3.txt 
# -*- coding: utf-8 -*-
import string
import sys

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\""
print("strip=",strip)
for filename in sys.argv[1:]:
	for line in open(filename):
		for word in line.lower().split():
			word = word.strip(strip)
			if len(word) >2:
				words[word] = words.get(word,0) + 1
for word in sorted(words):
	print("{0} ## occurs {1} times".format(word,words[word]))