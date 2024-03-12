import argparse
def cezar(key, data):
    szyfrogram = ""
    for i in data: 
        litera = key + ord(i)
        if litera > ord('z'):
            litera -= 26
        elif litera < ord('a'): 
            litera += 26
        szyfrogram += chr(litera)
    return szyfrogram

def cezar_d(key, data):
    szyfrogram = ""
    for i in data: 
        litera = ord(i) - key
        if litera > ord('z'):
            litera -= 26
        elif litera < ord('a'): 
            litera += 26
        szyfrogram += chr(litera)
    return szyfrogram





def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a


def alfaniczny(a, b, data):
    szyfrogram = ""
    for i in data:
        litera = (a*ord(i)+b)%26+97
        # if litera > ord('z'):
        #     litera -= 26
        # elif litera < ord('a'): 
        #     litera += 26
        szyfrogram += chr(litera)
    return szyfrogram


def alfaniczny_d(a, b, data):
    szyfrogram = ""

    for i in range(1, 26):
            if (a * i) % 26 == 1:
                aprim = i

    print(aprim)

    for i in data:
        litera = (aprim*(ord(i)-b))%26+97
        # if litera > ord('z'):
        #     litera -= 26
        # elif litera < ord('a'): 
        #     litera += 26
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
            try: 
                key = int(readkey)
                szyfrogram = cezar(key, data)
                with open("crypto.txt", "w") as file:
                    file.write(szyfrogram)
            except: 
                raise ValueError(f"Niepoprawna wartość klucza, klucz musi być liczbą naturalną w zakresie 1...25, podana wartość {readkey}")

    if args.option_c and args.option_d:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        with open('key.txt', 'r') as file:
            readkey = file.read()
            try: 
                key = int(readkey)
                decrypt = cezar_d(key, data)
                with open("plain.txt", "w") as file:
                    file.write(decrypt)
            except: 
                raise ValueError(f"Niepoprawna wartość klucza, klucz musi być liczbą naturalną w zakresie 1...25, podana wartość {readkey}")


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
