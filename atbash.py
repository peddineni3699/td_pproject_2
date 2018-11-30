# Treehouse TechDegree - Python, Unit 2: Secret Messages

"""Encrypts & decrypts text, based on Atbash cipher encryption

This cipher is a special subset of the Affine cipher,
and it requires specific values for 'a' and 'b'
    ascii_uppercase     26 characters
    ascii_lowercase     26 characters
    digits              10 characters
    punctuation         32 characters
    whitespace          6 characters
"""
import string

from affine import Affine

class Atbash(Affine):
    """A subset of the Affine cipher, using uppercase letters only"""
    def __init__(self):
        """Initializes a new Atbash instance with default values"""
        super().__init__(b=25)
        # The Affine cipher parent performs validation upon initialization
        #   that is not relevant to the Atbash class.
        # Therefore, the values specific to the Atbash cipher are set
        #   after initialization of  the parent.
        self.characters = string.ascii_uppercase
        self.a = 25

    # Atbash is only designed to function with a single set of letters
    #   and should not be case-sensitive.
    # So I'm calling the superclass with a cast to uppercase
    def encrypt(self, text):
        """Returns a string of encrypted text
        
        text -- the text to be encrypted
        """
        return super().encrypt(text.upper())


    def decrypt(self, text):
        """Returns a string of decrypted text
        
        text -- the text to be decrypted
        """
        return super().decrypt(text.upper())
