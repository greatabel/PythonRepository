import importlib

math = importlib.import_module('math')
print(math.sin(1))
mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.douban.com')
print(u.read(300))

print(u.read().decode('utf-8'))
