import string

from ciphers import Cipher
from random import shuffle

# In order to have square dimensions, 5 subsets of the string library  are utilized:
#   Uppercase       26 characters
#   Lowercase       26 characters
#   Digits (0-9)    10 characters
#   Punctuation     32 characters
#   Whitespace       6 characters
#
# This allows the use of a 10x10 Polybius Square, with indexes 00 - 99

class Polybius(Cipher):
    def __init__(self):
        """Initializes a new Atbash instance with default values"""

        # This implementation supports a square of size 10 x 10
        self.characters = list(
            self.characters
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
            + string.whitespace
        )


    def encrypt(self, text):
        """Returns a string of encrypted text"""
        ciphertext = []
        for char in text:
            try:
                index = self.characters.index(char)
            # If character is not in set for cipher,
            #   directly append it without transformation
            except ValueError:
                ciphertext.append(char)
            else:
                digit1 = int(index / 10)
                digit2 = index % 10
                ciphertext.append(str(digit1) + str(digit2))
        return " ".join(ciphertext)


    def decrypt(self, ciphertext):
        """Returns a string of decrypted text"""

        # Remove whitespace from input text.
        #   Allowing whitespace in the entry makes
        #   it easer for useres to be able to parse
        #   potentially long strings of numbers.
        ciphertext = ciphertext.replace(" ", "")
        # Check to ensure that only numbers have been passed,
        try:
            # Polybius Square only takes numbers.
            #   If any other characters are found, raise an error
            int(ciphertext)
        except ValueError:
            raise ValueError("Invalid input.  "
                             "Polybius Square decryption takes only numbers and spaces.")
        # Check to ensure that the cast integer is positive
        if int(ciphertext) < 0:
            raise ValueError("Numeric input cannot be negative.")
        # Check to ensure that an even number of digits have been passed,
        #   because decryption happens in pairs
        if len(ciphertext) % 2 == 1:
            raise ValueError("Could not parse input.  "
                             "Expected an even number of digits, but received an odd number.")
        text = []
        # At this point, the input has been sanitized and can be safely decrypted.
        i_range = iter(range(0, len(ciphertext)))
        for i in i_range:
            try:
                index = int(ciphertext[i]) * 10 + int(ciphertext[i+1])
            # This was added before the full character list was implemented,
            #   but it should probably stay for edge cases
            except ValueError:
                text.append(ciphertext[i])
            else:
                text.append(self.characters[index])   
                # Since the ciphertext is grouped into two letters,
                #   a valid decoded character should advance the iterator by 2
                next(i_range)    
        return "".join(text)