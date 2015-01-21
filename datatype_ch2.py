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