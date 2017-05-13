#encoding:utf-8
from colorama import Fore, Back, Style

from urllib.request import urlopen
from xml.etree.ElementTree import parse

def main():
    print('start')
    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)
    print('doc=',doc)
    for item in doc.iterfind('channel/item'): 
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')
        print(title) 
        print(date) 
        print(link) 
        print()
    print(Fore.BLUE + "and content:" + Style.RESET_ALL)

    print(Back.GREEN + 'demo2'+ Back.RESET)




            
if __name__ == '__main__':
    main()
