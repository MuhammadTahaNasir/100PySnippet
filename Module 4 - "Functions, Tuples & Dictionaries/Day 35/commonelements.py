# Taking input lists from the user
list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ").split()

common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)
