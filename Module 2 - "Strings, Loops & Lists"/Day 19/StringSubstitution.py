def replace_python_with_py3(word_list):
    modified_list = [word.replace("python", "Py3") for word in word_list]
    return modified_list

# Taking the input from user
user_input_list = input("Enter a list of sentences separated by commas: ")
input_list = user_input_list.split(", ")

# Applying the function 
modified_list = replace_python_with_py3(input_list)

# Printing the modified list
print("Modified List:", modified_list)
