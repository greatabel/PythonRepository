def example1():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e

def example2():
    try:
        int('N/A')
    except ValueError as e:
        print('# It failded. Reason:', e)

def example3():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from None

if __name__ == '__main__':
    try:
        example1()
    except Exception as e:
        print('1:', e)
        
    try:
        example2()
    except Exception as e:
        print('2:', e)

    try:
        example3()
    except Exception as e:
        print('3:', e)

