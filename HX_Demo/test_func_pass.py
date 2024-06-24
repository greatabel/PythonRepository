# import inspect

def a():
    print('a')


def b():
    print('b')


def main(funcp, t):
    funcp()
    r = funcp.__name__
    print(r)
    print(t, '#'*10)


if __name__ == "__main__":
    main(a, 'test')
    main(b, 'hello')