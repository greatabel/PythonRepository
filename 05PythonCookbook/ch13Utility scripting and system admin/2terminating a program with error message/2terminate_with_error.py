import sys

def main():
    print('in main()')
    if 1 < 2:
        raise SystemExit('It''s failed test!')

if __name__ == "__main__":
    main()