'''
1.1 给定一个带头节点的单链表，将其逆序
即如果单链表原来为 head -> 1 -> 2 -> 3 逆序后变成 head -> 3 -> 2 -> 1

#----------------------------#



'''


import time
from termcolor import colored


class Node:
    def __init__(self, data, nextnode=None):
        self.data = data
        self.nextnode = nextnode


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add_node(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def print_node(self):
        print('head -> ', end='')
        curr = self.head
        while curr:
            print(curr.data, ' -> ', end='')
            curr = curr.nextnode
        print('\n')

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.nextnode
            # print('next=', next)
            curr.nextnode = prev
            prev = curr
            curr = next
        self.head = prev


def main_process():
    linkedlist = LinkedList()
    for i in reversed(range(1, 7+1)):        
        linkedlist.add_node(i)
        print('i=', i)

    linkedlist.print_node()
    print('reverse_list:')
    linkedlist.reverse_list()
    linkedlist.print_node()
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





