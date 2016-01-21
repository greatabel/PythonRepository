# demo1: ls | python3 accepting_input.py
# demo2: python3 accepting_input.py passwd.txt 
# demo3: python3 accepting_input.py < passwd.txt 

import fileinput

with fileinput.input() as f_input: 
    for line in f_input:
        print(line, end='')

print('*'*20)

with fileinput.input('passwd1.txt') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')
