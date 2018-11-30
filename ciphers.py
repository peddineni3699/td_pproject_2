# Provided by Treehouse as a starter file for the project

import string

from random import shuffle


class Cipher:
    #   All derived classes require at least the set of uppercase characters
    characters = string.ascii_uppercase

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    #   NYI; will add to derived classes on re-visit
    def create_one_time_pad(self):
        # Shuffling allows each instance to have its own key
        return shuffle(self.characters)
