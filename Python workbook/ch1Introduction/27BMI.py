input = input("Enter weight height separated by commas: ")

input_list = input.split(',')

BMI = 703 * float(input_list[0])/ (float(input_list[1]) ** 2)
print(" BMI: %.02f " %BMI )