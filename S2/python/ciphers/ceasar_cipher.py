def ceaser_cipher(file):
    file = open(file, "r")
    plain_text = file.read()
    ciphered = ""
    for n in plain_text:
        ciphered += chr(ord(n)+3)
    f = open("caeser_ciphered.txt", "w")
    f.write(ciphered)
    return ciphered

def ceaser_decipher(file):
    file = open(file, "r")
    ciphered_text = file.read()
    deciphered = ""
    for n in ciphered_text:
        deciphered += chr(ord(n) - 3)
    f = open("caeser_deciphered.txt", "w")
    f.write(deciphered)
    return deciphered


if __name__ == '__main__':
    print(ceaser_cipher("test.txt"))
    print(ceaser_decipher("caeser_ciphered.txt"))
