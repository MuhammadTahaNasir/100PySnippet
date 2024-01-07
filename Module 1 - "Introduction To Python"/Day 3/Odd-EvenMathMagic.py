# Getting the input from the user

user_input = int(input("Enter a positive integer: "))

# For checking of the positive number 
if user_input > 0:
    
    #Calculating the sum of even numbers 
    even_numbers = [i for i in range(2, user_input + 1, 2)] 
    sum_even = sum(even_numbers)

    #Calculating the product of odd numbers 
    odd_numbers = [i for i in range(1, user_input + 1, 2)]
    product_odd = 1
    for num in odd_numbers:
        product_odd *= num

    print(f"Sum of even numbers: {sum_even}")
    print(f"Product of odd numbers: {product_odd}")
else:
    # For non-positive numbers 
    print("Please enter a positive integer.")
