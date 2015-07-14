from datetime import datetime, date
import json

class Jsonable(object):

    def date_handler(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()

    def save_json(self, file_name):
        with open(file_name, 'w') as output:
            output.write(json.dumps(self.__dict__, default=self.date_handler))

class Person(Jsonable):

    def __init__(self, name, bday):
        self.name = name
        self.bday = bday


if __name__ == '__main__':
    matt = Person('matt', date(1983, 7, 12))
    matt.save_json("matt.json")
    assert issubclass(Person, Jsonable)
    assert isinstance(matt, Person)
    assert isinstance(matt, Jsonable)
    print(issubclass(Person, Jsonable),isinstance(matt, Person),isinstance(matt, Jsonable))