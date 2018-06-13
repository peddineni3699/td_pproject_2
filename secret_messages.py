# Aaron Pope
# 05/22/2018
# Treehouse TechDegree - Python, Unit 2: Secret Messages

"""Command line tool to perform encryption & decryption on supported ciphers

This script runs in a loop, allowing the user to first
select to encrypt or decrypt text, then to select the cipher to use.
Where applicable, logic has been added to account for user input
required for specific ciphers.
"""
import os
from sys import exit

import utils.utils as utils
from affine import Affine
from atbash import Atbash
from caesar import Caesar
from polybius_square import Polybius



# Create keys for easier display and parsing selections in command line
ciphers = {key: cipher for key, cipher in 
            zip(range(1, 5), [Affine(), Atbash(), Caesar(), Polybius()])}
# Constants for operation selection logic
OPERATION_ENCRYPT = "ENCRYPT"
OPERATION_DECRYPT = "DECRYPT"

def select_cipher():
    """Returns a cipher reference based on user input"""
    while(True):        
        for key, value in ciphers.items():
            print("{}) {}".format(key, value.__class__.__name__))
        
        cipher_choice = input(">>>  ")

        try:
            utils.exit_check(cipher_choice.upper())
            cipher_choice = int(cipher_choice)
            if cipher_choice not in ciphers.keys():
                utils.exit_check(cipher_choice)
                raise ValueError(
                    "Entered value does not exist in cipher list")
        except ValueError:
            utils.print_invalid_entry_message()
        else:
            break
    return ciphers[cipher_choice]

def select_encrypt_decrypt():
    """Returns the string literal of encrypt/decrypt operation selection"""
    while(True):
        print ("Which operation would you like to perform?\n"
                "E) Encrypt\n"
                "D) Decrypt")
        try:
            operation_choice = input(">>>  ").upper()
            # Check for valid input
            if operation_choice not in {"E", "D"}:
                utils.exit_check(operation_choice)
                raise ValueError('Enter "E" to encrypt or "D" to decrypt')
        except ValueError:
            utils.print_invalid_entry_message()
            continue
        else:
            return (OPERATION_ENCRYPT if operation_choice == "E" 
                                        else OPERATION_DECRYPT)

if __name__ == '__main__':        
    # Begin UI flow
    utils.clear_screen()
    print ("Welcome to the Cipher Machine!\n"
           "Follow the prompts to encrypt or decrypt messages.\n"
           "You can always enter 'Q' or 'quit' to leave the program.\n\n")

    while(True):
        selected_operation = select_encrypt_decrypt()
        print("\n{} from which cipher?".format(selected_operation))
        selected_cipher = select_cipher()

        # Affine cipher requires input of key values
        if selected_cipher == ciphers[1]:
            selected_cipher.prompt_for_variables()
            print("a: {}".format(selected_cipher.a))
            print("b: {}".format(selected_cipher.b))
        

        if selected_operation == OPERATION_ENCRYPT:
            encrypted_text = selected_cipher.encrypt(
                input("Enter text to encrypt:  ")
            )
            print("---> {}\n".format(encrypted_text))
        else:
            while (True):
                try:
                    decrypted_text = selected_cipher.decrypt(
                        input("Enter text to decrypt:  ")
                    )
                # Particularly, the Polybius Square cipher 
                #   requires a specific input.
                # This catches any error thrown 
                #   from the Polybius() class during decryption attempt
                except ValueError as e:
                    print("{}\nPlease try again.\n".format(e))
                else:
                    break
            print("---> {}\n".format(decrypted_text))
