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


    #need to compleate function


            
generate_otp(5,100)
sheet=load_sheet('otp3.txt')
msg=get_plain_text()
cypher_text=encrypt(msg,sheet)
print(cypher_text)
#plain_text= decrypt(cypher_text,sheet)
sheet_guess = input("which otp to use?: ")
current_sheet = 'otp' + sheet_guess + '.txt'
sheet = load_sheet(current_sheet)
plain_text = decrypt(cypher_text,sheet)
print(plain_text)












