def beaufort_cipher(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char_value = (ord(plaintext[i].upper()) - ord('A')) % 26
        key_value = (ord(key[i % len(key)].upper())-ord('A')) % 26
        encrypted_char = chr(((key_value - char_value) % 26) + ord('A'))
        ciphertext += encrypted_char

    return ciphertext

def main():
    plaintext = input("Enter the message: ")

    key = input("Enter the key: ")

    while not key.isalpha():
        print("Key must only contain letters.")
        key = input("Enter the key: ")

    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")

    if choice == 'e':
        ciphertext = beaufort_cipher(plaintext, key)
        print("Encrypted message:", ciphertext)
    elif choice == 'd':
       decryptedtext = beaufort_cipher(plaintext, key)
       print("Decrypted message:", decryptedtext)
    else:
       print("Invalid choice. Please enter 'e' or 'd'.")


if __name__ == '__main__':
    main()