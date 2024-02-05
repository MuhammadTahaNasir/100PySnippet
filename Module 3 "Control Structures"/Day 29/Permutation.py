def generate_permutations(input_list):
    if not input_list:
        return [[]]
    
    all_permutations = []
    for i in range(len(input_list)):
        remaining_elements = input_list[:i] + input_list[i+1:]
        for p in generate_permutations(remaining_elements):
            all_permutations.append([input_list[i]] + p)
    
    return all_permutations

user_input = input("Enter a list of elements separated by spaces: ")
elements_list = user_input.split()

all_permutations = generate_permutations(elements_list)

print("All Permutations:")
for permutation in all_permutations:
    print(permutation)
