test_files_path = "../CD_TestFiles/"
caesar_files_output_path = "caesar_output/"


def caesar_cipher(file):
    # read plain text
    plain_text_file = open(test_files_path + file, "rb")
    plain_text = plain_text_file.read()
    plain_text_file.close()

    # cipher text and write to file
    file_name = file.partition('.')[0]
    get_ext = file.partition('.')[2]
    ciphered_file = open(caesar_files_output_path + file_name + "_caesar_ciphered" + "." + get_ext, "wb")
    ciphered = make_caesar_cypher(plain_text)
    ciphered_file.write(bytearray(ciphered))
    ciphered_file.close()


def make_caesar_cypher(text):
    ciphered = []
    numb = 3
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
    deciphered_text_file = open(caesar_files_output_path + file, "rb")
    ciphered_text = deciphered_text_file.read()

    # decipher text and write to file
    file_name = file.partition("_caesar_ciphered")[0]
    get_ext = file.partition('.')[2]
    f = open(caesar_files_output_path + file_name + "_caesar_deciphered." + get_ext, "wb")
    deciphered = make_caesar_decipher(ciphered_text)
    f.write(bytearray(deciphered))
    f.close()


def cipher_test_files():
    caesar_cipher("a.txt")
    caesar_cipher("alice29.txt")
    caesar_cipher("cp.htm")
    #caesar_cipher("lena.bmp")
    caesar_cipher("Person.java")
    caesar_cipher("progc.c")


def decipher_test_files():
    caesar_decipher("a_caesar_ciphered.txt")
    caesar_decipher("alice29_caesar_ciphered.txt")
    caesar_decipher("cp_caesar_ciphered.htm")
    #caesar_decipher("lena_caesar_deciphered.bmp")
    caesar_decipher("Person_caesar_ciphered.java")
    caesar_decipher("progc_caesar_ciphered.c")


if __name__ == '__main__':
    cipher_test_files()
    decipher_test_files()
