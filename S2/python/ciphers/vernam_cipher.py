import random
import string

from Python.string_fountain import string_fountain_gen

def vernam_cipher(file):
    file = open(file, "r")
    plain_text = file.readlines()
    key_generated = []
    keycnt = 0
    f = open("vernam_ciphered.txt", "w")
    for lines in plain_text:
        ciphered = ""
        for n in lines:
            key = random.randint(0, 255)
            ciphered += chr(ord(n)-key)
            key_generated[keycnt] = key
            keycnt+=1

        f.write(ciphered)
    f.close()
    return


def key_gen(numb):
    keys = random.sample(range(1, 255), numb)
    return keys


if __name__ == '__main__':
    print(chr(65))
    print(vernam_cipher("test.txt"))