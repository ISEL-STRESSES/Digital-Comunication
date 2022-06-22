import random
import secrets
local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"


def vernam_cipher(file, key_file):
    # read plain text
    plain_text_file = open(local_path+file, "rb")
    plain_text = plain_text_file.read()
    plain_text_file.close()

    # generate key
    key = secrets.token_bytes(len(plain_text) + secrets.randbelow(5))

    # write key
    file_name = file.partition('.')[0]
    get_ext = key_file.partition(".")[2]
    key_file = open(key_file, "wb")
    key_file.write(key)
    key_file.close()

    # cipher text and write to file
    f = open(file_name + "_vernam_ciphered"+"."+get_ext, "wb")
    cipher = make_vernam_cypher(plain_text, key)
    f.write(bytearray(cipher))
    f.close()


def make_vernam_cypher(text, key):
    ciphered = []
    p = 0
    for n in range(len(text)):
        ciphered.append((text[n] ^ key[p]))
        p += 1
        if p == len(key):
            p = 0
    return ciphered


def vernam_decipher(file, key_file):
    # read ciphered text
    ciphered_text_file = open(file, "rb")
    cypher_text = ciphered_text_file.read()
    ciphered_text_file.close()

    # read key
    file_name = key_file.partition("_vernam_key")[0]
    get_ext = key_file.partition(".")[2]
    file_key = open(key_file, "rb")
    key = file_key.read()
    file_key.close()

    # decipher text and write to file
    f = open("vernam_deciphered_"+file_name+"."+get_ext, "wb")
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
    vernam_cipher("test.txt", "test_vernam_key.txt")
    vernam_decipher("test_vernam_ciphered.txt", "test_vernam_key.txt")
    cipher_test_files()
    decipher_test_files()
