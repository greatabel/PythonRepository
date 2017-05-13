RATE = 0.04
saving = float(input("How many  saving? "))
oneyear = saving * (1 + RATE)
twoyear = oneyear * (1 + RATE)
threeyear = twoyear * (1 + RATE)

print("first: $%.2f next: $%.2f 2year later:$%.2f" % (oneyear, twoyear, threeyear))
