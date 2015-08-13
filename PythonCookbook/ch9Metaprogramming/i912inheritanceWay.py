class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)
# Example:
class A(LoggedGetattribute): 
    def __init__(self,x):
        self.x = x 

    def spam(self):
        pass


if __name__ == "__main__":
    a = A(12)
    print(a.x)
    a.spam()
