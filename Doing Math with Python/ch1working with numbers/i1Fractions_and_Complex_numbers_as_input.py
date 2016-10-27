from fractions import Fraction

def main():
    try:
        a = Fraction(input('Enter a fraction: '))
        print(a)
    except ZeroDivisionError:
        print('Invalid fraction')

if __name__ == "__main__":
    main()