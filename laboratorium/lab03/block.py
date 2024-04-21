# Autor: Maria Koren

from PIL import Image

def save(data, where, message="Done"):
    new_data = bytes(data)
    output_image = Image.new("L", input_image.size)
    output_image.putdata(new_data)
    output_image.save(where)
    print(message)

def encrypt_image(input_image, key, mode):
    image_data = input_image.tobytes()
    size = input_image.size
    new_data = []
    if mode == "ECB":
        for x in range(size[0]):
            for y in range(size[1]):
                pp = y * size[0] + x 
                op = image_data[pp]
                pta = op ^ key
                new_data.append(pta)
    elif mode == "CBC":
        new_data = [image_data[0] ^ key]
        for x in range(size[0]*size[1] - 1):
            new_data.append(new_data[x] ^ image_data[x + 1] ^ key)

    new_data = new_data[:size[0]*size[1]]
    return new_data

input_image = Image.open("plain.bmp")
key = "klucz"
key_bytes = key.encode("UTF-8")
ecb_encrypted_data = encrypt_image(input_image, key_bytes[0], "ECB")
save(ecb_encrypted_data, "ecb_crypto.bmp", "zapisano ecb")
cbc_encrypted_data = encrypt_image(input_image, key_bytes[0], "CBC")
save(cbc_encrypted_data, "cbc_crypto.bmp", "zapisano cbc")
print("Done")
