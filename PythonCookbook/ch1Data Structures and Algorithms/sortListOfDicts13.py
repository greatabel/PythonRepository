import colorama
from colorama import Fore, Back, Style

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

def main():
    from operator import itemgetter
    print("before:", rows)
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))

    print(Fore.RED + "---" + Style.RESET_ALL)
    print(rows_by_fname)
    print(Fore.GREEN + "---" + Style.RESET_ALL)
    print(rows_by_uid)

    print(Fore.YELLOW + "---" + Style.RESET_ALL)
    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
    print(rows_by_lfname)

if __name__ == '__main__':
    main()
