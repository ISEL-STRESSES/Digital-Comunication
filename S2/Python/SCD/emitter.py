from bitstring import BitArray
from matplotlib import pyplot as plt
import numpy as np

local_path = "../CD_TestFiles/"
test_path = "./Test_Output/"

SAMPLES_PER_BIT = 10
ORIGIN = 0


def nrzu_store_line(vector, file_name, opened, file=None):
    if not opened:
        file = open(file_name, "wb")
    file.write(vector)
    file.close()


def nrzu_store(vectors, file_name):
    dest = test_path + file_name.partition(".")[0] + "_NRZU." + file_name.partition(".")[2]
    if len(vectors) == 1:
        nrzu_store_line(vectors, dest, False)
    file = open(dest, "w")
    for vector in vectors:
        file.write(vector)
    file.close()


def nrzu_coder(data, amp, bit_rate):
    time = np.arange(ORIGIN, bit_rate * len(data), bit_rate / SAMPLES_PER_BIT)
    dots = []

    for bit in data:
        aux = 0
        for i in range(aux, aux + SAMPLES_PER_BIT):
            dots.append(bit * amp)
        aux += SAMPLES_PER_BIT

    plt.plot(time, dots)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude(V)")
    plt.title("NRZU")
    plt.show()
    return dots


def file_load(file_name):
    file = open(file_name, "r").readlines() # open(file_name, "rb").readlines()
    print(file)
    print()
    byte = BitArray()
    for line in file:
        # transformar uma linha em um array de chars nao ha a puta do .map{}
        # line.map{word -> word.map{it}}.map{ it.toBin() } :list<list<char>>
        for word in line:
            for char in word:
                byte.append(bytes(char))
        print(bytes(line))
        print()

    bits = [bin(bit)[2:] for bit in bytes(byte)]
    return bits


if __name__ == '__main__':
    a = file_load(local_path + "a.txt")
    print(a)
    # vec = nrzu_coder(data=a, amp=5, bit_rate=0.1)
    # nrzu_store(vec, "a.txt")
