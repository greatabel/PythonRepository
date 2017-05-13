#encoding:utf-8
from colorama import Fore, Back, Style



def main():

    import os

    mydir = '/Users/abel/Downloads/AbelProject/PythonRepository/PythonCookbook/ch5FilesAndIO/'
    names = os.listdir(mydir)
    print(names)

    print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    print(Back.GREEN + 'Expand the user ''s home directory'+ Back.RESET)

    import os.path
    names = [ name for name in os.listdir(mydir)
        if os.path.isfile(os.path.join(mydir,name))]
    print(names)

    dirnames = [name for name in os.listdir(mydir)
                if os.path.isdir(os.path.join(mydir,name))]
    print(dirnames)

    pyfiles = [name for name in os.listdir(mydir)
                if name.endswith('.py')]
    print(pyfiles)

    print(Fore.RED + "demo3:" + Style.RESET_ALL)
    import glob
    pyfilesA = glob.glob(mydir+'/*.py')
    print(pyfilesA)

    from fnmatch import fnmatch
    pyfilesB = [name for name in os.listdir(mydir) if fnmatch(name,'*.py')]
    print(pyfilesB)


            
if __name__ == '__main__':
    main()
