import colorama
from colorama import Fore, Back, Style

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'MyNode({!r})'.format(self._value)

    def addChild(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


def main():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(20)
    child3 = Node(3)
    root.addChild(child1)
    root.addChild(child2)
    root.addChild(child3)
    
    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    for ch in root:
        print(ch)
            
if __name__ == '__main__':
    main()

