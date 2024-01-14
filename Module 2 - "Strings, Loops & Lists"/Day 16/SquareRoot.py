def calculate_square_root(number):
    if number < 0:
        return "Undefined for negative numbers"
    guess = number / 2.0

    # Iterate using the Babylonian method for a more accurate result
    for _ in range(10):  
        guess = (guess + number / guess) / 2.0

    return guess

# Take input from the user
user_input = float(input("Enter a number: "))

# Calculate the square root
result = calculate_square_root(user_input)

# Print the result
print(f"The square root of {user_input} is approximately:", result)
