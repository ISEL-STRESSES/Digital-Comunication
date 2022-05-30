def ceaser_cipher(file):
    file = open(file, "r")
    plain_text = file.readlines()
    f = open("caeser_ciphered.txt", "w")
    for lines in plain_text:
        ciphered = ""
        for n in lines:
            ciphered += chr(ord(n)+3)
        f.write(ciphered)
    f.close()
    return


def ceaser_decipher(file):
    file = open(file, "r")
    ciphered_text = file.read().splitlines()
    f = open("caeser_deciphered.txt", "w")
    for lines in ciphered_text:
        deciphered = ""
        for n in lines:
            deciphered += chr(ord(n) - 3)
        f.write(deciphered + "\n")
    f.close()
    return deciphered


if __name__ == '__main__':
    ceaser_cipher("test.txt")
    ceaser_decipher("caeser_ciphered.txt")
