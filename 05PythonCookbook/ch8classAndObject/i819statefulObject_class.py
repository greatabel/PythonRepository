class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, state):
        self.__class__ = state

    # Delegate to the state class
    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()
    def open(self):
         raise NotImplementedError()
    def close(self):
         raise NotImplementedError()




class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')

    def write(self, data):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed')  

class OpenConnection(Connection):
    def read(self):
        print('reading')

    def write(self, data):
        print('writing')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)

if __name__ == '__main__':
    c = Connection()
    print(c)
    print('#'*10)
    print(c.__class__)
    try:
        c.read()
    except RuntimeError as e:
        print('myerror: ',e)

    c.open()
    c.write('t')
    c.close()