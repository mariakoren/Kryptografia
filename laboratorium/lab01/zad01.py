import argparse

def main():
    parser = argparse.ArgumentParser(description='Opis twojego programu')

    parser.add_argument('-c', '--option_c', help='Cezar', action='store_true')
    parser.add_argument('-a', '--option_a', help='Alfaniczny', action='store_true')
    parser.add_argument('-e', '--option_e', help='Szyfrowanie', action='store_true')
    parser.add_argument('-d', '--option_d', help='Odszyfrowanie', action='store_true')
    parser.add_argument('-j', '--option_j', help='Kryptoanaliza z tekstem jawnym', action='store_true')
    parser.add_argument('-k', '--option_k', help='Kryptoanaliza wyłącznie w oparciu o kryptogram', action='store_true')
 
    args = parser.parse_args()
    
    if args.option_c:
        print("Cezar")
        with open('plain.txt', 'r') as file:
            data = file.read()
            print(data)

        with open('key.txt', 'r') as file:
            readkey = file.read()
            try: 
                key = int(readkey)
            except: 
                raise ValueError(f"Niepoprawna wartość klucza, klucz musi być liczbą naturalną w zakresie 1...25, podana wartość {readkey}")
  
            if key > 25 or key < 1:
                raise ValueError(f"Niepoprawna wartość klucza, klucz musi być w zakresie 1...25, podana wartość {key}")

    if args.option_a:
        print("Alfaniczny")
    if args.option_e:
        print("Szyfrowanie")
    if args.option_d:
        print("Odszyfrowanie")
    if args.option_j:
        print("Kryptoanaliza z tekstem jawnym")
    if args.option_k:
        print("Kryptoanaliza wyłącznie w oparciu o kryptogram")
    

if __name__ == "__main__":
    main()
