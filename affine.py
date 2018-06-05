import math_utils
import random
import string

from ciphers import Cipher
from random import shuffle

class Affine(Cipher):
    def __init__(self, a=19, b=random.randrange(100)):
        self.CHARACTERS = list(
            char for char in string.punctuation 
            + string.ascii_lowercase 
            + string.digits 
            + string.ascii_uppercase 
            + string.whitespace)

        # Shuffling allows each instance to have its own key
        shuffle(self.CHARACTERS)

        # a and m must be coprimes, 
        #   meaning that they cannot have any common factor greater than 1.
        try:
            math_utils.coprimes_identified(a, len(self.CHARACTERS))
        except ValueError as e:
            print("\n=== INITIALIZATION ERROR ===\n{}\n".format(e))

        # Breaking the single variable naming rule because these are to be used
        #   in the linear function "f(x) = ax + b % m"
        self.a = a
        self.b = b


    def encrypt(self, text):
        ciphertext = []
        # text = text.upper()
        for char in text:
            try:
                key = (self.a * self.CHARACTERS.index(char) + self.b) % len(self.CHARACTERS)
            except ValueError:
                ciphertext.append(char)
            else:
                ciphertext.append(self.CHARACTERS[key])
        return ''.join(ciphertext)


    def decrypt(self, ciphertext):
        text = []
        # ciphertext = ciphertext.upper()
        for char in ciphertext:
            try:
                key = math_utils.mult_mod_inv(self.a, len(self.CHARACTERS)) * (self.CHARACTERS.index(char) - self.b) % len(self.CHARACTERS)
            except ValueError:
                text.append(char)
            else:
                text.append(self.CHARACTERS[key])
        return ''.join(text)
