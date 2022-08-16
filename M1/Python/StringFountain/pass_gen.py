import string
import random
import matplotlib.pyplot as plot

from StringFountain.string_fountain import string_fountain_gen, entropy_calc


def analyse_password_strength(password):
    if check_security(password) is False:
        return "Weak Password"
    else:
        count = []
        occur, size = get_occur(password)
        for i in occur.values():
            count.append(i)
        entropy_password = entropy_calc(count, size)
        if entropy_password < 3:
            return "Weak Password"
        if entropy_password < 4:
            return "Medium Password"
        else:
            return "Strong Password"


def get_occur(word):
    num_occur = {}
    size = 0
    for i in word:
        size += 1
        if i in num_occur:
            num_occur[i] += 1
        else:
            num_occur[i] = 1
    return num_occur, size


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


def create_password_files(filename, min_size, max_size, amount):
    file = open(filename + ".txt", 'w')
    for i in range(0, amount):
        file.write(pass_gen(min_size, max_size) + "\n")
    file.close()


def analyse_password_file(filename):
    file = open(filename)
    passwords = file.readlines()
    classification_passes = [0, 0, 0]
    rnd = []
    for n in passwords:
        rnd += n
        if analyse_password_strength(n) == "Weak Password":
            classification_passes[0] +=1
        else:
            if analyse_password_strength(n) == "Medium Password":
                classification_passes[1] += 1
            else:
                classification_passes[2] += 1
    password_sec_levels = ['Weak Password', 'Medium Password', 'Strong Password']
    plot.bar(password_sec_levels, classification_passes)
    plot.show()
    return classification_passes


if __name__ == '__main__':
    create_password_files("pass1", 4, 4, 100)
    analyse_password_file("pass1.txt")
    create_password_files("pass2", 10, 10, 100)
    analyse_password_file("pass2.txt")
    create_password_files("pass3", 15, 16, 100)
    analyse_password_file("pass3.txt")
    create_password_files("pass4", 20, 22, 100)
    analyse_password_file("pass4.txt")
    create_password_files("pass5", 30, 30, 100)
    analyse_password_file("pass5.txt")

