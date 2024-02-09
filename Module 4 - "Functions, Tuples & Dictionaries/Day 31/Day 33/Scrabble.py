def scrabble_checker(word):
    scrabbles = {
        'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3, 'h': 2, 'i': 9,
        'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2, 'q': 1, 'r': 6,
        's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2, 'x': 1, 'y': 2, 'z': 1
    }
    
    word = word.lower()
    for letter in word:
        if letter not in scrabbles or scrabbles[letter] == 0:
            return False
        else:
            scrabbles[letter] -= 1
    return True

def main():
    word = input("Enter a word to check if it's a valid Scrabble word: ")
    if scrabble_checker(word):
        print(f"'{word}' is a Scrabble word!")
    else:
        print(f"'{word}' is an invalid Scrabble word.")

if __name__ == "__main__":
    main()
