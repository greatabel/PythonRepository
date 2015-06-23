#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style


def testA():
    items = ['a','b','c','d',1,2,3,4,5]
    
    for index, val in enumerate(items):
        print(index,val)
    print('让第一个为3，而不是0')
    for index, val in enumerate(items,3):
        print(index,val)

def testB():
    parse_data('passwdA.txt')

def testC():
    import collections
    word_summary = collections.defaultdict(list)
    with open('passwdA.txt','r') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        #当前行的单词
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)

    print(word_summary)

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f,1):
            fields = line.split(',')
            print('len=',len(fields))
            try:
                count = int(fields[1])
            except ValueError as e:
                print('line {} : Parse error : {}'.format(lineno,e))
            except IndexError as ie:
                print('line {} : my IndexError error : {}'.format(lineno,ie))


def main():
    print(Back.GREEN + 'and with a green background'+Back.RESET )
    testB()
    print(Back.RED + 'and with a red background'+Back.RESET )
    testA()
    print(Back.YELLOW + 'and with a yellow background'+Back.RESET )
    testC()
    
    

            
if __name__ == '__main__':
    main()

