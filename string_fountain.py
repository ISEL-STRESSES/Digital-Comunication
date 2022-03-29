import random


def string_fountain(strs, fmp, length):
    if len(strs) != len(fmp): return "no"
    if sum(fmp) != 1: return "fmp not valid"
    for elem in strs:
        if strs.count(elem) > 1: return "no"
    indices = random.sample(range(len(strs)), length)
    res = []
    for i in indices:
        res += strs[i]
    return res

