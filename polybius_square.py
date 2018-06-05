from random import shuffle
import string

from ciphers import Cipher

# In order to have square dimensions, 5 subsets of the string library  are utilized:
#   Uppercase       26 characters
#   Lowercase       26 characters
#   Digits (0-9)    10 characters
#   Punctuation     32 characters
#   Whitespace       6 characters
#
# This allows the use of a 10x10 Polybius Square, with indexes 00 - 99
#
# Punctuation is used as the first set populated to the squared
#   in order to prevent numbers or letters from being mapped to
#   their logical numerical equivalent.



class Polybius(Cipher):
    def __init__(self):
        self.CHARACTERS = list(
            char for char in string.punctuation 
            + string.ascii_lowercase 
            + string.digits 
            + string.ascii_uppercase 
            + string.whitespace)
        shuffle(self.CHARACTERS)

    def encrypt(self, text):
        ciphertext = []
        for char in text:
            try:
                index = self.CHARACTERS.index(char)
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
            # This was added before the full character list was implemented,
            #   but it should probably stay for edge cases
            except ValueError:
                text.append(ciphertext[i])
            else:
                text.append(self.CHARACTERS[index])   
                # Since the ciphertext is grouped into two letters,
                #   a valid decoded character should advance the iterator by 2
                next(i_range)    
        return "".join(text)