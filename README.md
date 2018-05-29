# Secret Messages
For Treehouse TechDegree (Python), Unit 2: Secret Messages

---
General submission guidelines are provided by Treehouse and can be found here: http://treehouse-techdegree.s3.amazonaws.com/Student-Project-Submission-Checklist.pdf


# Requirements

#### Choose at least 3 basic ciphers from the following list of implement encrypting and decrypting abilities.
* [Alberti cipher](https://en.wikipedia.org/wiki/Alberti_cipher)
* [Affine cipher](https://en.wikipedia.org/wiki/Affine_cipher)
* [Atbash cipher](https://en.wikipedia.org/wiki/Atbash)
* [Polybius square cipher](https://en.wikipedia.org/wiki/Polybius_square)
* [Transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher)
* [ADFGVX cipher](https://en.wikipedia.org/wiki/ADFGVX_cipher)
* [Bifid cipher](https://en.wikipedia.org/wiki/Bifid_cipher)
* [Keyword cipher](https://en.wikipedia.org/wiki/Keyword_cipher)
* [Hill cipher](https://en.wikipedia.org/wiki/Hill_cipher)

*Note: Caesar Cipher is included as a starter file and does not count toward one of the three requirements.*

#### Provide a command line menu providing an option to either encrypt or decrypt a value.  Then, in a sub-menu, provide a list of implemented ciphers.
    E) Encrypt
    D) Decrypt
        1) [cipher 1]
        2) [cipher 2]
        3) [cipher 3]

#### Write a separate class, which inherits from `cipher` and implements encryption and decryption functionality for each of the chosen ciphers.

#### Prompt the user for input to encrypt or decrypt and, if applicable, any additional input settings required to perform the cipher process.

#### The input value is correctly encrypted or decrypted using the chosen cipher and the output is displayed on the screen.

#### Ensure that all items on the [Student Project Submission Checklist](http://treehouse-techdegree.s3.amazonaws.com/Student-Project-Submission-Checklist.pdf) are completed.

#### *General Guidelines*
* Include informative information docstrings in functions and/or methods.

* Follow [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008) for coding style, organization, and easy-to-read code.

* Provide general code comments for information and context.


## EXTRA CREDIT (1/2)
#### Implement a [one time pad](https://en.wikipedia.org/wiki/One-time_pad) to secure the cipher.
    A one time pad is an additional input step required prior to encrypting and decrypting a message.  As long as both the sender and receiver use the same pad, the message itself becomes secure.  Without the pad, the message cannot be recovered.

## EXTRA CREDIT (2/2)
#### Encrypted output is displayed in 5 character blocks, with padding added as required.
*Example:*
> "The quick brown fox" 

could be represented as 

>"LFDKA NMYML K1KZE &XPQR"
