import os

from atbash import Atbash
from affine import Affine
from caesar import Caesar
from polybius_square import Polybius

if __name__ == '__main__':
    ciphers = {key: cipher_name for key, cipher_name in 
        zip(range(1, 5), [Affine(), Atbash(), Caesar(), Polybius()])}

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


    def select_cipher():
        while(True):        
            for key, value in ciphers.items():
                print("{}) {}".format(key, value.__class__.__name__))
            
            try:
                cipher_choice = int(input ("\nEnter a number from the options above:  "))
                if cipher_choice not in ciphers.keys():
                    raise ValueError("Please select one of the available options.")
            except ValueError:
                clear_screen()
                print ("Invalid entry.  Please select again.\n")
            else:
                break
        cipher_choice = ciphers[cipher_choice]
        print(cipher_choice.__class__.__name__)
        return cipher_choice

    def select_encrypt_decrypt():
        while(True):
            print ("Choose to encrypt or decrypt:\nE) Encrypt\nD) Decrypt")
            try:
                choice = input (">>>  ")
                if choice.upper() not in {"E", "D"}:
                    raise ValueError('Enter "E" to encrypt or "D" to decrypt')
            except ValueError:
                clear_screen()
                continue
            else:
                break

        

    # Begin UI flow
    clear_screen()
    print ("Welcome to the Cipher Machine!\n")
    print ("Let's start by selecting a cipher to use:")
    while(True):
        selected_cipher = select_cipher()
        print("You selected {}".format(selected_cipher.__class__.__name__))
        select_encrypt_decrypt()
        # TODO: Write the UI
        break
