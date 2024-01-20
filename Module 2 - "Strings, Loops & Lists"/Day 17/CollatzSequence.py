def collatz_sequence(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # Print the final 1

starting_number = int(input("Enter a positive integer: "))

if starting_number <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Collatz sequence for {starting_number}: ", end="")
    collatz_sequence(starting_number)
