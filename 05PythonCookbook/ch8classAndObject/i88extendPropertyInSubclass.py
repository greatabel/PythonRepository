#encoding:utf-8
from colorama import Fore, Back, Style

class Person:
    def __init__(self, name):
                self.name = name
    # Getter function
    @property
    def name(self): 
        return 'in return:'+self._name
    
    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string') 
        self._name = value

    # Deleter function (optional)
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")



class SubPerson(Person):
    @property
    def name(self):
        print('getting name in SubPerson')
        return super().name

    @name.setter
    def name(self,value):
        print("setting name in SubPerson",value)
        super(SubPerson, SubPerson).name.__set__(self,value)


def main():
    a = Person('Abel')
    print(a,'#',a.name)
    
    a.name = 'Stone'

    b = SubPerson('Greatabel')
    b.name = 'test'
    print(b.name)

    print(Fore.RED + "---:" + Style.RESET_ALL)
   
    


    print(Back.GREEN + '---'+ Back.RESET)






            
if __name__ == '__main__':
    main()

