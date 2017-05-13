#encoding:utf-8
from colorama import Fore, Back, Style

def sample():
    n = 0
    def func():
        print('n=',n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # attach as function attribut
    func.get_n = get_n
    func.set_n = set_n

    return func


def main():
    f = sample()
    f()
    f.set_n(100)
    f()
    print('here=',f.get_n())

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()
