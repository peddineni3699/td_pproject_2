import string

from affine import Affine

class Atbash(Affine):
    def __init__(self):
        super().__init__(b=25)
        self.characters = string.ascii_uppercase
        self.a = 25

    # Atbash is only designed to function with a single set of letters
    #   and should not be case-sensitive.
    # So I'm calling the superclass with a cast to uppercase
    def encrypt(self, text):
        return super().encrypt(text.upper())


    def decrypt(self, text):
        return super().decrypt(text.upper())
