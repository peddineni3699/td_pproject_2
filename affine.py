# Treehouse TechDegree - Python, Unit 2: Secret Messages

"""Encrypts & decrypts text, based on Affine cipher encryption

This implementation supports 5 subsets of the string library:
    ascii_uppercase     26 characters
    ascii_lowercase     26 characters
    digits              10 characters
    punctuation         32 characters
    whitespace          6 characters
"""
import string

import utils.math_utils as math_utils
from ciphers import Cipher
from random import shuffle
from random import randrange

class Affine(Cipher):
    """A substitution cipher based on linear modulo shifting"""
    def __init__(self, a=23, b=50):
        """Initializes a new Affine instance with default values
        
        a: Magnitude of cipher shift (default 23)
        b: Offset of cipher shift (default 50)
        """
        self.characters = list(
            self.characters
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
            + " "
        )

        try:
            # a and m must be coprimes, 
            #   meaning that they cannot have any common factor greater than 1.
            # Storing in variable to use in error message
            coprimes_exist = math_utils.are_coprimes(a, len(self.characters))
            if coprimes_exist:            
                raise ValueError('{} found to be a common divisor.\n'
                                '"a" and {} must be coprimes.\n'
                                'Please enter a different value for "a"'
                                .format(coprimes_exist, len(self.characters)))
        except ValueError:
            print("Could not initialize Affine cipher.  "
                  "{} found to be a common divisor."
                  .format(coprimes_exist))
            print("\n'a' and {} must be coprimes.\n"
                  "Please enter a different value for 'a'."
                  .format(len(self.characters)))
            

        # Breaking the single variable naming rule because these are to be used
        #   in the linear function "f(x) = (ax + b) % m"
        self.a = a
        self.b = b


    def encrypt(self, text):
        """Returns a string of encrypted text
        
        text -- the text to be encrypted
        """
        ciphertext = []
        # text = text.upper()
        for char in text:
            try:
                key = (self.a * self.characters.index(char) + self.b) % len(self.characters)
            # If character is not in set for cipher,
            #   directly append it without transformation
            except ValueError:
                ciphertext.append(char)
            else:
                ciphertext.append(self.characters[key])
        return ''.join(ciphertext)


    def decrypt(self, ciphertext):
        """Returns a string of decrypted text
        
        text -- the text to be decrypted
        """
        text = []
        # ciphertext = ciphertext.upper()
        for char in ciphertext:
            try:
                key = math_utils.mult_mod_inv(self.a, len(self.characters)) * (self.characters.index(char) - self.b) % len(self.characters)
            # If character is not in set for cipher,
            #   directly append it without transformation
            except ValueError:
                text.append(char)
            else:
                text.append(self.characters[key])
        return ''.join(text)


    def set_a(self, number):
        """Safely sets variable 'a'
        
        number -- the number intended to be set for 'a'
        """
        try:
            coprimes_exist = math_utils.are_coprimes(number, len(self.characters))
        except ValueError:
            raise ValueError("Invalid entry for 'a'")
        else:
            if coprimes_exist:            
                raise IOError('{} found to be a common divisor.\n'
                                '"a" and {} must be coprimes.\n'
                                'Please enter a different value for "a"'
                                .format(coprimes_exist, len(self.characters)))
            else:
                self.a = number

    
    def prompt_for_variables(self):
        """Allows the user to set the 'a' and 'b' variables through command line"""
        print("\nEnter key values for 'a' and 'b'")
        print("If you want to use the default/current values, just press ENTER for each")
        while(True):
            try:
                a_input = (input("\nEnter a value for 'a'\n"
                                 "CURRENT VALUE: {}\n>>>  ".format(self.a)))
                # See if a value was entered
                if a_input:
                    self.set_a(int(a_input))
                # Otherwise, use the current value
                else:
                    break
            except ValueError:
                print("'a' must be an integer")
            except IOError as e:
                print(e)
            else:
                break

        while(True):
            try:
                b_input = (input("\nEnter a value for 'b'\n"
                                 "CURRENT VALUE: {}\n>>>  ".format(self.b)))
                # See if a value was entered
                if b_input:
                    self.b = int(b_input)
                # Otherwise, use the current value
                else:
                    break
            except ValueError:
                print("'b' must be an integer")
            else:
                break


    @property
    def description(self):
        """A brief description of the Affine cipher"""
        return ('According to Wikipedia, the Affine cipher is '
                'a "monoalphabetic substitution cipher, wherein each letter in an alphabet '
                'is mapped to its numeric equivalent, '
                'encrypted using the function [E(x)=(ax+b) mod m], '
                'and converted back to a letter."\n'
                'The characters supported by the implementation in this program include:\n'
                '-- uppercase letters: {}\n'
                '-- lowercase letters: {}\n'
                '-- digits: {}\n'
                '-- punctuation: {}\n'
                '-- blank space: " "\n'
                .format(string.ascii_uppercase,
                        string.ascii_lowercase,
                        string.digits,
                        string.punctuation)
                )
