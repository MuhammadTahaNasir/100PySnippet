# Taking the input from user
user_input = input("Enter a string: ")

# Removing non-alphanumeric characters and converting it to lowercase
cleaned_string = ''.join(char.lower() for char in user_input if char.isalnum())

# Checking if the cleaned string is equal to its reverse or not 
if cleaned_string == cleaned_string[::-1]:
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
