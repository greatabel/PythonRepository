def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))

def main():
    try:
        a = float(input('Enter a number: '))
        
        multi_table(float(a))
    except ValueError:
        print('You entered an invalid input')    


if __name__ == "__main__":
    main()