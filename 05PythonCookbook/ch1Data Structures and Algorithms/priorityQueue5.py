import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    """docstring for Item"""
    def __init__(self, name):
        self.name =  name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
        
def main():
    q = PriorityQueue()
    q.push(Item("foo1A"),1)
    q.push(Item("foo5"),5)
    q.push(Item("foo4"),4)
    q.push(Item("foo1B"),1)
    print("Q->",q._queue)
    print("pop=>",q.pop())
    print("Q->",q._queue)
    print("pop=>",q.pop())
    print("Q->",q._queue)

if __name__ == '__main__':
    main()