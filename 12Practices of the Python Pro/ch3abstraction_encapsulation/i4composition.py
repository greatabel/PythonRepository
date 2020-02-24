class SpeakMixin:  # <1>
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f'The {name} says, "Hello!"')


class RollOverMixin:  # <2>
    def roll_over(self):
        print('Did a barrel roll!')


class Dog(SpeakMixin, RollOverMixin):  # <3>
    pass


dog = Dog()
dog.speak()
dog.roll_over()