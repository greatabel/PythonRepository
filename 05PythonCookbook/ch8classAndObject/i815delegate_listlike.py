import colorama
from colorama import Fore, Back, Style

class ListLike:
    def __init__(self):
        self._items = []
    def __getattr__(self,name):
        return getattr(self._items, name)

    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __delitem__(self, index):
        del self._items[index]

if __name__ == '__main__':
    a = ListLike()
    a.append(2)
    print(a)
    a.insert(0,10)
    a.insert(0,100)
    print(Fore.GREEN + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)
    print('len(a)=',len(a))
    print(a[0],'#',a[1])
    a.sort()
    print(a._items)
  