#encoding:utf-8
from colorama import Fore, Back, Style

from urllib.request import urlopen

class UrlTemplate:
    def __init__(self,template):
        self.template = template
    def open(self ,**kwargs):
        return urlopen(self.template.format_map(kwargs))

#------
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener

if __name__ == '__main__':
    yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
    print(Back.GREEN + 'demo2'+ Back.RESET)
    
    yahooA = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahooA(names="IBM,AAPL,FB", fields='sl1c1v'):
        print(line.decode('utf-8'))


