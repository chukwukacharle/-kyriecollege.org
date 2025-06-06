def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
