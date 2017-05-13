from functools import wraps

def thisIsliving(fun):
    @wraps(fun)
    def living(*args, **kw):
        return fun(*args, **kw) +" #Test:living"
    return living

@thisIsliving
def whatIsLiving():
    return "???"

if __name__ == "__main__":
    print(whatIsLiving())