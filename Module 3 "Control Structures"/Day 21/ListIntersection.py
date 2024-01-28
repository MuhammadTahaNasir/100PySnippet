# Taking input from the user for the first and second list
input_str1 = input("Enter elements of the first list separated by spaces: ")
list1 = [int(x) for x in input_str1.split()]

input_str2 = input("Enter elements of the second list separated by spaces: ")
list2 = [int(x) for x in input_str2.split()]

# Finding the intersection of the two lists
intersection = list(set(list1) & set(list2))

# Displaying the result
print("Intersection of the two lists:", intersection)
