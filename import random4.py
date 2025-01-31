import random
import string

def generate_password(length=12):
    # Define the character set: uppercase letters, digits, and special characters
    characters = string.ascii_uppercase + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Generate a random password of length 12
random_password = generate_password(12)
print(f"Generated Password: {random_password}")
