def roots(a,b,c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

if __name__ == "__main__":
    a = input('Enter a:')
    b = input('Enter b:')
    c = input('Enter c:')
    print('a,b,c=', float(a), float(b), float(c))
    roots(float(a), float(b), float(c))