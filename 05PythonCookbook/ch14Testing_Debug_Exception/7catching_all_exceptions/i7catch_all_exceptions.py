#  https://docs.python.org/2/tutorial/errors.html
import sys

if __name__ == "__main__":
    try:
        f = open('test.txt')
        s = f.readline()
        i = int(s.strip())
    except Exception as e:
        print('Reason:', e)
