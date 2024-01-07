import random
import string

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

def main():
    length = int(input("Enter the desired length for the password: "))
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
