#encoding:utf-8
from colorama import Fore, Back, Style

class Person:
    def __init__(self, first_name):
                self.first_name = first_name
    # Getter function
    @property
    def first_name(self): 
        return 'in return:'+self._first_name
    
    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string') 
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

class PersonA:
    def __init__(self, first_name):
                self.set_first_name(first_name)
            # Getter function
    def get_first_name(self): 
        return self._first_name
            # Setter function
    def set_first_name(self, value): 
        if not isinstance(value, str):
            raise TypeError('Expected a string') 
        self._first_name = value
            # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")
            # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)

def main():
    a = Person('Abel')
    print(a,'#',a.first_name)
    
    a.first_name = 'Stone'
    print(a.first_name)

    # a.first_name=42
    # del a.first_name

    print(Fore.BLUE + "other way:" + Style.RESET_ALL)
   
    b = PersonA('Greatabel')
    print(b,b.get_first_name())
    b.set_first_name("test")
    print(b.get_first_name())
    b.name = 'test1'
    print(b.name)


    print(Back.GREEN + 'demo2'+ Back.RESET)






            
if __name__ == '__main__':
    main()