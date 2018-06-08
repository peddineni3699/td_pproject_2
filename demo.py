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
        # print(cipher_choice)
        return cipher_choice

    def sample_encrypt(cipher):
        text = input("Enter some text to encrypt: ")
        print("--> {}".format(c.encrypt(text)))

    def sample_decrypt(cipher):
        text = input("Enter the above output to see it decrypted: ")
        print("--> {}\n".format(c.decrypt(text)))

    def cipher_demo(cipher):
        sample_encrypt(cipher)
        sample_decrypt(cipher)

    # Begin UI flow
    clear_screen()
    print ("Welcome to the Cipher Machine!\n")
    print ("This demo will allow for a single encryption & decryption "
            + "operation for each of the implemented ciphers.\n")
    

    print ("=== Caesar sample ===")
    c = Caesar()
    cipher_demo(c)
    
    print ("=== Affine sample ===")
    c = Affine()
    cipher_demo(c)

    print ("=== Atbash sample ===")
    c = Atbash()
    cipher_demo(c)

    print ("=== Polybius Square sample ===")
    c = Polybius()
    cipher_demo(c)
