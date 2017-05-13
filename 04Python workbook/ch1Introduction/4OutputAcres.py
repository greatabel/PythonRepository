SQFT_PER_ACRE = 43560
mylength = input("What is your length? ")
mywidth = input("What is your width? ")
erea = float(mylength)*float(mywidth)
acres = erea/SQFT_PER_ACRE
print("hello erea's Acres = {0:.2f}".format(acres))