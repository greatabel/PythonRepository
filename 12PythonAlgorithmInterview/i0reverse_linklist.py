'''
给定一个带头节点的单链表，将其逆序


#----------------------------#



'''




import time
from termcolor import colored

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_list_by_constructive(head):
    new_head = None
    while head:
        new_head = Node(head.value, new_head)
        head = head.next
    return new_head

def main_process():
    
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





