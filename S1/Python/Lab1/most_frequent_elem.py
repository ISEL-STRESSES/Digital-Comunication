from collections import Counter


def most_frequent_elem(file):
    return Counter(open(file, "r").read()).most_common(1)
