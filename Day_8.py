import  os
from Day_8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(word, n):
    encrypt_word = ""
    
    for letter in word:
        encrypt_word += alphabet[alphabet.index(letter) + n]
    print(f"Your message encripted is: {encrypt_word}")

def decrypt(word, n):
    decrypt_word = ""
    for letter in word:
        decrypt_word += alphabet[alphabet.index(letter) - n]
    print(f"Your message was: {decrypt_word}")

if __name__ == '__main__':
    program_continue = True

    while program_continue:
        os.system('clear')
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == 'encode':
            encrypt(input("Type your message:\n").lower(), shift)

        elif direction == 'decode':
            decrypt(input("Type your message:\n").lower(), shift)

        else:
            print("Out of range")

        usr_choose = input("Want to encrypt more messages? Yes or No: ").lower()
        if usr_choose == "yes":
            continue
        
        elif usr_choose == "no":
            program_continue = False