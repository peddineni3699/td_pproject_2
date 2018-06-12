# Aaron Pope
# 05/22/2018
# Treehouse TechDegree - Python, Unit 2: Secret Messages

def mult_mod_inv(a, mod):
    """Returns the multiplicative modular inverse of 'a' under modulo 'mod'"""
    # A rather brute-force method of finding the multiplicative modular inverse
    factor = 1
    mod_inv = a % mod

    while (mod_inv != 1):
        factor += 1 
        mod_inv = a * factor % mod
    return factor


def are_coprimes(num1, num2):
    """Returns a boolean indicating if two numbers are coprimes"""
    larger_number = num1 if num1 > num2 else num2

    for divisor in range(2, int(larger_number/2)):
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
    return False
