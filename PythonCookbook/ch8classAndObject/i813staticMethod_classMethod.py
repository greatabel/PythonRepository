import colorama
from colorama import Fore, Back, Style
#http://blog.csdn.net/maoersong/article/details/32714781
class A:
    def fun0(self):
        print("call normal method")
    @staticmethod
    def fun1():
        print("call staticmethod")

    @classmethod
    def fun2(cls):
        print("call classmethod")
        print("cls.__name__ is:",cls.__name__)

        
        

def main():
    a  = A()
    a.fun0()
    a.fun1()
    a.fun2()
    A.fun2()
    A.fun1()



    print(Fore.GREEN + '-'*20 + Fore.RESET+Back.RED+'demo2'+Back.RESET)
    




if __name__ == '__main__':
    main()