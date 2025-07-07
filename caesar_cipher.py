import caesar_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    
    if direction=="encode":
        new_text=""
        for letter in text:
            if letter in alphabet:
                index=alphabet.index(letter)
                index=(index+shift)%26
                new_text +=alphabet[index]
        return new_text

    if direction=="decode":
        new_text=""
        for letter in text:
            if letter in alphabet:
                index=alphabet.index(letter)
                index=(index-shift)%26
                new_text +=alphabet[index]     
        return new_text

countinue=True
while countinue:
    print(caesar_cipher_art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    result=caesar(direction,text,shift)
    print(f"You {direction}d message is {result}.")  
    result=input("Type 'Yes' if you want to continue, otherwise type 'No'.").lower
    if result=="no":
        countinue=False
        print("Good Bye!")     