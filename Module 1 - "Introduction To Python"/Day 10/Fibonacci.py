def fibonacci_series(n):
    first, second = 0, 1
    fibonacci_sequence = []

    print(f"Fibonacci Sequence up to {n} terms:")

    for _ in range(n):
        print(first, end=", ")
        fibonacci_sequence.append(first)
        first, second = second, first + second

    print()
    return fibonacci_sequence

def main():
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    fibonacci_sequence = fibonacci_series(n)

if __name__ == "__main__":
    main()
