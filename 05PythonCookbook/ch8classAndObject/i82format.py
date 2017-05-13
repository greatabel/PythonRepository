#encoding:utf-8
from colorama import Fore, Back, Style

_formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}/{d.day}/{d.year}',
        'dmy' : '{d.day}/{d.month}/{d.year}'
        }

class Date:
    def __init__(self, year, month, day):
                self.year = year
                self.month = month
                self.day = day

    def __str__(self):
        return '@^@({0.year!s},{0.month!s},{0.day!r})'.format(self)
        
    def __format__(self,code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

def main():
    d = Date(2015, 6, 30)
    print(d,'#',format(d))

    print(format(d,'mdy'))

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()

