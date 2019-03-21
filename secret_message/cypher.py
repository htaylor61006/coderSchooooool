alphabet= 'abcdefghijklmnopqrstuvwxyz'


def encrypt(message,key):
    newMessage=""
    for character in message:
        if character in alphabet:

            position= alphabet.find(character)
            newPosition = (position + key) %26
            newCharacter= alphabet[newPosition]
            #print(character, "is now", newCharacter)
            newMessage += newCharacter
        else:
            newMessage += character
    return newMessage


key = int(input('enter number to be key '))

message = input(' please enter message!!!!!!!!!!!! ')


encrypted = encrypt(message,key)

print(encrypted)

decrypted = encrypt(encrypted,key * -1)
print(decrypted)
