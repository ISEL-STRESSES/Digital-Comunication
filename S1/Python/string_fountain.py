import random
import matplotlib.pyplot as plot


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
    for i in result:
        file.write(i + ";")
    file.close()

    for i in strs:
        count[idx] = result.count(i)
    plot.bar(strs, count, width=0.5)
    plot.show()
    return result


if __name__ == '__main__':
    res = string_fountain(["aa", "bb", "b", "dd"], [0, 0, 0, 1], 3)
    print(res)
    res = string_fountain(["aba", "bab", "ab", "dasd"], [1 / 10, 2 / 10, 3 / 10, 4 / 10], 3)
    print(res)
