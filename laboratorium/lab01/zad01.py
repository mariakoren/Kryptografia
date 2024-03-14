import argparse

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a


def cezar(key, data):
    szyfrogram = ""
    for i in data:
        litera = ord(i)
        if litera in range(65, 91):
            litera += key
            if litera > 90:
                litera = litera - 26
        if litera in range(97, 123):
            litera += key
            if litera > 122:
                litera = litera - 26
        szyfrogram += chr(litera)
    return szyfrogram


def cezar_d(key, data):
    szyfrogram = ""
    for i in data:
        litera = ord(i)
        if litera in range(65, 91):
            litera -= key
            if litera < 65:
                litera = litera + 26
        if litera in range(97, 123):
            litera -= key
            if litera < 97:
                litera = litera + 26
        szyfrogram += chr(litera)
    return szyfrogram


def find_prime(x):
    counter = 0
    while counter * x % 26 != 1:
        counter += 1
    return counter


def alfaniczny(a, b, data):
    szyfrogram = ""
    for i in data:
        litera = ord(i)
        if litera in range(65, 91):
            litera = litera * a + b
            while litera > 90:
                litera = litera - 26
        if litera in range(97, 123):
            litera = litera * a + b
            while litera > 122:
                litera = litera - 26
        szyfrogram += chr(litera)
    return szyfrogram


def alfaniczny_d(a, b, data):
    szyfrogram = ""
    aprim=find_prime(a)
    for character in data:
        litera = ord(character)
        if litera in range(65, 91):
            litera = aprim*(litera - b) 
            while litera > 90:
                litera = litera - 26
        if litera in range(97, 123):
            litera = aprim * (litera - b)
            while litera > 122:
                litera = litera - 26
        szyfrogram += chr(litera)
    return szyfrogram

def main():
    parser = argparse.ArgumentParser(description='Opis twojego programu')
    parser.add_argument('-c', '--option_c', help='Cezar', action='store_true')
    parser.add_argument('-a', '--option_a', help='Alfaniczny', action='store_true')
    parser.add_argument('-e', '--option_e', help='Szyfrowanie', action='store_true')
    parser.add_argument('-d', '--option_d', help='Odszyfrowanie', action='store_true')
    parser.add_argument('-j', '--option_j', help='Kryptoanaliza z tekstem jawnym', action='store_true')
    parser.add_argument('-k', '--option_k', help='Kryptoanaliza wyłącznie w oparciu o kryptogram', action='store_true')
 
    args = parser.parse_args()
    
    if args.option_c and args.option_e:
        with open('plain.txt', 'r') as file:
            data = file.read()
        with open('key.txt', 'r') as file:
            readkey = file.read()
       
        key = int(readkey)
        if not 1 <= key <= 25:
            raise ValueError(f"Niewłaściwa wartość klucza, klucz musi być liczbą naturalną w zakresie 1...25, podana wartość: {readkey}")
        szyfrogram = cezar(key, data)
        with open("crypto.txt", "w") as file:
            file.write(szyfrogram)

    

    if args.option_c and args.option_d:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        with open('key.txt', 'r') as file:
            readkey = file.read()

        key = int(readkey)
        if not 1 <= key <= 25:
            raise ValueError(f"Niewłaściwa wartość klucza, klucz musi być liczbą naturalną w zakresie 1...25, podana wartość: {readkey}")
        decrypt = cezar_d(key, data)
        with open("plain.txt", "w") as file:
            file.write(decrypt)
        

    if args.option_a and args.option_e:
        with open('plain.txt', 'r') as file:
            data = file.read()
        with open('key.txt', 'r') as file:
            key = file.read().split()
        
        a = int(key[0])
        b = int(key[1])
        nwd_value = nwd(a, 26)
        if nwd_value != 1:
            raise ValueError(f"Niepoprawna wartość klucza, klucz musi być parą liczb naturalnych takich, że NWD(a,26)=1, nwd {nwd_value}")
        szyfrogram = alfaniczny(a, b, data)
        with open("crypto.txt", "a") as file:
            file.write(szyfrogram)
        print(f"zaszyfrowany tekst to {szyfrogram}")

    if args.option_a and args.option_d:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        with open('key.txt', 'r') as file:
            key = file.read().split()
        
        a = int(key[0])
        b = int(key[1])
        nwd_value = nwd(a, 26)
        if nwd_value != 1:
            raise ValueError(f"Niepoprawna wartość klucza, klucz musi być parą liczb naturalnych takich, że NWD(a,26)=1, nwd {nwd_value}")
        decrypt = alfaniczny_d(a, b, data)
        with open("plain.txt", "a") as file:
            file.write(decrypt)


    if args.option_j:
        print("Kryptoanaliza z tekstem jawnym")
    if args.option_k:
        print("Kryptoanaliza wyłącznie w oparciu o kryptogram")
    

if __name__ == "__main__":
    main()
