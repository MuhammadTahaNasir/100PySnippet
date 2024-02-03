def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    
    if length % 2 == 0:
        left_middle = sorted_numbers[length // 2 - 1]
        right_middle = sorted_numbers[length // 2]
        median = (left_middle + right_middle) / 2
    else:
        median = sorted_numbers[length // 2]
    
    return median

# Taking input from the user for a list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(x) for x in user_input.split()]

median_value = calculate_median(numbers_list)
print(f"Original List: {numbers_list}")
print(f"Median: {median_value}")
