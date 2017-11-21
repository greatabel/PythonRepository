class Car(object):
    def __init__(self):
        self._speed = 100


    def show_speed(self):
        print("Speed is", self._speed)
        return self._speed


    def speed(self, value):
        print("Setting to ", value)
        self._speed = value


car = Car()
car.show_speed()
car.speed(80)
car.show_speed()
