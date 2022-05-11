import string
import random

from StringFountain.string_fountain import string_fountain_gen


def check_security(stuff):
    lower = False
    upper = False
    digit = False
    symbol = False
    for i in stuff:
        if string.ascii_lowercase.__contains__(i):
            lower = True
        if string.ascii_uppercase.__contains__(i):
            upper = True
        if string.digits.__contains__(i):
            digit = True
        if string.punctuation.__contains__(i):
            symbol = True
        if lower and upper and digit and symbol:
            return True
    return False


def pass_gen(min, max):
    if max < min:
        return None
    if min <= 3:
        return None  # password with less than 3 characters can't contain lower case, upper case, digits and symbols
    pass_elements = list(string.ascii_letters + string.digits + string.punctuation)
    dim = random.randint(min, max)
    while True:
        random_chars = string_fountain_gen(pass_elements, [1/len(pass_elements)]*len(pass_elements), dim, False, False)
        if check_security(random_chars):
            break
    password = ""
    for n in random_chars:
        password += n
    return password


def create_password_files(filename):
    file = open(filename + ".txt", 'w')
    for i in range(0, 25):
        file.write(pass_gen(10, 10) + "\n")
    file.close()


if __name__ == '__main__':
    create_password_files("pass1")
    create_password_files("pass2")
    create_password_files("pass3")
    create_password_files("pass4")
    create_password_files("pass5")

