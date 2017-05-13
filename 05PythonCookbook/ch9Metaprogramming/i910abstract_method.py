from abc import ABCMeta, abstractmethod

class MyABC(metaclass=ABCMeta):
    pass

MyABC.register(tuple)

assert issubclass(tuple, MyABC)

assert isinstance((), MyABC)

class Headers(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.headers = ''

    @abstractmethod
    def _getAHeaders(self):
        pass

    def __str__(self):
        return str(self.headers)

    def __repr__(self):
        return repr(self.headers)

class AHeaders(Headers):

    def __init__(self,url, username, password):
        self.url = url
        self.headers = self._getAHeaders(username, password)

    def _getAHeaders(self, username,password):
        print(username,password, "in AHeaders _getAHeaders!")

a = AHeaders("www.a.com", 'abel', '1234')
