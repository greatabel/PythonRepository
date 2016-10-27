from fractions import Fraction

def main():
    try:
        a = Fraction(input('Enter a fraction: '))
        print(a)
        # b = 2 + 3j
        # c = complex(20,30)
        # print(type(b),c)
        z = complex(input('Enter a complex number: '))
        print(z)
    except ZeroDivisionError:
        print('Invalid fraction')

if __name__ == "__main__":
    main()