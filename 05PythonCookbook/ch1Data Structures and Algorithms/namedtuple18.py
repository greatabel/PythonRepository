import colorama
from colorama import Fore, Back, Style



def main():
    
  from collections import namedtuple
  Subscriber = namedtuple("Subscriber",['address','joinedtime'])

  sub = Subscriber('abel@126.com','2015-06-19')
  subA = Subscriber('abelA@126.com','2015-05-20')
  print(sub,"|",sub.address,"|", sub.joinedtime)
  print(subA,"|",subA.address,"|", subA.joinedtime)

  #http://stackoverflow.com/questions/12087905/pythonic-way-to-sorting-list-of-namedtuples-by-field-name
  seq = [sub, subA]
  print("seq=",seq)
  from operator import attrgetter
  print(sorted(seq, key=attrgetter('address')))
  print(sorted(seq, key=attrgetter('joinedtime')))

if __name__ == '__main__':
    main()
