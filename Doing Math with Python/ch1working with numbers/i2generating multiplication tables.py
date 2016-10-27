from fractions import Fraction

def multi_table(a, n):
    for i in range(1, n+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

def main():
    try:
        a = float(input('Enter a number: '))
        n = float(input('Enter the number of multiples: '))
        if not n.is_integer() or n < 0:
            print('The number of multiples should be a positive integer')
        else:
            multi_table(a, int(n))
    except ValueError:
        print('You entered an invalid input')    


if __name__ == "__main__":
    main()