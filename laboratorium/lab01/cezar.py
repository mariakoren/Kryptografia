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

def cezar_j(data, extra):
    data = data.replace('\n', ' ')
    extra = extra.replace('\n', ' ')
    extra = extra.split(" ")
    keys = []
    extra_index = 0
    for index_word, word in enumerate(data.split()):
        min_len = min(len(data.split()), len(extra))
        if index_word >= min_len:
            break
        key_word = extra[index_word]
        for index_character, character in enumerate(word):
            if ord(character) in range(65, 91) or ord(character) in range(97, 123):
                key = (ord(character) - ord(key_word[index_character % len(key_word)])) % 26
                keys.append(key)
                extra_index = (extra_index + 1) % len(extra) 
    unique = set(keys)
    if len(unique) == 1:
        key = unique.pop()
        decrypt = cezar_d(key, data)
        with open("plain.txt", "w") as file:
            file.write(decrypt)
        return key
    else:
        return "Can't find a key"



def cezar_k(data):
    message = ""
    for key in range(1, 26):
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
            message += chr(litera)
        message += "\n"
    return message



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

def alfaniczny_j(data, extra):
    if len(extra) < len(data):
        data_copy = data[:len(extra)]

    for a in range(1, 26):
        for b in range(26):
            zaszyfrowany = alfaniczny(a, b, extra)
            if zaszyfrowany == data_copy:
                key = f"{a} {b}"
                decrypt = alfaniczny_d(a, b, data)
                with open("plain.txt", "w") as file:
                    file.write(decrypt)
                return key
    
    return "Can't find a key"




def alfaniczny_k(data):
    message = ""
    data = data.replace('\n', ' ')
    for key_b in range(1, 27):
        for key_a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            for character in data:
                a = ord(character)
                if a in range(65, 91):
                    a = (a - key_b) * key_a
                    while a > 90:
                        a = a - 26
                if a in range(97, 123):
                    a = (a - key_b) * key_a
                    while a > 122:
                        a = a - 26
                message += chr(a)
            message += "\n"
    return message

def main():
    parser = argparse.ArgumentParser(description='Szyfr Cezarego oraz Alfaniczny')
    parser.add_argument('-c', '--option_c', help='Cezar', action='store_true')
    parser.add_argument('-a', '--option_a', help='Alfaniczny', action='store_true')
    parser.add_argument('-e', '--option_e', help='Szyfrowanie', action='store_true')
    parser.add_argument('-d', '--option_d', help='Odszyfrowanie', action='store_true')
    parser.add_argument('-j', '--option_j', help='Kryptoanaliza z tekstem jawnym', action='store_true')
    parser.add_argument('-k', '--option_k', help='Kryptoanaliza wyłącznie w oparciu o kryptogram', action='store_true')
 
    args = parser.parse_args()
    
    if args.option_c and args.option_e:
        try: 
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
        except ValueError as e:
            raise ValueError(str(e))

    

    elif args.option_c and args.option_d:
        try:
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
        except ValueError as e:
            raise ValueError(str(e))
        
    elif args.option_c and args.option_j:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        with open('extra.txt', 'r') as file:
            extra = file.read()
        key_new = cezar_j(data, extra)
        with open("key-new.txt", "w") as file:
            file.write(str(key_new))


    elif args.option_c and args.option_k:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        message = cezar_k(data)
        with open("plain.txt", "w") as file:
            file.write(str(message))


    elif args.option_a and args.option_e:
        try:
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
        except ValueError as e:
            raise ValueError(str(e))


    elif args.option_a and args.option_d:
        try:
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
        except ValueError as e:
            raise ValueError(str(e))
        
    elif args.option_a and args.option_j:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        with open('extra.txt', 'r') as file:
            extra = file.read()
        key_new = alfaniczny_j(data, extra)
        with open("key-new.txt", "w") as file:
            file.write(str(key_new))


    elif args.option_a and args.option_k:
        with open('crypto.txt', 'r') as file:
            data = file.read()
        message = alfaniczny_k(data)
        with open("plain.txt", "w") as file:
            file.write(str(message))

    else:
        print("niepoprawne opcje")

    

if __name__ == "__main__":
    main()
