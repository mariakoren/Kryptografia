# Autor
# Maria Koren

import sys
import random
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def is_witness(a, n):
    return pow(a, n - 1, n) == 1

def is_probably_prime(n,):
        for i in range(1, int((n/2)+1)):
            if gcd(n, i) == 1:
                if not is_witness(i, n):
                    return False
        return True

def find_nontrivial_factor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return None

def rabin_miller_test(n, exponent=None):
    if gcd(n, 2) == 2:
        return 2
    if exponent is None:
        exponent = n - 1
    r, s = 0, exponent
    while s % 2 == 0:
        r += 1
        s //= 2
    
    a = random.randint(2, n - 2)
    x = mod_exp(a, s, n)
    if x == 1 or x == n - 1:
        return "prawdopodobnie pierwsza"
    for _ in range(r - 1):
        x = mod_exp(x, 2, n)
        if x == n - 1:
            return "prawdopodobnie pierwsza"
    return gcd(x - 1, n)

def main():
    fermat_only = '-f' in sys.argv
    input_file = 'wejscie.txt'
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return
    
    try:
        n = int(lines[0].strip())
        exponent = None
        
        if len(lines) == 2:
            exponent = int(lines[1].strip())
        elif len(lines) == 3:
            exponent = int(lines[1].strip()) * int(lines[2].strip()) - 1
    except ValueError:
        print("Invalid input format.")
        return

    if fermat_only:
        if is_probably_prime(n):
            result = "prawdopodobnie pierwsza"
        else:
            result = "na pewno złożona"
    else:
        factor = find_nontrivial_factor(n)
        if factor:
            result = str(factor)
        else:
            factor = rabin_miller_test(n, exponent)
            if factor == "prawdopodobnie pierwsza":
                result = "prawdopodobnie pierwsza"
            else:
                result = str(factor)
    
    with open('wyjscie.txt', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == "__main__":
    main()
