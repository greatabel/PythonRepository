import os

def main():
    sz = os.get_terminal_size()
    print(sz.columns, 'columns')
    print(sz.lines, 'lines')
    for i in range(sz.lines):
        print(i+1)

if __name__ == "__main__":
    main()

