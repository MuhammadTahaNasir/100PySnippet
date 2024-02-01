def caesar_cipher(text, shift, action='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset) if action == 'encrypt' else chr((ord(char) - offset - shift) % 26 + offset)
            result += shifted_char
        else:
            result += char
    return result

plaintext = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(plaintext, shift_value)
decrypted_text = caesar_cipher(encrypted_text, shift_value, action='decrypt')

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
