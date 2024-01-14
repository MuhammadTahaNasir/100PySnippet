def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Take input from the user
user_input = input("Enter a string: ")

# Count the number of vowels
result = count_vowels(user_input)

# Print the result
print(f"The number of vowels in the string is: {result}")
