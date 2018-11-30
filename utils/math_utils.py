# Treehouse TechDegree - Python, Unit 2: Secret Messages

def mult_mod_inv(a, mod):
    """Returns the multiplicative modular inverse of 'a' under modulo 'mod'
    
    a -- base number
    mod -- the modulus
    """
    # A rather brute-force method of finding the multiplicative modular inverse
    factor = 1
    mod_inv = a % mod

    while (mod_inv != 1):
        factor += 1 
        mod_inv = a * factor % mod
    return factor


def are_coprimes(num1, num2):
    """Returns a boolean indicating if two numbers are coprimes
    
    num1 -- the first of two numbers to be compared
    num2 -- the second of two numbers to be compared

    The order in which the arguments are passed does not matter.
    This method first identifies be larger number, before performing
    its coprime checks.
    """
    larger_number = num1 if num1 > num2 else num2

    # Start at 2, since 1 is always an acceptable common factor.
    # End at (larger_number / 2) because it is the largest
    #   possible common factor.
    for divisor in range(2, int(larger_number/2)):
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
    return False
