import collections
import math
import random
import matplotlib.pyplot as plot
from scipy.stats import entropy


def entropy(data):
    e = 0
    counter = collections.Counter(data)
    l = len(data)
    for count in counter.values():
        # count is always > 0
        p_x = count / l
        e += - p_x * math.log2(p_x)

    return e


def string_fountain(strs, fmp, repeat):
    if len(strs) != len(fmp) or sum(fmp) != 1:
        return None
    for elem in strs:
        if strs.count(elem) > 1:    # check for repeated elements in strs parameter
            return None
    result = random.choices(strs, weights=fmp, k=repeat)
    count = [0] * len(strs)
    idx = 0
    file = open("stringoutput", 'w')
    string = ""
    for i in result:
        string += i
        file.write(i + ";")
    file.close()
    print(entropy(string))

    for i in strs:
        count[idx] = result.count(i)
        idx += 1

    # histogram creation
    plot.bar(strs, count)
    plot.show()
    return result


if __name__ == '__main__':
    res = string_fountain(["aa", "bb", "b", "dd"], [0, 0, 0, 1], 3)
    print(res)
    res = string_fountain(["aba", "bab", "ab", "dasd"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3)
    print(res)

