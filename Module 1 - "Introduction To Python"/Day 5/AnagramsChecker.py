# Asking the user to input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Checking if the strings are anagrams
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
