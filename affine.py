import random
import string

from ciphers import Cipher

CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + string.whitespace

class Affine(Cipher):
    def __init__(self, a=5, b=random.randrange(100)):
        # Breaking the single variable naming rule because these are to be used
        #   in the linear function "f(x) = ax + b % m"
        
        # a and m must be coprimes, 
        #   meaning that they cannot have any common factor greater than 1.
        try:
            self.coprimes_identified(a)
        except ValueError as e:
            print("\n=== INITIALIZATION ERROR ===\n{}\n".format(e))
        self.a = a
        self.b = b


    def encrypt(self, text):
        ciphertext = []
        # text = text.upper()
        for char in text:
            try:
                key = (self.a * CHARACTERS.index(char) + self.b) % len(CHARACTERS)
            except ValueError:
                ciphertext.append(char)
            else:
                ciphertext.append(CHARACTERS[key])
        return ''.join(ciphertext)


    def decrypt(self, ciphertext):
        text = []
        # ciphertext = ciphertext.upper()
        for char in ciphertext:
            try:
                key = self.mult_mod_inv() * (CHARACTERS.index(char) - self.b) % len(CHARACTERS)
            except ValueError:
                text.append(char)
            else:
                text.append(CHARACTERS[key])
        return ''.join(text)


    def mult_mod_inv(self):
        # A rather brute-force method of finding the multiplicative modular inverse
        factor = 1
        mod_inv = self.a % len(CHARACTERS)

        while (mod_inv != 1):
            factor += 1 
            mod_inv = self.a * factor % len(CHARACTERS)
        return factor

    
    def coprimes_identified(self, a):
        larger_number = a if a > len(CHARACTERS) else len(CHARACTERS)

        for divisor in range(2, int(larger_number/2)):
            if a % divisor == 0 and len(CHARACTERS) % divisor == 0:
                raise ValueError("{} found to be a common divisor.\n'a' and {} must be coprimes.\nPlease enter a different value for 'a'."
                    .format(divisor, len(CHARACTERS)))
        return False