from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

        
def main():
    with open('somefile.txt') as f:
        for line, preline in search(f,'python',5):
            for pline in preline:
                print(pline, end='')
            print(line,end='')
            print('-'*20)

if __name__ == '__main__':
    main()