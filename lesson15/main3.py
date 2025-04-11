import random
import string

def generate_password(length=8):
    """
    Generate a random password ensuring at least one lowercase letter,
    one uppercase letter, one digit, and one special character.

    Args:
        length (int): Total length of the password. Must be at least 4.

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all required character types.")

    # Guarantee at least one character from each category:
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest of the password with random selections from all allowed characters
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = random.choices(all_chars, k=remaining_length)

    # Combine the selected characters and shuffle to avoid a predictable pattern
    password_list = [lower, upper, digit, special] + remaining_chars
    random.shuffle(password_list)

    return ''.join(password_list)

# Example usage:
if __name__ == "__main__":
    desired_length = 12  # you can adjust this length as needed
    print("Randomly generated password:", generate_password(desired_length))
