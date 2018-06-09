# Provided by Treehouse as a starter file for the project
#   Modified by Aaron Pope

import string

from random import shuffle


class Cipher:
    characters = string.ascii_uppercase
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def description(self):
        raise NotImplementedError()

    def create_one_time_pad(self):
        # Shuffling allows each instance to have its own key
        return shuffle(self.characters)

