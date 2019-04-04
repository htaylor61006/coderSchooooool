from random import randint

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def generate_otp(sheets,length):
    for sheet in range(sheets):
        with open ("otp" +str(sheet) + ".txt", "w") as f:
            for i in range(length):
                f.write(str(randint(0,26)) + "\n")



def load_sheet(filename):
    with open (filename, "r") as f:
        contents = f.read().splitlines()

    return contents

def get_plain_text():
    plain_text = input(" type your message ")
    return plain_text.lower()


def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename,data):
    with open(filename, "w") as f:
        f.write(data)

        
def encrypt(plaintext,sheet):
    cipher_text = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            cipher_text += character

        else:
            encrypted = (ALPHABET.index(character) +int(sheet[position])) %26
            cipher_text += ALPHABET[encrypted]

    return cipher_text

def decrypt(cipherText,sheet):
    plain_text=''
    for position,character in enumerate(cipherText):
        if character not in ALPHABET:
            plain_text+= character
        else:
            decrypted= (ALPHABET.index(character) - int(sheet[position])) % 26
            plain_text+= ALPHABET[decrypted]

    return plain_text 
            

def menu():
    choices=['1','2','3','4']
    choice=(0)
    while True:
        while choice not in choices:
            print('What would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. Quit the program')
            choice = input('Please type 1,2,3 or 4 and press Enter ')
        if choice== '1':
            sheets= int(input('How many one time pads would you like to generate? '))
            length= int(input('What will be your maximum message lenght? '))
            generate_otp(sheets, length)

        elif choice=='2':
            filename= input('Type the filename of the otp you want to use. ')
            sheet= load_sheet(filename)
            plaintext= get_plain_text()
            ciphertext= encrypt(plaintext,sheet)
            filename= input('What will be the name of your encrypted file? ')
            save_file(filename,ciphertext)
        
            

        break

            



menu()
































