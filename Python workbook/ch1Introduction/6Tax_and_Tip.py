TAX_RATE = 0.10
TIP_RATE = 0.18
cost = int(input("What is your cost? "))
tax = cost * TAX_RATE
tip = cost * TIP_RATE

print("tax: $%.2f tip: $%.2f total:$%.2f" % (tax, tip, cost))
# print("total = {0:.2f}".format(total))