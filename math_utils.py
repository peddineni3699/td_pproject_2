def mult_mod_inv(inverse_target, mod):
    # A rather brute-force method of finding the multiplicative modular inverse
    factor = 1
    mod_inv = inverse_target % mod

    while (mod_inv != 1):
        factor += 1 
        mod_inv = inverse_target * factor % mod
    return factor


def are_coprimes(num1, num2):
    larger_number = num1 if num1 > num2 else num2

    for divisor in range(2, int(larger_number/2)):
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
    return False