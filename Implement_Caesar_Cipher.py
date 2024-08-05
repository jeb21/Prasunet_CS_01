# IMPLEMENT_CAESAR_CIPHER
# TASK-1

def caesar_encrypt(text, shift):
    encryp_txt = ""
    for char in text:
        if char.isalpha():
            shift_value = ord('A') if char.isupper() else ord('a')
            encrypt_char = chr((ord(char) - shift_value + shift) % 26 + shift_value)
            encryp_txt += encrypt_char
        else:
            encryp_txt += char
    return encryp_txt

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        print(" ")
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (Q to quit): ").upper()
        if choice == 'Q':
            break
        elif choice in ['E', 'D']:
            print(" ")
            message = input("Enter your message: ")
            print(" ")
            shift = int(input("Enter the shift value (0-25): "))
            print(" ")
            if choice == 'E':
                encrypted_message = caesar_encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
                print(" ")
            else:
                decrypted_message = caesar_decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
                print(" ")
        else:
            print("Invalid choice. Please choose E, D, or Q.")
            print(" ")

if __name__ == "__main__":
    main()