#encoding:utf-8
from colorama import Fore, Back, Style

#--------------1
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def print_result(result):
    print('Got:',result)

def add(x,y):
    return x + y
#------------2
class ResultHandler:
    """docstring for ResultHandler"""
    def __init__(self):
        self.sequence = 0
    def handler(self,result):
        self.sequence += 1
        print('[{}] got: {}'.format(self.sequence,result))

#------------3
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got here:{}'.format(sequence,result))
    return handler

#---------4
def make_handlerCoroutine():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] From Coroutine: {}'.format(sequence,result))
#--------5
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handlerA(result,seq):
    seq.sequence += 1
    print('[{}] Got4:{}'.format(seq.sequence,result))

def main():
    apply_async(add,(1,9),callback=print_result)
    apply_async(add,('Hello','world'),callback=print_result)

    print(Fore.BLUE + "other way 1:" + Style.RESET_ALL)
    
    r = ResultHandler()
    apply_async(add,(1,9),callback=r.handler)
    apply_async(add,('Hello','world'),callback=r.handler)
    


    print(Back.GREEN + 'other way 2:'+ Back.RESET)

    handler = make_handler()
    apply_async(add,(10,90), callback= handler)
    apply_async(add,("Great","Abel"),callback= handler)

    print(Back.BLUE + 'other way 3:'+ Back.RESET)
    handlerC = make_handlerCoroutine()
    next(handlerC)
    apply_async(add,(10,90), callback= handlerC.send)
    apply_async(add,("Great","Abel"),callback= handlerC.send)

    print(Back.RED + 'other way 4:'+ Back.RESET)
    seq = SequenceNo()
    from functools import partial
    apply_async(add,(1,9),callback=partial(handlerA,seq=seq))
    apply_async(add,("Test","Metho4"),callback=partial(handlerA,seq=seq))

            
if __name__ == '__main__':
    main()
