import secrets
from PIL import Image
test_files_path = "../CD_TestFiles/"
vernam_files_output_path = "vernam_output/"


def vernam_cipher(file, key_file):
    # get file name and extension
    file_name = file.partition('.')[0]
    get_ext = file.partition('.')[2]

    key_extra_dim = secrets.randbelow(256)

    try:
        # open image
        plain_img = Image.open(test_files_path + file)

        # generate key
        width, height = plain_img.size
        key = secrets.token_bytes(width*height + key_extra_dim)

        # cipher image
        ciphered_img = make_vernam_cypher_img(plain_img, key)

        # save ciphered image
        ciphered_img.save(vernam_files_output_path + file_name + "_vernam_ciphered." + get_ext)
    except IOError:
        # read plain text
        plain_text_file = open(test_files_path + file, "rb")
        plain_text = plain_text_file.read()
        plain_text_file.close()

        # generate key
        key = secrets.token_bytes(len(plain_text) + key_extra_dim)

        # cipher text and write to file
        f = open(vernam_files_output_path + file_name + "_vernam_ciphered"+"."+get_ext, "wb")
        cipher = make_vernam_cypher(plain_text, key)
        f.write(bytearray(cipher))
        f.close()

    # write key to file
    key_file = open(vernam_files_output_path + key_file, "wb")
    key_file.write(key)
    key_file.close()


def make_vernam_cypher(text, key):
    ciphered = []
    p = 0
    for n in range(len(text)):
        ciphered.append((text[n] ^ key[p]))
        p += 1
        if p == len(key):
            p = 0
    return ciphered


def make_vernam_cypher_img(img, key):   # ciphers and deciphers image
    pixel_map = img.load()
    ciphered = Image.new('L', img.size)
    pixels_new = ciphered.load()
    p = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels_new[i, j] = (pixel_map[i, j] ^ key[p]) % 256
            p += 1
            if p == len(key):
                p = 0
    return ciphered


def vernam_decipher(file, key_file):
    # get file name and extension
    file_name = key_file.partition(vernam_files_output_path + "_vernam_key")[0]
    get_ext = file.partition('.')[2]

    # read key
    file_key = open(vernam_files_output_path + key_file, "rb")
    key = file_key.read()
    file_key.close()

    try:
        # open image
        img = Image.open(vernam_files_output_path + file)

        # cipher image
        im = make_vernam_cypher_img(img, key)

        # save ciphered image
        im.save(vernam_files_output_path + file_name + "_vernam_deciphered." + get_ext)
    except IOError:
        # read ciphered text
        ciphered_text_file = open(vernam_files_output_path + file, "rb")
        cypher_text = ciphered_text_file.read()
        ciphered_text_file.close()

        # decipher text and write to file
        f = open(vernam_files_output_path + file_name + "_vernam_deciphered."+get_ext, "wb")
        deciphered = make_vernam_cypher(cypher_text, key)
        f.write(bytearray(deciphered))
        f.close()


def cipher_test_files():
    vernam_cipher("a.txt", "a_vernam_key.txt")
    vernam_cipher("alice29.txt", "alice29_vernam_key.txt")
    vernam_cipher("cp.htm", "cp_vernam_key.htm")
    vernam_cipher("lena.bmp", "lena_vernam_key.bmp")
    vernam_cipher("Person.java", "Person_vernam_key.java")
    vernam_cipher("progc.c", "progc_vernam_key.c")


def decipher_test_files():
    vernam_decipher("a_vernam_ciphered.txt", "a_vernam_key.txt")
    vernam_decipher("alice29_vernam_ciphered.txt", "alice29_vernam_key.txt")
    vernam_decipher("cp_vernam_ciphered.htm", "cp_vernam_key.htm")
    vernam_decipher("lena_vernam_ciphered.bmp", "lena_vernam_key.bmp")
    vernam_decipher("Person_vernam_ciphered.java", "Person_vernam_key.java")
    vernam_decipher("progc_vernam_ciphered.c", "progc_vernam_key.c")


if __name__ == '__main__':
    cipher_test_files()
    decipher_test_files()
