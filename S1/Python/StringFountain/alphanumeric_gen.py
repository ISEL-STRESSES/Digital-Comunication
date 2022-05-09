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


if __name__ == '__main__':
    print(alphanumeric_gen())
    print(alphanumeric_gen())
    print(alphanumeric_gen())
