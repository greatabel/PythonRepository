import random 


class A:
    def __init__(self):
        self.mylist = []

    def add_to(self, new):
        self.mylist.append(new)

    def __iter__(self):
        return (x for x in self.mylist)

def get_initial_state():
    return A()

def condition(state_var):
    return random.choice([True, False])

def calculate_from(datum):
    return datum + 10

def modify(datum, state_var):
    return datum + state_var

def modify_differently(datum):
    return datum * 100

def process(thing):
    print("process:" + str(thing))

data_set = list(range(1, 10))

# --------------------------------

# configure the data to start with
collection = get_initial_state()
state_var = None
for datum in data_set:
    if condition(state_var):
        state_var = calculate_from(datum)
        new = modify(datum, state_var)
        collection.add_to(new)
    else:
        new = modify_differently(datum)
        collection.add_to(new)

# Now actually work with the data
for thing in collection:
    process(thing)