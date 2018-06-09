# Aaron Pope
# 05/22/2018
# Treehouse TechDegree - Python, Unit 2: Secret Messages

import math_utils
import string

from ciphers import Cipher
from random import shuffle
from random import randrange

class Affine(Cipher):
    def __init__(self, a=23, b=50):
        self.characters = list(
            self.characters
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
            + " "
        )

        # a and m must be coprimes, 
        #   meaning that they cannot have any common factor greater than 1.
        coprimes_exist = math_utils.are_coprimes(a, len(self.characters))

        try:
            if coprimes_exist:            
                raise ValueError('{} found to be a common divisor.\n'
                                '"a" and {} must be coprimes.\n'
                                'Please enter a different value for "a"'.format(coprimes_exist, len(self.characters)))
        except ValueError:
            print("Could not initialize Affine cipher.  {} found to be a common divisor.".format(coprimes_exist))
            print("\n'a' and {} must be coprimes.\nPlease enter a different value for 'a'.".format(len(self.characters)))
            

        # Breaking the single variable naming rule because these are to be used
        #   in the linear function "f(x) = ax + b % m"
        self.a = a
        self.b = b


    def encrypt(self, text):
        ciphertext = []
        # text = text.upper()
        for char in text:
            try:
                key = (self.a * self.characters.index(char) + self.b) % len(self.characters)
            except ValueError:
                ciphertext.append(char)
            else:
                ciphertext.append(self.characters[key])
        return ''.join(ciphertext)


    def decrypt(self, ciphertext):
        text = []
        # ciphertext = ciphertext.upper()
        for char in ciphertext:
            try:
                key = math_utils.mult_mod_inv(self.a, len(self.characters)) * (self.characters.index(char) - self.b) % len(self.characters)
            except ValueError:
                text.append(char)
            else:
                text.append(self.characters[key])
        return ''.join(text)


    @property
    def description(self):
        description = ('According to Wikipedia, the Affine cipher is '
                       'a "monoalphabetic substitution cipher, wherein each letter in an alphabet '
                       'is mapped to its numeric equivalent, encrypted using the function [E(x)=(ax+b) mod m], '
                       'and converted back to a letter."'
                      )
        return description