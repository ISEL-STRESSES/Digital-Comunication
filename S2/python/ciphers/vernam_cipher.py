import random
import string


def vernam_cipher(file):
    file = open(file, "r")
    plain_text = file.readlines()
    key_generated = []
    keycnt = 0
    f = open("vernam_ciphered.txt", "wb", encoding="utf-8")
    cnt = 0
    for lines in plain_text:
        cipher, key = makeVernamCypher(lines)
        print(cipher)
        f.write(cipher)
        key_generated[cnt] = key
        cnt += 1
    #for lines in plain_text:
    #    ciphered = ""
    #    for n in lines:
    #        key = random.randint(0, 255)
    #        ciphered += chr(ord(n)-key)
    #        key_generated[keycnt] = key
    #        keycnt+=1
    #    f.write(ciphered)
    f.close()
    return


def makeVernamCypher(text):
    key = key_gen(len(text))
    ciphered = ""
    p = 0
    for char in text:
        ciphered += chr(ord(char) ^ key[p])
        p += 1
        if p == len(key):
            p = 0
    return ciphered, key


def key_gen(numb):
    keys = random.sample(range(1, 255), numb)
    return keys


if __name__ == '__main__':
    print(chr(65))
    print(vernam_cipher("test.txt"))