import os

from atbash import Atbash
from affine import Affine
from caesar import Caesar
from polybius_square import Polybius

if __name__ == '__main__':
    ciphers = {key: cipher_name for key, cipher_name in 
        zip(range(1, 5), [Affine(), Atbash(), Caesar(), Polybius()])}
    OPERATION_ENCRYPT = "ENCRYPT"
    OPERATION_DECRYPT = "DECRYPT"


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
                # clear_screen()
                print ("Invalid entry.  Please select again.\n")
            else:
                break
        return ciphers[cipher_choice]

    def select_encrypt_decrypt():
        while(True):
            print ("Which operation would you like to perform?\nE) Encrypt\nD) Decrypt")
            try:
                choice = input (">>>  ").upper()
                if choice not in {"E", "D"}:
                    raise ValueError('Enter "E" to encrypt or "D" to decrypt')
            except ValueError:
                # clear_screen()
                continue
            else:
                return OPERATION_ENCRYPT if choice == "E" else OPERATION_DECRYPT
        

    # Begin UI flow
    clear_screen()
    print ("Welcome to the Cipher Machine!\n")
    while(True):
        selected_operation = select_encrypt_decrypt()
        print("\n{} from which cipher?".format(selected_operation))
        selected_cipher = select_cipher()
        print(selected_cipher.description)
        print("You selected {}".format(selected_cipher.__class__.__name__))
        
        # TODO: Write the UI
        break
