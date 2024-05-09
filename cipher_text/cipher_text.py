import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
        cipher_text=""
        for let in text: 
           if let in alphabet:
             pos=alphabet.index(let)
             new_pos=(pos+shift)%26
             new_letter=alphabet[new_pos] 
             cipher_text+=new_letter 
           else:
               cipher_text+=let  
        return cipher_text 
def decrypt(text,shift):
        decipher_text=""
        for let in text: 
           if let in alphabet:
             pos=alphabet.index(let)
             new_pos=(pos-shift)%26
             new_letter=alphabet[new_pos] 
             decipher_text+=new_letter
           else:
               decipher_text+=let    
        return decipher_text
encrypt(text,shift)
decrypt(text,shift)       
if direction=='encode':
    encoded_text=encrypt(text,shift)
    print(f"The encoded text is {encoded_text}")   
if direction=='decode':
    decoded_text=decrypt(text,shift)
    print(f"The decoded text is {decoded_text}")
    
   

   