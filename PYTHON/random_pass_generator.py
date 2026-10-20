import random
import string

def generate_password(length, use_digits, use_symbols):
    # Base character set: English letters
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate exact length password randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("==========================================")
    print("      Random Password Generator App       ")
    print("==========================================")
    
    try:
        length = int(input("Enter desired password length (e.g., 8, 12, 16): "))
        
        if length <= 0:
            print("❌ Password length must be greater than 0!")
            return

        use_digits = input("Include numbers? (y/n): ").strip().lower() in ['y', 'yes']
        use_symbols = input("Include special symbols? (y/n): ").strip().lower() in ['y', 'yes']
        
        password = generate_password(length, use_digits, use_symbols)
        
        print("\n------------------------------------------")
        print(f"🔑 Generated Password : {password}")
        print(f"📏 Password Length   : {len(password)}")
        print("------------------------------------------")
        
    except ValueError:
        print("❌ Invalid input! Please enter a valid number for length.")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using Password Generator. Goodbye!")
            break
        print("\n" + "="*40 + "\n")