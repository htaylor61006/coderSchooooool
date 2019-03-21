from random import randint

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def generate_opt(sheets,length):
    for sheet in range(sheets):
        with open ("otp" +str(sheet) + ".txt", "w") as f:
            for i in range(length):
                f.write(str(randint(0,26)) + "\n")
