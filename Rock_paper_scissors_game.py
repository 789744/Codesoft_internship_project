import random
import string

def generate_password(length, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("\n----- Password Generator -----")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("⚠ Length must be greater than zero.")
            return

        symbol_choice = inpu_
