import random
import string

def generate_complex_password(length=12):
    # Define character sets
    letters_uppercase = string.ascii_uppercase
    letters_lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Ensure at least one character from each set
    password = [
        random.choice(letters_uppercase),
        random.choice(letters_lowercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    all_characters = letters_uppercase + letters_lowercase + digits + symbols
    password.extend(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

# Example usage
password = generate_complex_password()
print("Generated Complex Password:", password)
