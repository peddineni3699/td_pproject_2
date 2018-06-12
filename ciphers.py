# Provided by Treehouse as a starter file for the project
#   Modified by Aaron Pope

import string

from random import shuffle


class Cipher:
    # Modified: Aaron Pope
    #   All derived classes require at least the set of uppercase characters
    characters = string.ascii_uppercase

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    # Modified: Aaron Pope
    #   NYI; will add to derived classes on re-visit
    def create_one_time_pad(self):
        # Shuffling allows each instance to have its own key
        return shuffle(self.characters)

