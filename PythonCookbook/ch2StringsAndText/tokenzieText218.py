import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' 
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def generate_tokens(pat, text):
    from collections import namedtuple
    Token = namedtuple('Token', ['type','value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())




def main():
    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'): print(tok)

if __name__ == '__main__':
    main()