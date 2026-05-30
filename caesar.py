
# text = input("Enter the text to encrypt: ")
def caesar_cipher(key, message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    
    encrypt = ""
    for letter in message:
        if letter in alphabet:
            index = (alphabet.find(letter) + key) % len(alphabet)
            encrypt += alphabet[index]
        else:
            encrypt += letter
    print("Decrypted message:", encrypt.lower())
caesar_cipher(5, "Hello, World!")
caesar_cipher(0, "Hello, World!")   