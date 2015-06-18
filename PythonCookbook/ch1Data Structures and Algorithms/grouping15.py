import colorama
from colorama import Fore, Back, Style

rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

def main():
    from operator import itemgetter
    from itertools import groupby

    print("before:", rows)

    print(Fore.RED + "---" + Style.RESET_ALL)
    rows.sort(key=itemgetter('date'))
    print(rows)
    print(Fore.GREEN + "---" + Style.RESET_ALL)
    
    for date, items in groupby(rows,key=itemgetter('date')):
        print(date)
        for i in items:
            print(" ",i)


    print(Fore.GREEN + "---" + Style.RESET_ALL)




if __name__ == '__main__':
    main()
