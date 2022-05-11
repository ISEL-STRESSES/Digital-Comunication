import string

from S1.Python.StringFountain.string_fountain import string_fountain_gen


def alphanumeric_gen():
    pass_elements = list(string.ascii_uppercase + string.digits)
    random_alphanumeric = string_fountain_gen(pass_elements, [1/len(pass_elements)]*len(pass_elements), 24, False, False)
    alphanumeric_key = ""
    i = 0
    for n in random_alphanumeric:
        alphanumeric_key += n
        i += 1
        if i == 4:
            alphanumeric_key += " "
            i = 0
    return alphanumeric_key


def create_password_files(filename):
    file = open(filename, 'w')
    for i in range(0, 25):
        file.write(alphanumeric_gen() + "\n")
    file.close()


if __name__ == '__main__':
    create_password_files("alphanumeric1")
    create_password_files("alphanumeric2")
    create_password_files("alphanumeric3")
    create_password_files("alphanumeric4")
    create_password_files("alphanumeric5")
    print(alphanumeric_gen())
