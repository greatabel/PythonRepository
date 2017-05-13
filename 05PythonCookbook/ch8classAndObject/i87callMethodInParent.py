#encoding:utf-8
from colorama import Fore, Back, Style

class A:
    def __init__(self):
        self.x = 0

    def spam(self):
        print("A.spam")

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam')
        super().spam()

def main():
    a = A()
    a.spam()
    print(a.x)
    print('##')
    b = B()
    b.spam()
    print(b.x,b.y)

    print(Fore.RED + "---:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + '---'+ Back.RESET)






            
if __name__ == '__main__':
    main()

