def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCD
result = gcd(num1, num2)

# Unveiling the Result
print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is:", result)
