BREAD_PRICE = 3.49
DISC = 0.6

num_loaves = int(input("Enter num:"))

regular_price = num_loaves * BREAD_PRICE
discount = regular_price * DISC
total = regular_price - discount

print("regular_price: %5.2f discount: %5.2f total: %5.2f" %(regular_price, discount,total))