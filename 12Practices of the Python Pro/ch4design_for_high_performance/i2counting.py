colors = {'red': 2, 'blue': 3, 'pink': 1}

def get_number_with_highest_count(counts):  # <1>
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


print(colors, get_number_with_highest_count(colors))