import os
import sys

program = "python3"

print("Process calling")
arguments = ["called_Process.py"]

os.execvp(program, (program,) + tuple(arguments))