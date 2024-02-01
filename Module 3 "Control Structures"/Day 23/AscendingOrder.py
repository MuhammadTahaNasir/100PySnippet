def ascending_list(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

# Checking if the list is sorted in ascending order
if ascending_list(user_list):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")
