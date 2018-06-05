import string

from ciphers import Cipher

# Utilizing letters and numbers 
CHARACTERS = string.ascii_uppercase + string.digits

class Polybius(Cipher):
    def __init__(self):
        pass

    def encrypt(self, text):
        coded_text = []
        for char in text:
            try:
                CHARACTERS.index(char)
            except ValueError:
                coded_text.append(char)

    def decrypt(self, code):
        pass