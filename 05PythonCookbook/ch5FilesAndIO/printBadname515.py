def bad_filename(filename): 
    return repr(filename)[1:-1]



from colorama import Fore, Back, Style



def main():

    import os

    mydir = '/Users/abel/Downloads/AbelProject/PythonRepository/PythonCookbook/ch5FilesAndIO/'
    names = os.listdir(mydir)
    # print(names)

    print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    print(Back.GREEN + 'Expand the user ''s home directory'+ Back.RESET)

    try: 
        print(names)
    except UnicodeEncodeError: 
        print(bad_filename(filename))

            
if __name__ == '__main__':
    main()