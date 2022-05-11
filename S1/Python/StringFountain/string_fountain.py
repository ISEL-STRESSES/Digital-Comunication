import random
from collections import Counter

import matplotlib.pyplot as plot
import scipy
from scipy import stats


def ent(data):
    """Calculates entropy of the passed `pd.Series`"""
    p_data = data.value_counts()           # counts occurrence of each value
    entropy = scipy.stats.entropy(p_data)  # get entropy from counts
    return entropy


def check_parameters_string_fountain(strs, fmp):
    if len(strs) != len(fmp) or sum(fmp) != 1:
        return False
    for elem in strs:
        if strs.count(elem) > 1:    # check for repeated elements in strs parameter
            return False
    return True


def string_fountain_gen(strs, fmp, repeat, histogram, entropy):
    result = random.choices(strs, weights=fmp, k=repeat)
    count = [0] * len(strs)
    idx = 0
    file = open("stringoutput.txt", 'w')
    string = ""
    for i in result:
        string += i
        file.write(i + ";")
    file.close()
    if entropy:
        print(stats.entropy(list(Counter(fmp).values()), base=2))

    for i in strs:
        count[idx] = result.count(i)
        idx += 1

    # histogram creation
    if histogram:
        plot.bar(strs, count)
        plot.show()

    return result


def string_fountain(strs, fmp, repeat, histogram, entropy):
    if check_parameters_string_fountain(strs, fmp):
        return string_fountain_gen(strs, fmp, repeat, histogram, entropy)
    return None


if __name__ == '__main__':
    res = string_fountain(["aa", "bb", "b", "dd"], [0, 0, 0, 1], 3, False, False)
    print(res)
    res = string_fountain(["aba", "bab", "ab", "dasd"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3, False, False)
    print(res)
