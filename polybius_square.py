import string

from ciphers import Cipher

# Utilizing letters and numbers 
CHARACTERS = string.ascii_uppercase + string.digits + string.whitespace

class Polybius(Cipher):
    def __init__(self):
        pass

    def encrypt(self, text):
        ciphertext = []
        text = text.upper()
        for char in text:
            try:
                index = CHARACTERS.index(char)
            except ValueError:
                ciphertext.append(char)
            else:
                digit1 = int(index / 6)
                digit2 = index % 6
                ciphertext.append(str(digit1) + str(digit2))
        return " ".join(ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.replace(" ", "")
        text = []
        i_range = iter(range(0, len(ciphertext)))
        for i in i_range:
            try:
                index = int(ciphertext[i]) * 6 + int(ciphertext[i+1])
            except ValueError:
                text.append(ciphertext[i])
            else:
                text.append(CHARACTERS[index])   
                # Since the ciphertext is grouped into two letters,
                #   a valid decoded character should advance the iterator by 2
                next(i_range)    
        return "".join(text)