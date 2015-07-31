#https://hg.python.org/cpython/file/2.7/Demo/scripts/pi.py
#有趣


import sys

def main():
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        # Next approximation
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        # Print common digits
        d, d1 = a//b, a1//b1
        while d == d1:
            output(d)
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = a//b, a1//b1

def output(d):
    # Use write() to avoid spaces between the digits
    sys.stdout.write(str(d))
    # Flush so the output is seen immediately
    sys.stdout.flush()

if __name__ == "__main__":
    main()