#encoding:utf-8
from colorama import Fore, Back, Style


def main():
    stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
        ]

    import sqlite3
    db = sqlite3.connect('database.db')
    c = db.cursor()
    c.execute('create table portfolio (symbol text, shares integer, price real)')
    db.commit()

    c.executemany('insert into portfolio values (?,?,?)', stocks)
    db.commit()

    for row in db.execute('select * from portfolio'):
        print(row)

    print(Fore.BLUE + "and content:" + Style.RESET_ALL)

    print(Back.GREEN + 'demo2'+ Back.RESET)




            
if __name__ == '__main__':
    main()
