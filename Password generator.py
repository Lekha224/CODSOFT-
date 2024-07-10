
import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if len(characters) == 0:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Customizable Password Generator!")
    
    length = int(input("Enter the desired length of the password: "))
    
    if length <= 0:
        print("Password length should be greater than zero.")
        return
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print("\nGenerated Password:", password)
    except ValueError as ve:
        print(str(ve))

if __name__ == "__main__":
    main()
