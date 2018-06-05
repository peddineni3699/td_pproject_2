def mult_mod_inv(inverse_target, mod):
    # A rather brute-force method of finding the multiplicative modular inverse
    factor = 1
    mod_inv = inverse_target % mod

    while (mod_inv != 1):
        factor += 1 
        mod_inv = inverse_target * factor % mod
    return factor


# TODO: Could probably use a rename/refactor, since it's now a standalone utility
def coprimes_identified(num1, num2):
    larger_number = num1 if num1 > num2 else num2

    for divisor in range(2, int(larger_number/2)):
        if num1 % divisor == 0 and num2 % divisor == 0:
            raise ValueError("{} found to be a common divisor.\n'a' and {} must be coprimes.\nPlease enter a different value for 'a'."
                .format(divisor, larger_number))
    return False