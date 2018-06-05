import string

from ciphers import Cipher

# In order to have square dimensions, 5 subsets of the string library  are utilized:
#   Uppercase       26 characters
#   Lowercase       26 characters
#   Digits (0-9)    10 characters
#   Punctuation     32 characters
#   Whitespace       6 characters
#
# This allows the use of a 10x10 Polybius Square
CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + string.whitespace

class Polybius(Cipher):
    def __init__(self):
        # This cipher does not require a key
        pass

    def encrypt(self, text):
        ciphertext = []
        # Convert the text in put to uppercase
        text = text.upper()
        for char in text:
            try:
                index = CHARACTERS.index(char)
            except ValueError:
                ciphertext.append(char)
            else:
                digit1 = int(index / 10)
                digit2 = index % 10
                ciphertext.append(str(digit1) + str(digit2))
        return " ".join(ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.replace(" ", "")
        text = []
        i_range = iter(range(0, len(ciphertext)))
        for i in i_range:
            try:
                index = int(ciphertext[i]) * 10 + int(ciphertext[i+1])
            except ValueError:
                text.append(ciphertext[i])
            else:
                text.append(CHARACTERS[index])   
                # Since the ciphertext is grouped into two letters,
                #   a valid decoded character should advance the iterator by 2
                next(i_range)    
        return "".join(text)