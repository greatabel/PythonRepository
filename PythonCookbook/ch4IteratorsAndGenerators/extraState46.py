#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style
from collections import deque

class linehistory:

    def __init__(self, lines, hislen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def main():
    print(Back.GREEN + 'and with a green background'+Back.RESET )
    with open('passwd.txt') as f:
        lines = linehistory(f)

        for line in lines:
            print('line=> ',line)
            if 'ps1' in line:
                print('lines.history=',lines.history)
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno,hline),end='')
    
    

            
if __name__ == '__main__':
    main()

