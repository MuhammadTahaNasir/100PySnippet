def count_character_occurrences(input_string):
    char_count = {}

    for char in input_string:
        # Increment the count for each character
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

# Take input from the user
user_input = input("Enter a string: ")

# Count the occurrences of each character
result = count_character_occurrences(user_input)

# Print the character occurrences
print("Character occurrences:")
for char, count in result.items():
    print(f"'{char}': {count}")
