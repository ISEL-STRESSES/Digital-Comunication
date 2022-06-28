from PIL import Image

test_files_path = "../CD_TestFiles/"
caesar_files_output_path = "caesar_output/"


def caesar_cipher(file):
    # get file name and extension
    file_name = file.partition('.')[0]
    get_ext = file.partition('.')[2]

    try:
        # open image
        plain_img = Image.open(test_files_path + file)

        # cipher image
        ciphered_img = make_caesar_cypher_img(plain_img)

        # save ciphered image
        ciphered_img.save(caesar_files_output_path + file_name + "_caesar_ciphered." + get_ext)
    except IOError:
        # read plain text
        plain_file = open(test_files_path + file, "rb")
        plain_text = plain_file.read()
        plain_file.close()

        # cipher text
        ciphered = make_caesar_cypher(plain_text)

        # write cipher to file
        ciphered_file = open(caesar_files_output_path + file_name + "_caesar_ciphered." + get_ext, "wb")
        ciphered_file.write(bytearray(ciphered))
        ciphered_file.close()


def make_caesar_cypher(text):
    ciphered = []
    numb = 3
    for n in range(len(text)):
        ciphered.append((text[n] + numb))
    return ciphered


def make_caesar_cypher_img(img):
    pixel_map = img.load()
    ciphered = Image.new('L', img.size)
    pixels_new = ciphered.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels_new[i, j] = (pixel_map[i, j] + 3) % 256
    return ciphered


def make_caesar_decipher(text):
    ciphered = []
    numb = 3
    for n in range(len(text)):
        ciphered.append((text[n] - numb))
    return ciphered


def make_caesar_decipher_img(img):
    pixel_map = img.load()
    im = Image.new('L', img.size)
    pixels_new = im.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels_new[i, j] = (pixel_map[i, j] - 3) % 256
    return im


def caesar_decipher(file):
    # get file name and extension
    file_name = file.partition("_caesar_ciphered")[0]
    get_ext = file.partition('.')[2]

    try:
        # open image
        img = Image.open(caesar_files_output_path + file)

        # cipher image
        im = make_caesar_decipher_img(img)

        # save ciphered image
        im.save(caesar_files_output_path + file_name + "_caesar_deciphered." + get_ext)
    except IOError:
        # read ciphered text
        deciphered_text_file = open(caesar_files_output_path + file, "rb")
        ciphered_text = deciphered_text_file.read()

        # decipher text
        deciphered = make_caesar_decipher(ciphered_text)

        # write deciphered to file
        f = open(caesar_files_output_path + file_name + "_caesar_deciphered." + get_ext, "wb")
        f.write(bytearray(deciphered))
        f.close()


def cipher_test_files():
    caesar_cipher("a.txt")
    caesar_cipher("alice29.txt")
    caesar_cipher("cp.htm")
    caesar_cipher("lena.bmp")
    caesar_cipher("Person.java")
    caesar_cipher("progc.c")


def decipher_test_files():
    caesar_decipher("a_caesar_ciphered.txt")
    caesar_decipher("alice29_caesar_ciphered.txt")
    caesar_decipher("cp_caesar_ciphered.htm")
    caesar_decipher("lena_caesar_ciphered.bmp")
    caesar_decipher("Person_caesar_ciphered.java")
    caesar_decipher("progc_caesar_ciphered.c")


if __name__ == '__main__':
    cipher_test_files()
    decipher_test_files()
