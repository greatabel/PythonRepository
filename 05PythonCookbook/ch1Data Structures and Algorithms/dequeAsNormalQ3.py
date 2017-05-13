from collections import deque

def main():
    q = deque()
    q.append(1)
    q.append(20)
    q.append(300)
    print(q)
    q.appendleft(4000)
    print(q)
    print(q.pop())
    print(q)
    print(q.popleft())
    print(q)

if __name__ == '__main__':
    main()