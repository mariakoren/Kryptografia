# Autor:
# Maria Koren
import hashlib
import os

if os.path.exists("diff.txt"):
    os.remove("diff.txt")

hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384, hashlib.sha512, hashlib.blake2b]

with open('personal.txt', 'rb') as f_in1, open('diff.txt', 'a') as f_out:
    data = f_in1.read()
    for func in hash_functions:
        h = func(data).hexdigest()
        f_out.write(f"{func.__name__}:\n{h}\n\n")