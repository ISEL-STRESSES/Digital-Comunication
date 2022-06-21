import random
import secrets
import string


def vernam_cipher(file):
    file = open(file, "rb")
    plain_text = file.read()
    file.close()
    key = secrets.token_bytes(len(plain_text) + secrets.randbelow(5))
    f = open("vernam_ciphered.txt", "wb")
    key_file = open("key.txt", "wb")

    key_file.write(key)
    key_file.close()
    cipher = make_vernam_cypher(plain_text, key)
    f.write(bytearray(cipher))
    f.close()
    return


def make_vernam_cypher(text, key):
    ciphered = []
    p = 0
    for n in range(len(text)):
        ciphered.append((text[n] ^ key[p]))
        p += 1
        if p == len(key):
            p = 0
    return ciphered


def decipher_vernam(text, key):
    deciphered = []
    p = 0
    for n in range(len(text)):
        deciphered.append((n ^ key[p]))
        p += 1
        if p == len(key):
            p = 0
    return deciphered


def vernam_decipher(file):
    file = open(file, "rb")
    cypher_text = file.read()
    file.close()

    file_key = open("key.txt", "rb")
    key = file_key.read()
    file_key.close()

    f = open("vernam_deciphered.txt", "wb")
    deciphered = make_vernam_cypher(cypher_text, key)
    f.write(bytearray(deciphered))
    f.close()


if __name__ == '__main__':
    vernam_cipher("test.txt")
    vernam_decipher("vernam_ciphered.txt")
