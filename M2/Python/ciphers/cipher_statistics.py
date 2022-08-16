import math
import matplotlib.pyplot as plot
import numpy as np


def entropy_calc(file, file_path):
    file_name = file.partition('.')[0]
    file = open(file_path + file, "rb")
    counters = {byte: 0 for byte in range(2 ** 8)}

    for byte in file.read():
        counters[byte] += 1

    probabilities = [counter / file.tell() for counter in counters.values()]
    entropy = -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)
    print(file_name)
    print("Entropy = " + str(entropy))


def hist(file, file_path):
    file_name = file.partition('.')[0]
    file = open(file_path + file, "rb")
    counter = [0] * 256
    for byte in file.read():
        counter[byte] += 1

    strs = np.arange(start=0, stop=256, step=1)

    plot.bar(strs, counter)
    plot.savefig(file_path+file_name+"_hist.png")

    plot.show()

