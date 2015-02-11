# -*- coding: utf-8 -*-
str1 = "this is string example....wow!!!";
str2 = "exam";

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))
#限制在exam出现前
print(str1.find(str2, 10 ,14))
print('-^0^-'*10+'next example:->')


import sys
sites = {}
for filename in sys.argv[1:]:
	for line in open(filename):
		i = 0
		while True:
			site = None
			i = line.find("http://",i)
			if i > -1:
				i += len("http://")
				for j in range(i,len(line)):
					#Python isalnum() 方法检测字符串是否由字母和数字组成
					if not (line[j].isalnum() or line[j] in ".-"):
						site = line[i:j].lower()
						break
				if site and "." in site:
					#获取信息，如果获取不到的时候就按照他的参数设置该值
					sites.setdefault(site,set()).add(filename)
				i = j
			else:
				break
print('sites=', sites)
for site in sorted(sites):
	print("{0} [@] is referred to in:".format(site))
	for filename in sorted(sites[site],key = str.lower):
		print(" {0}".format(filename))