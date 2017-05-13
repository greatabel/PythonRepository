#encoding:utf-8
from colorama import Fore, Back, Style

def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))

import html
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                      name=name,
                      attrs=attr_str,
                      value=html.escape(value))
    return element

def anyargs(*args, **kwargs):
    print('args=',args)
    print('kwargs=',kwargs)

def main():
    print(avg(1,2))
    print(avg(1,2,3))

    print(Fore.BLUE + "and content:" + Style.RESET_ALL)

    print(make_element('item', 'I am value',size='large',quantity=6))
    print(make_element('p','<spam>'))


    print(Back.GREEN + 'demo2'+ Back.RESET)

    anyargs(1,2,3,t1=10,t2=20)




            
if __name__ == '__main__':
    main()
