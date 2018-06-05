import random
import string

from ciphers import Cipher

LETTERS = string.ascii_uppercase

class Affine(Cipher):
    def __init__(self, a=5, b=random.randrange(26)):
        # Breaking the single variable naming rule because these are to be used
        #   in the linear function "f(x) = ax + b % m"
        
        # a and b must be coprimes, meaning that they cannot be the same number
        #   Popping guarantees that the same number cannot be randomly chosen
        # self.a = primes.pop(random.randrange(len(primes)))
        self.a = a
        self.b = b

        # TODO: Take one of these out
        # self.letters = {number: letter for number, letter in zip(range(0, 26),string.ascii_uppercase)}
        self.coder = {letter: (self.a * LETTERS.index(letter) + self.b) % len(LETTERS) for letter in LETTERS}


    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                key = (self.a * LETTERS.index(char) + self.b) % len(LETTERS)
            except ValueError:
                output.append(char)
            else:
                print("Key = {}".format(key))
                output.append(LETTERS[key])
        return ''.join(output)


    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                key = self.mult_mod_inv() * (LETTERS.index(char) - self.b) % len(LETTERS)
            except ValueError:
                output.append(char)
            else:
                print("Key = {}".format(key))
                output.append(LETTERS[key])
        return ''.join(output)


    def mult_mod_inv(self):
        factor = 1
        mod_inv = self.a % len(LETTERS)

        while (mod_inv != 1):
            factor += 1 
            mod_inv = self.a * factor % len(LETTERS)

        return factor