import weakref
# cls 和 self 区别
# http://stackoverflow.com/questions/4613000/what-is-the-cls-variable-used-in-python-classes
class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print("Initializing Spam")
        self.name = name

if __name__ == "__main__":
    s = Spam('Abel')
    t = Spam('Abel')
    c = Spam('xiaoming')
    print(s is t)