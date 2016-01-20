# demo1: ls | python3 accepting_input.py

import fileinput

with fileinput.input() as f_input: 
    for line in f_input:
        print(line, end='')
