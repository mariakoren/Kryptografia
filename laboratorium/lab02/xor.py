# Autor: Maria Koren

import os
import argparse

def generate_key():
    key = []
    for _ in range(64):
        random = chr(os.urandom(1)[0] % 26 + 97)
        key.append(random)

    try:
        with open("key.txt", "w") as file:
            file.write("".join(key))
            print("Zapisano klucz")
    except Exception as e:
        print(e)

    return key[0]


def preparing_text():
    try:
        with open("orig.txt", "r") as file:
            data = file.read().strip().replace("\n", " ").lower()

        if os.path.exists("plain.txt"):
            os.remove("plain.txt")

        with open("plain.txt", "w") as plain:
            line = ""
            for char in data:
                if char.isalpha() or char == " ":
                    line += char
                    if len(line) == 64:
                        plain.write(line + "\n")
                        line = ""
            if len(line) != 0:
                plain.write(line + "a" * (64 - len(line)))
        print("Zapisano do pliku plain.txt")
    except Exception as e:
        print(e)


def encryption():
    text = []
    key = []
    encrypted = []

    try:
        with open("plain.txt", "r") as file:
            data = file.read().splitlines()
        text.extend(data)
        with open("key.txt", "r") as file:
            k = file.read()
        if len(k) == 64:
            key.append(k)
        else:
            key.append(generate_key())
    except Exception as e:
        print(e)

    for i in range(len(text)):
        tmp = []
        for j in range(len(key[0])):
            tmp.append(format(ord(text[i][j]) ^ ord(key[0][j]), '08b'))
        encrypted.append(''.join(tmp))

    try:
        if os.path.exists("crypto.txt"):
            os.remove("crypto.txt")
        with open("crypto.txt", "a") as file:
            for i in range(len(encrypted)):
                file.write(encrypted[i])
                if i + 1 != len(encrypted):
                    file.write("\n")
        print("Zapisano do pliku crypto.txt")
    except Exception as e:
        print(e)


def cryptoanalysis():
    key = ["" for _ in range(64)]
    decrypted = []
    try:
        with open("crypto.txt", "r") as file:
            segments = [
                [line[i: i + 8] for i in range(0, len(line), 8)]
                for line in file.read().strip().split("\n")
            ]
    except Exception as e:
        print(e)

    for i in range(len(segments)):
        for j in range(len(segments[i])):
            if (
                    segments[i][j][0] == "0"
                    and segments[i][j][1] == "1"
                    and segments[i][j][2] == "0"
            ):
                key[j] = chr(int(segments[i][j], 2) ^ 32)

    for i in range(len(segments)):
        for j in range(len(segments[i])):
            try:
                decrypted_char = chr(int(segments[i][j], 2) ^ ord(key[j]))
                decrypted.append(decrypted_char)
            except:
                decrypted.append("_")

    try:
        with open("decrypt.txt", "w") as file:
            file.write("".join(decrypted))
        print("Zapisano do pliku decrypt.txt")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Błędne powtórzenie klucza jednorazowego")
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('-p', action='store_true', help='(przygotowanie tekstu do przykladu dzialania')
    group1.add_argument('-e', action='store_true', help='szyfrowanie')
    group1.add_argument('-k', action='store_true', help='kryptoanaliza wyłącznie w oparciu o kryptogram')
    args = parser.parse_args()

    if args.p:
        print("Opcja -p")
        preparing_text()
    elif args.e:
        print("Opcja -e")
        encryption()
    elif args.k:
        print("Opcja -k")
        cryptoanalysis()
    else:
        print("Wybrano niepoprawną flagę")
