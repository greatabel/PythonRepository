import os
import time

# usage of this script, something like:python3 10find_ByModifytime.py  . 3600


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            print('fullpath=', fullpath)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                print('mtime=',mtime,'now=',now,'sub=',(now - mtime))
                if mtime > (now - seconds):
                    print(fullpath,'\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)
    
    modified_within(sys.argv[1], float(sys.argv[2]))

