class Car(object):
    def __init__(self):
        self._speed = 100

    @property
    def speed(self):
        print("Speed is", self._speed)
        return self._speed

    @speed.setter
    def speed(self, value):
        print("Setting to ", value)
        self._speed = value


car = Car()
car.speed
car.speed = 80
car.speed 
