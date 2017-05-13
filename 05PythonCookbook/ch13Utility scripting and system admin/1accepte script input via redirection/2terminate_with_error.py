# usage: python3 2terminate_with_error.py ;echo $?
# http://stackoverflow.com/questions/285289/exit-codes-in-python
import sys

def main():
    print('in main()')
    if 1 < 2:
        raise SystemExit('It''s failed test!')

if __name__ == "__main__":
    print(main())