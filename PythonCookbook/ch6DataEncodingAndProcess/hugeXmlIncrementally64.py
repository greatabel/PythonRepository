#encoding:utf-8
from colorama import Fore, Back, Style

from urllib.request import urlopen
from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

def main():
    print('start')
    from collections import Counter
    potholes_by_zip = Counter()

    data = parse_and_remove('potholes.xml', 'row/row')
    print('data=',data)
    
    for pothole in data:
        potholes_by_zip[pothole.findtext('zip')] += 1

    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)

    print(Fore.BLUE + "and content:" + Style.RESET_ALL)

    print(Back.GREEN + 'demo2'+ Back.RESET)




            
if __name__ == '__main__':
    main()
