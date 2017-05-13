import colorama
from colorama import Fore, Back, Style

def demo():
    # Determine if any .py files exist in a directory
    import os
    print(os.getcwd())
    files = os.listdir(os.getcwd())
    if any(name.endswith('.py') for name in files):
        print('There be python!') 
    else:
        print('Sorry, no python.')
      # Output a tuple as CSV
    s = ('ACME', 50, 123.45) 
    print(','.join(str(x) for x in s))
      # Data reduction across fields of a data structure
    portfolio = [
         {'name':'GOOG', 'shares': 50},
         {'name':'YHOO', 'shares': 75},
         {'name':'AOL', 'shares': 20},
         {'name':'SCOX', 'shares': 65}
      ]
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)

def main():
  demo()
  nums = [1, 2, 3, 4, 5]
  print(sum(x**2 for x in nums))

if __name__ == '__main__':
    main()
