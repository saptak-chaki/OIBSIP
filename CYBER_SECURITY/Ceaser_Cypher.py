def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("==========================================")
    print("      Caesar Cipher Encryption Tool       ")
    print("==========================================")
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift key (e.g., 3): "))
    
    if choice == 'E':
        result = encrypt(message, shift)
        print(f"\n🔒 Encrypted Message: {result}")
    elif choice == 'D':
        result = decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {result}")
    else:
        print("❌ Invalid choice!")
    print("==========================================")

if __name__ == "__main__":
    main()