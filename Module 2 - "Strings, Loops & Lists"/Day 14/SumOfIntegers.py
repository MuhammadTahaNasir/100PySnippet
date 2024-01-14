def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    number_str = str(number)

    # Initialize the sum
    digit_sum = 0

    # Sum the digits
    for digit_str in number_str:
        digit_sum += int(digit_str)

    return digit_sum

# Take input from the user
user_input = int(input("Enter an integer: "))

# Compute the sum of digits
result = sum_of_digits(user_input)

# Print the result
print(f"The sum of digits in {user_input} is:", result)
