class Thing(object): pass
class Rock(Thing): pass
class Paper(Thing): pass
class Scissors(Thing): pass

def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None         # No winner
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Paper):
        if isinstance(y, Rock):
                return x
        elif isinstance(y, Paper):
            return None         # No winner
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y, Rock):
            return y
        elif isinstance(y, Paper):
            return x
        elif isinstance(y, Scissors):
            return None         # No winner
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")

rock, paper, scissors = Rock(), Paper(), Scissors()