import math
import random
import matplotlib.pyplot as plot


def check_parameters_string_fountain(strs, fmp):
    if len(strs) != len(fmp) or sum(fmp) != 1:
        return False
    for elem in strs:
        if strs.count(elem) > 1:  # check for repeated elements in strs parameter
            return False
    return True


def string_fountain_gen(strs, fmp, repeat, histogram, entropy):
    generated_strings = random.choices(strs, weights=fmp, k=repeat)
    count = [0] * len(strs)
    index = 0
    file = open("stringoutput.txt", 'w')
    string = ""
    for i in generated_strings:
        string += i
        file.write(i + ";")
    file.close()

    for i in strs:
        count[index] = generated_strings.count(i)
        index += 1
    counts = []
    size = 0
    for n in count:
        if n != 0:
            size += n
            counts.append(n)

    if entropy:     #entropy calc
        print("Entropy = " + str(entropy_calc(counts, size)))

    if histogram:   # histogram creation
        plot.bar(strs, count)
        plot.show()
    return generated_strings


def string_fountain(strs, fmp, repeat, histogram, entropy):
    if check_parameters_string_fountain(strs, fmp):
        return string_fountain_gen(strs, fmp, repeat, histogram, entropy)
    return None


def entropy_calc(count, dim):
    entropy = 0
    for n in count:
        entropy += (-math.log2(n / dim)) * n / dim
    return entropy


if __name__ == '__main__':
    print(string_fountain(["aba", "bab", "ab", "dasd"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3, True, True))
