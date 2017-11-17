import random 


def condition(state_var):
    return random.choice([True, False])

def modify(datum, state_var=10):
    return datum + state_var

def process(thing):
    print("process:" + str(thing))

data_set = list(range(1, 10))

# --------------------------------
# collection = get_initial_state()

collection = [d if condition(d) else modify(d)
             for d in data_set]

# Now actually work with the data
for thing in collection:
    process(thing)