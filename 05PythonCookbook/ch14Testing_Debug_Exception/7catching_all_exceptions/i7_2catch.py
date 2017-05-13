import sys

def parse_int(s):
    try:
        # 我们故意写个不存在的v
        n = int(v)
    except Exception:
        print("Counldn't parse")

def parse_int_BetterVersion(s):
    try:
        # 我们故意写个不存在的v
        n = int(v)
    except Exception as e:
        print("Counldn't parse")
        print('Reason:', e)

if __name__ == "__main__":
    parse_int('n/a')
    parse_int(10)
    parse_int(10.2)
    print('###')
    parse_int_BetterVersion('n/a')
