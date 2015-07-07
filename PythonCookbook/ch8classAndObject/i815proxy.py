import colorama
from colorama import Fore, Back, Style

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


if __name__ == '__main__':
    class Spam:
        def __init__(self, x):
            self.x = x

        def bar(self, y):
            print('Spam.bar:', self.x, y)

    s = Spam(1)
    s.bar(9)

    print(Fore.GREEN + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)

    p = Proxy(s)
    print(p.x)
    p.bar(900)
    p.x = 100
    print(p.x)


