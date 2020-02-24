def get_number_with_highest_count(counts):  # <1>
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = {}
    for number in numbers:  # <2>
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return get_number_with_highest_count(counts)

nums = ['red', 'red', 'blue', 'red', 'pink', 'blue']
print(most_frequent(nums))