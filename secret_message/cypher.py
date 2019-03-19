alphabet= 'abcdefghijklmnopqrstuvwxyz'
key = int(input('enter number to be key '))
newMessage=""

message = input(' please enter message!!!!!!!!!!!! ')

for character in message:
    if character in alphabet:

        
        position= alphabet.find(character)
        newPosition = (position + key) %26
        newCharacter= alphabet[newPosition]
        #print(character, "is now", newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character
print(newMessage)
