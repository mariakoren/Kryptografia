from PIL import Image
import hashlib
import random

input_image = Image.open("plain.bmp")


def save(data, where="images/image.bmp", message="Done"):
    new_data = bytes(data)

    output_image = Image.new("L", input_image.size)  # Create a new grayscale image
    output_image.putdata(new_data)  # Put the pixel data into the image
    output_image.save(where)
    print(message)


block_size = 8
image_data = input_image.tobytes()
size = input_image.size

# ECB
new_data = []
keys = []
for x in range(block_size):
    # key = hashlib.md5(str(x ** 3 + x).encode("UTF-8")).digest()
    key = hashlib.md5(str(random.random() * x).encode("UTF-8")).digest()
    keys.append(key)

for x in range(size[0]):
    for y in range(size[1]):
        pp = y * size[0] + x  # pixel position
        op = image_data[pp]  # original pixel
        pta = op ^ keys[x % block_size][y % block_size]     # pixel to add
        new_data.append(pta)

new_data = new_data[:size[0]*size[1]]

save(new_data, "ecb_crypto.bmp", "zapisano ecb")


# CBC
new_key = 13
new_data = [image_data[0] ^ new_key]
for x in range(size[0]*size[1] - 1):
    new_data.append(new_data[x] ^ image_data[x + 1] ^ keys[(x + 1) % 64 // 8][(x + 1) % 8])

new_data = new_data[:size[0]*size[1]]

save(new_data, "cbc_crypto.bmp", "zapisano cbc")

print("Done")
