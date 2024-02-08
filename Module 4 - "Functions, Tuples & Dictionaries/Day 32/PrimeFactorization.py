import math

def prime_factors(num):
    factors = []

    # Check for divisibility by 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # Check for divisibility by odd numbers starting from 3
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i

    # If num is a prime number greater than 2
    if num > 2:
        factors.append(num)

    return factors

def main():
    # Asking the user to enter a number
    num = int(input("Enter a number: "))

    # Calculating and print the prime factors of the entered number
    factors = prime_factors(num)
    print("Prime factors of", num, "are:", factors)

if __name__ == "__main__":
    main()
