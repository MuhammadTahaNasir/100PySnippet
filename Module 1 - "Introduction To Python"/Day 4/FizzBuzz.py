# Setting the range for the FizzBuzz
current = 1
end = 100

while current <= end:
    
    if current % 3 == 0 and current % 5 == 0:
        print("FizzBuzz")
    
    elif current % 3 == 0:
        print("Fizz")
    
    elif current % 5 == 0:
        print("Buzz")
    
    else:
        print(current)

    # Moving to the next number
    current += 1
