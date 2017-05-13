import pkgutil

try:
    something_txt = pkgutil.get_data('example', 'data/something.txt')
    print('#',something_txt)
    
except:
    print('error here 2')
    raise