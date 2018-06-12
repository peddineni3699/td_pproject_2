import os

from atbash import Atbash
from affine import Affine
from caesar import Caesar
from polybius_square import Polybius
from sys import exit

if __name__ == '__main__':
    # Create keys for easier display and parsing selections in command line
    ciphers = {key: cipher for key, cipher in 
        zip(range(1, 5), [Affine(), Atbash(), Caesar(), Polybius()])}
    OPERATION_ENCRYPT = "ENCRYPT"
    OPERATION_DECRYPT = "DECRYPT"
    EXIT_ARGS = {"Q", "QUIT"}


    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def exit_check(choice):
        if choice in EXIT_ARGS:
            exit()

    def print_invalid_entry_message():
        print("Invalid entry.  Please select again.\n")


    def select_cipher():
        while(True):        
            for key, value in ciphers.items():
                print("{}) {}".format(key, value.__class__.__name__))
            
            cipher_choice = input(">>>  ")

            try:
                exit_check(cipher_choice.upper())
                cipher_choice = int(cipher_choice)
                if cipher_choice not in ciphers.keys():
                    exit_check(cipher_choice)
                    raise ValueError("Entered value does not exist in cipher list")
            except ValueError:
                print_invalid_entry_message()
            else:
                break
        return ciphers[cipher_choice]

    def select_encrypt_decrypt():
        while(True):
            print ("Which operation would you like to perform?\nE) Encrypt\nD) Decrypt")
            try:
                operation_choice = input (">>>  ").upper()
                if operation_choice not in {"E", "D"}:
                    exit_check(operation_choice)
                    raise ValueError('Enter "E" to encrypt or "D" to decrypt')
            except ValueError:
                print_invalid_entry_message()
                continue
            else:
                return OPERATION_ENCRYPT if operation_choice == "E" else OPERATION_DECRYPT

    def prompt_for_affine_variables(cipher):
        while(True):
            try:
                a_input = (input("Enter a value for 'a'\n>>>  "))
                # See if a value was entered
                if a_input:
                    cipher.set_a(int(a_input))
                # Otherwise, use the current value
                else:
                    break
            except ValueError as e:
                print(e)
            else:
                break

        while(True):
            try:
                b_input = (input("Enter a value for 'b'\n>>>  "))
                # See if a value was entered
                if b_input:
                    cipher.b = int(b_input)
                # Otherwise, use the current value
                else:
                    break
            except ValueError as e:
                print("'b' must be a postiive integer")
            else:
                break
        

    # Begin UI flow
    clear_screen()
    print ("""Welcome to the Cipher Machine!
Follow the prompts to encrypt or decrypt messages.
You can always enter 'Q' or 'quit' to leave the program.\n\n""")
    while(True):
        selected_operation = select_encrypt_decrypt()
        print("\n{} from which cipher?".format(selected_operation))
        selected_cipher = select_cipher()

        if selected_cipher == ciphers[1]:
            prompt_for_affine_variables(selected_cipher)
            print(selected_cipher.a)
            print(selected_cipher.b)
        
        if selected_operation == OPERATION_ENCRYPT:
            encrypted_text = selected_cipher.encrypt(input("Enter text to encrypt:  "))
            print("---> {}\n".format(encrypted_text))
        else:
            while (True):
                try:
                    decrypted_text = selected_cipher.decrypt(input("Enter text to decrypt:  "))
                except ValueError as e:
                    print("{}\nPlease try again.\n".format(e))
                else:
                    break
            print("---> {}\n".format(decrypted_text))
