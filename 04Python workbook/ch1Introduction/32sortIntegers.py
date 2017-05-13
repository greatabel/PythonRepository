input = input("Enter 3integers separated by commas: ")

input_list = input.split(',')
mylist = []
mylist.append(float(input_list[0]))
mylist.append(float(input_list[1]))
mylist.append(float(input_list[2]))
print(sorted(mylist))