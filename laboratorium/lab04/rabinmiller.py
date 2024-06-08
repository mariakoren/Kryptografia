# Autor
# Maria Koren

import sys
import random
import math

def read_input():
    f2 = open("wejscie.txt", "r")
    i = 0
    exponent = 0
    n = 0
    for line in f2.readlines():
        if i == 0:
            n = line
        elif i == 1:
            exponent = line
        elif i == 2:
            exponent = (int(exponent) * int(line))-1
        i += 1
    f2.close()
    return int(n), int(exponent)

def write_result(result):
    f = open('wyjscie.txt', 'w', encoding='utf-8')
    f.write(result)
    f.close()

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

def fermat(n):
    for j in range(21):
        i = random.randint(2, n-2)
        gcd_ = gcd(n, i)
        if gcd_ == 1 and pow(i, n-1, n) != 1:
            return False
    return True


def rabin_miller(n, exponent):
    for j in range(21):
        i = random.randint(2, n - 1)
        if gcd(n, i) != 1:
            print("Znaleziono liczbe z rozkladu!")
            return str(gcd(n, i))

        m = n - 1
        if exponent != 0:
            m = exponent
        k = 0
        while m % 2 == 0:
            m = m // 2
            k += 1
        b = pow(i, m, n)
        list = [b]
        while k > 1:
            b = pow(b, 2, n)
            list.append(b)
            k -= 1
        if list[0] == 1 or list[0] == n - 1:
            continue
        if list[-1] != 1 and list[-1]!=n-1:
            print(list[-1])
            return "na pewno złożona"
        for i in range(1, len(list)):
            if list[i] == 1:
                if list[i-1] != n-1:
                    print("Znaleziono liczbe z rozkladu!")
                    return str(gcd(list[i-1]-1, n))
                else:
                    break
    return "prawdopodobnie pierwsza"


def main():
    fermat_only = False
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "-f":
                print("Test Fermata")
                fermat_only = True
            case default:
                print("Niepoprawny argument")
                exit()
    
    n, exponent = read_input()
    if n == 0:
        print("Nie podales w pliku zadnych danych")
    
    if fermat_only:
        if fermat(n):
            write_result("prawdopodobnie pierwsza")
        else:
            write_result("na pewno złożona")
    else:
        print("Algorytm Rabina-Millera")
        wynik = rabin_miller(n, exponent)
        write_result(wynik)
        

if __name__ == "__main__":
    main()
