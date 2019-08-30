'''
给定一个带头节点的单链表，将其逆序


#----------------------------#



'''




import time
from termcolor import colored


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'LinkedList({}, {})'.format(self.value, repr(self.next))


def reverse(item, tail = None):
    next = item.next
    item.next = tail
    if next is None:
        return item
    else:
        return reverse(next, item)


def main_process():
    
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





