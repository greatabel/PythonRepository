import warnings

# usage:
# python3 -W all i11issue_warn.py 
# python3 -W error i11issue_warn.py 

def func(x, y, logfile=None, debug=False):
    print("#", logfile)
    if logfile is not None:
        warnings.warn('logfile argument depressed', DeprecationWarning)

if __name__ == "__main__":
    func(1, 2,'mylog')
