import sys

def main():
    print('in main()')
    sys.stderr.write('It failed\n')
    raise SystemExit(1)

if __name__ == "__main__":
    main()