# Autor: Maria Koren

from PIL import Image
import random

input_image = Image.open("plain.bmp")


def save(data, where="images/image.bmp", message="Done"):
    new_data = bytes(data)

    output_image = input_image.copy()
    output_image.frombytes(bytes(new_data))
    output_image.save(where)
    print(message)


block_size = 8
image_data = input_image.tobytes()
size = input_image.size

# ECB
new_data = []
keys = []
for _ in range(16): 
    # Generowanie kluczy jako losowych bajtów
    key = bytes([random.randint(0, 255) for _ in range(block_size)])
    keys.append(key)

for i in range(len(image_data)):
    op = image_data[i] 
    pta = op ^ keys[i % 16][i % 8]  
    new_data.append(pta)

assert len(new_data) == len(image_data)

save(new_data, "ecb_crypto.bmp")

# CBC
new_key = 156
iv = new_key 
new_data = [image_data[0] ^ iv]
for i in range(1, len(image_data)): 
    new_data.append(new_data[i-1] ^ image_data[i] ^ keys[i % 16][i % 8])

assert len(new_data) == len(image_data)
save(new_data, "cbc_crypto.bmp")