import random
import string

from ciphers import Cipher


primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

class Affine(Cipher):
    def __init__(self):
        # Breaking the single variable naming rule because these are to be used
        #   in the linear function "f(x) = ax + b % m"
        
        # a and b must be coprimes, meaning that they cannot be the same number
        #   Popping guarantees that the same number cannot be randomly chosen
        self.a = primes.pop(random.randrange(len(primes)))
        self.b = random.choice(primes)

        self.letters = {letter: number for letter, number in zip(string.ascii_uppercase, range(0, 26))}