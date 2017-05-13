class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open') 
        print('reading')
    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open') 
        print('writing')
    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open') 
        self.state = 'OPEN'
    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed') 
        self.state = 'CLOSED'


if __name__ == '__main__':
    c = Connection()
    print(c)
    print('#'*10)
    try:
        c.read()
    except RuntimeError as e:
        print('myerror: ',e)

    c.open()
    c.write('t')
    c.close()