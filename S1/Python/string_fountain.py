import random


def string_fountain(strs, fmp, length):
    if len(strs) != len(fmp) or sum(fmp) != 1:
        return None
    for elem in strs:
        if strs.count(elem) > 1:    # check for repeated elements in strs parameter
            return None
    indices = random.sample(range(len(strs)), length)
    res = []
    for i in indices:
        res += strs[i]
    return res
