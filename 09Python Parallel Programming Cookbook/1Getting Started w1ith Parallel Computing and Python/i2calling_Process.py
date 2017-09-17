import os
import sys

program = "python3"

print("Process calling")
arguments = ["i1called_Process.py"]

os.execvp(program, (program,) + tuple(arguments))
print("Good byel!")