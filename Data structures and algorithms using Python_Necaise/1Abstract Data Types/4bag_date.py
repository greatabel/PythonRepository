from linearbag import Bag
from date import Date

def main():
    bornBefore = Date(6, 1, 1988)
    bag = Bag()

    date = promptAndExtractDate()
    while date is not None:
        print(date)
        bag.add(date)
        date = promptAndExtractDate()

    print('#'*10)
    for i in bag:
        print(i)

def promptAndExtractDate():
   print( "Enter a birth date." )
   month = int( input("month (0 to quit): ")) 
   if month==0:
      return None 
   else :
      day = int( input("day: ") ) 
      year = int( input("year: ") ) 
      return Date( month, day, year)

#Call the main routine.
if __name__ == "__main__":
   main()