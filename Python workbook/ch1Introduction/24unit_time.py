#http://stackoverflow.com/questions/7378091/taking-multiple-inputs-from-user-in-python
# the book 's answer is wrong
input = input("Enter days hours minutes separated by commas: ")

input_list = input.split(',')

total = float(input_list[0]) * 24 * 60 * 60  + float(input_list[1]) * 60 * 60 +float(input_list[2]) * 60
print("total seconds: %.02f" %total)