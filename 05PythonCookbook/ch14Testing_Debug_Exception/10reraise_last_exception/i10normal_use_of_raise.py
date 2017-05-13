if __name__ == '__main__':
    # try:
    #     example()
    # except Exception as e:
    #     print('1:', e)
    if 1 < 2:
        raise Exception('I am boring')
    
    try:
        int('N/A')
    except Exception as e:
        # do some process here
        print(e)
        # and then pass error on
        raise
        