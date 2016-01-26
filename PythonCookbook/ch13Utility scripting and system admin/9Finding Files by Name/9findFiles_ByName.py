import os
import sys

# python3 9Finding\ Files\ by\ Name/9findFiles_ByName.py  9Finding\ Files\ by\ Name/ test.txt
def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == "__main__":
    findfile(sys.argv[1], sys.argv[2])