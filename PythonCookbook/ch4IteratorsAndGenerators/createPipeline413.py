from colorama import Fore, Back, Style

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    find all filenames in a directory
    '''
    for path, dirlist, filelist in os.walk(top):
        print(Back.GREEN + 'path='+path+' dirlist='+str(dirlist)+'# fileist='+str(filelist)+Back.RESET )
        for name in fnmatch.filter(filelist, filepat):
            print('in gen_find path=>',path,'name=>',name,'all=>  ',os.path.join(path,name))
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration. 
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line




def main():
    print(Back.GREEN + 'my way'+Back.RESET )
    
    # Example 1
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)

    # Example 2
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total kbytes', sum(bytes)/1024)


    
    
    

            
if __name__ == '__main__':
    main()

