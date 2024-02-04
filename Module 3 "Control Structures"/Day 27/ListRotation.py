def rotated_list(input_list, positions):
    n = len(input_list)
    positions = positions % n  # Checking that positions are within the list length
    
    rotated_result = []
    for i in range(n):
        new_index = (i + positions) % n
        rotated_result.append(input_list[new_index])

    return rotated_result

user_input = input("Enter a list of numbers separated by spaces: ")
original_list = [int(x) for x in user_input.split()]

# Number of positions to rotate be entered
positions_to_rotate = int(input("Enter the number of positions to rotate: "))
result_list = rotated_list(original_list, positions_to_rotate)

print("Original List:", original_list)
print("Rotated List:", result_list)
