def example():
    try:
        int('N/A')
    except ValueError:
        print('in example():not work')
        raise

if __name__ == '__main__':
    # try:
    #     example()
    # except Exception as e:
    #     print('1:', e)
    example()
        
    

