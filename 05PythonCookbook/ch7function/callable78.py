#encoding:utf-8
from colorama import Fore, Back, Style

def spam(a,b,c,d):
    print(a,b,c,d)


def main():
    from functools import partial
    s1 = partial(spam,1)
    s1(2,3,4)
    s1(20,30,40)
    print(Fore.RED + "other way:" + Style.RESET_ALL)
    s2 = partial(spam,d=100)
    s2(1,2,3)
    s2(10,20,30)
    
    

    print(Back.GREEN + 'demo2'+ Back.RESET)
    s3 = partial(spam,1,2,d=100)
    s3(3)
    s3(4)
    s3(1000)

    print(Back.GREEN + '*'*15+ Back.RESET)

    import math
    def distance(p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.hypot(x2 - x1, y2 - y1)
    points = [(1,2),(3,4),(5,6),(7,8)]

    pt = (4,3)
    points.sort(key=partial(distance,pt))
    print(points)

    
    
   
    









            
if __name__ == '__main__':
    main()
