#encoding:utf-8
from colorama import Fore, Back, Style



def main():

    import json
    data = {
       'name' : 'ACME',
       'shares' : 100,
       'price' : 542.23
    }

    json_str = json.dumps(data)
    print("json_str=",json_str)

    dataA = json.loads(json_str)
    print(dataA)

    with open('data.json', 'w') as f:
        json.dump(data, f)

    with open('data.json','r') as f:
        dataB = json.load(f)
        print(dataB)




            
if __name__ == '__main__':
    main()
