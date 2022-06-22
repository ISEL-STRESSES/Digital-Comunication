local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"


def caesar_cipher(file):
    # read plain text
    plain_text_file = open(file, "r")
    plain_text = plain_text_file.readlines()
    plain_text_file.close()

    f = open("caesar_ciphered.txt", "w")
    for lines in plain_text:
        ciphered = ""
        for n in lines:
            ciphered += chr(ord(n)+3)
        f.write(ciphered)
    f.close()


def caesar_decipher(file):
    file = open(file, "r")
    ciphered_text = file.read().splitlines()
    f = open("caesar_deciphered.txt", "w")
    for lines in ciphered_text:
        deciphered = ""
        for n in lines:
            deciphered += chr(ord(n) - 3)
        f.write(deciphered + "\n")
    f.close()
    return deciphered


def cipher_test_files():
    caesar_cipher("a.txt", "a_vernam_key.txt")
    caesar_cipher("alice29.txt", "alice29_vernam_key.txt")
    caesar_cipher("cp.htm", "cp_vernam_key.htm")
    caesar_cipher("lena.bmp", "lena_vernam_key.bmp")
    caesar_cipher("Person.java", "Person_vernam_key.java")
    caesar_cipher("progc.c", "progc_vernam_key.c")


def decipher_test_files():
    caesar_decipher("a_vernam_ciphered.txt", "a_vernam_key.txt")
    caesar_decipher("alice29_vernam_ciphered.txt", "alice29_vernam_key.txt")
    caesar_decipher("cp_vernam_ciphered.htm", "cp_vernam_key.htm")
    caesar_decipher("lena_vernam_ciphered.bmp", "lena_vernam_key.bmp")
    caesar_decipher("Person_vernam_ciphered.java", "Person_vernam_key.java")
    caesar_decipher("progc_vernam_ciphered.c", "progc_vernam_key.c")


if __name__ == '__main__':
    caesar_cipher("../CD_TestFiles/test.txt")
    caesar_decipher("caesar_ciphered.txt")
