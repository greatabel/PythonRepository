from colorama import Fore, Back, Style

def main():

    import csv
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        heads = next(f_csv)
        print('heads=',heads)
        print(Fore.BLUE + "and content:" + Style.RESET_ALL)
        for row in f_csv:
            print(row)

    print(Back.GREEN + 'demo2'+ Back.RESET)
    from collections import namedtuple
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            print(row)

            
if __name__ == '__main__':
    main()