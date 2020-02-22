from i0sales_tax import add_sales_tax


def print_receipt():
    total = 10
    state = 'MI'
    print(f'TOTAL: {total}')
    print(f'AFTER TAX: {add_sales_tax(total, state)}')  # <2>


import i0sales_tax


def print_receipt():
    total = 10
    locale = 'MI'
    print(f'AFTER MILLAGE: {i0sales_tax.add_sales_tax(total, locale)}')

if __name__ == "__main__":
    print_receipt()