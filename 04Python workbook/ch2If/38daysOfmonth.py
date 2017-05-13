#http://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python
from calendar import monthrange
input = input("Enter weight height separated by commas: ")

input_list = input.split(',')
output = monthrange(int(input_list[0]),int(input_list[1]))
print(output[1])
