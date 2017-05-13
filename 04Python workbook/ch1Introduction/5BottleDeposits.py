LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25
less = int(input("What is your containers 1 liter or less? "))
more = int(input("What is your containers more than 1 liter ? "))
total = LESS_DEPOSIT * less + MORE_DEPOSIT * more
print("total: $%.2f" % total)
# print("total = {0:.2f}".format(total))