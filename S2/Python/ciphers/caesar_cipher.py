local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"


def caesar_cipher(file):
    # read plain text
    plain_text_file = open(file, "rb")
    plain_text = plain_text_file.read()
    plain_text_file.close()


    # cipher text and write to file
    file_name = file.partition('.')[0]
    get_ext = file.partition(".")[2]
    ciphered_file = open("caesar_ciphered.txt", "wb")
    ciphered = make_caesar_cypher(plain_text)
    #for lines in plain_text:
    #    ciphered = ""
    #    for n in lines:
    #        ciphered += chr(ord(n)+3)
    ciphered_file.write(bytearray(ciphered))
    ciphered_file.close()


def make_caesar_cypher(text):
    ciphered = []
    numb = 3
    bytes = numb.to_bytes(1, 'big')
    for n in range(len(text)):
        ciphered.append((text[n] + numb))
    return ciphered


def make_caesar_decipher(text):
    ciphered = []
    numb = 3
    for n in range(len(text)):
        ciphered.append((text[n] - numb))
    return ciphered


def caesar_decipher(file):
    # read ciphered text
    file = open(file, "rb")
    ciphered_text = file.read()

    f = open("caesar_deciphered.txt", "wb")
    deciphered = make_caesar_decipher(ciphered_text)
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
    caesar_decipher("a_caesar_deciphered.txt")
    caesar_decipher("alice29_caesar_deciphered.txt")
    caesar_decipher("cp_caesar_deciphered.htm")
    caesar_decipher("lena_caesar_deciphered.bmp")
    caesar_decipher("Person_caesar_deciphered.java")
    caesar_decipher("progc_caesar_deciphered.c")


if __name__ == '__main__':
    caesar_cipher("../CD_TestFiles/test.txt")
    caesar_decipher("caesar_ciphered.txt")
