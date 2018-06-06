import os

from atbash import Atbash
from affine import Affine
from caesar import Caesar
from polybius_square import Polybius

if __name__ == '__main__':
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


    ciphers = {key: cipher_name for key, cipher_name in zip(range(1, 5), ["Affine", "Atbash", "Caesar", "Polybius Square"])}
    print ("Welcome to the Cipher Machine\n")
    print ("Let's start by selecting a cipher to use:")
    for key, value in ciphers.items():
        print("{}) {}".format(key, value))
    cipher_choice = input ("SELECTION:  ")

    try:
        int(cipher_choice)
    except ValueError:
        # TODO: Implement this
        print("BZZT!")
    
    while(True):
        print ("The project has started!")
        
        # TODO: Write the UI
        break
