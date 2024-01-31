def long_words(n, input_str):
    word_len = []
    txt = input_str.split(" ")
    
    for x in txt:
        if len(x) > n:
            word_len.append(x)

    return word_len

# Taking input from the user for 'n' and the input string
n = int(input("Enter the value of 'n': "))
user_input_str = input("Enter a string: ")

# Calling the 'long_words' function with user input and print the result
result = long_words(n, user_input_str)
print(result)
