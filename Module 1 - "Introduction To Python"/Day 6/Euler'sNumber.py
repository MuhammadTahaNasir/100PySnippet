# Calculating the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1.0
    else:
        return n * factorial(n - 1)

# Function to estimate Euler's Number (e) using the expansion of series
def calculate_euler_number(terms):
    e = 1.0

    for i in range(1, terms + 1):
        e += 1.0 / factorial(i)

    return e

terms = int(input("Enter the number of terms to estimate Euler's Number: "))

# Calculating the estimated value of Euler's Number
e = calculate_euler_number(terms)
print(f"Estimated value of Euler's Number (e) with {terms} terms: {e}")
