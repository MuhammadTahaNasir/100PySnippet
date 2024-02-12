def roman_to_integer(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_numerals[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
            
        prev_value = value
    
    return total

def main():
    roman_numeral = input("Enter a Roman numeral: ").upper()
    integer_value = roman_to_integer(roman_numeral)
    print(f"The integer value of {roman_numeral} is {integer_value}")

if __name__ == "__main__":
    main()
