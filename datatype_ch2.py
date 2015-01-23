#!/usr/bin/env python3

z = -80 + 20j
print(z)
print(z.real,z.imag)

import decimal
a = decimal.Decimal(1233)
b = decimal.Decimal(2344)
print( a + b )

print(23/1.05)
print(decimal.Decimal(23) / decimal.Decimal("1.05"))

text = """ test test "test" test1
		test2\
		test3 test"""
print(text)

a = "single 'quotes' are fine;\"doubles\" must be escaped."
b = 'single \'quotes\' must be secaped;"doubles" are fine.'
print(a,'\n#',b)


import re
def test_whether_is_phone(phonestring):
	phonePattern = re.compile(r"^((?:[0\d+[]])?\s*\d+(?:-\d+)?)$")
	# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
	match = phonePattern.match(phonestring)	 
	if match:
	    # 使用Match获得分组信息
	    print(match.group())
	else:
		print('not matched')

test_whether_is_phone('13911634999')
test_whether_is_phone('1391163test')

t = "This is not the best way to join two long strings" +\
  " together "
s = ("this is the nice way to"
	" join two long strings")
print(t)
print(s)

#unicode
#打出欧元符号 在osx：http://www.macgg.com/archives/6490.html
euros = "€\N{euro sign}\u20AC\U000020AC"
print(euros)
print(ord(euros[0]))
print(ord(euros[1]))
print(hex(ord(euros[0])))
print(hex(ord(euros[1])))

s = "test:" + chr(8364)+chr(0x20ac)
print('s=',s)
print(ascii(s))

#compare string
from unicodedata import normalize

print( normalize('NFD', u'\u00C7'),end =""  )
print( normalize('NFC', u'C\u0327') ,end="")
print( normalize('NFKD', u'C\u0327') ,end="")
print()
s = 'Spicy Jalapeño'
print(ord(s[13]))
print( ord(normalize('NFKD', s)[13] ))




treatises =['abc','def','gh']
print("".join(treatises))
print("-<>-".join(treatises))

record = "Leo Tolstory*123*1910-01-10*2015-01-22"
fields = record.split("*")
print(fields)
born = fields[2].split("-")

died = fields[3].split("-")
print(born,died)
print("lived about",int(died[0]) - int(born[0]),"years")

#http://stackoverflow.com/questions/10329290/python-3-x-using-string-maketrans-in-order-to-create-a-unicode-character-tran
intab = "abcde"
outtab = "12345"
trantab = str.maketrans(intab,outtab)
str = "this is a test of trans"
print(str)
print(str.translate(trantab))

print("The movel '{0}' was published in {1}".format("Hard Times",1854));
x = "three"
s = "{0} {1} {2}"
s = s.format("The",x,"tops")
print(s)
print("{who} turned {age} this year.".format(who="She",age=88))
print("The {who} was {0} last week".format(12, who = "boy"))
stock = ["paper","envelopes","notepads"]
print("We have {0[1]} and {0[2]} in stock".format(stock))

