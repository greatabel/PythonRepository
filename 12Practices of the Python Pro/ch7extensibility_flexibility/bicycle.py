class Tire:
    def __repr__(self):
        return 'A rubber tire'


class Frame:
    def __repr__(self):
        return 'An aluminum frame'

class Bicycle:
    def __init__(self):
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()

    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')


if __name__ == '__main__': 
    bike = Bicycle()
    bike.print_specs()