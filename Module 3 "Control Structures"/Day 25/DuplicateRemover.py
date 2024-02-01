def no_duplicates(original_list):
    updated_list = []
    for item in original_list:
        if item not in updated_list:
            updated_list.append(item)
    return updated_list

# Ask the user for a list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")
original_list = [int(x) for x in user_input.split()]

# Remove duplicates
result_list = no_duplicates(original_list)

print("Original List:", original_list)
print("List without Duplicates:", result_list)
