from urllib.request import urlopen
import csv

def downprices():
    u = urlopen('file:///Users/wanchang/Downloads/AbelProject/PythonRepository/PythonCookbook/ch14Testing_Debug_Exception/2patching_objects/test.csv') 
    lines = (line.decode('utf-8') for line in u)

    rows = (row for row in csv.reader(lines) if len(row) == 2)
    # for  name,price in rows:
    #     print('#',name, "price=",float(price))
    prices = { name:float(price) for name, price in rows }
    # print(prices)
    return prices

if __name__ == "__main__":
    result = downprices()
    print(result)