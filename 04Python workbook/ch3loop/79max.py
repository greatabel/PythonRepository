from random import randrange

NUM_ITEMS = 100

max_value = randrange(1, NUM_ITEMS + 1)
print(max_value)

num_updates = 0

for i in range(1,NUM_ITEMS):
	current = randrange(1,NUM_ITEMS + 1)

	if current > max_value:
		max_value = current
		num_updates = num_updates + 1
		print(current,"<== Update")
	else:
		print(current)

print("Max=", max_value)
print("The maximum value was updated",num_updates ,"times")