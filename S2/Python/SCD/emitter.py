from bitstring import BitArray
from matplotlib import pyplot as plt
import numpy as np

test_files_path = "../CD_TestFiles/"
scd_output_path = "scd_output/"

SAMPLES_PER_BIT = 10
ORIGIN = 0


def nrzu_store(vector, file):
    # get file name and extension
    file_name = file.partition('.')[0]
    get_ext = file.partition('.')[2]
    nrzu_file_name = file_name + "_NRZU." + get_ext

    file = open(scd_output_path + nrzu_file_name, "wb")
    file.write(bytearray(vector))
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
    file = open(file_name, "rb")
    txt = file.read()
    file.close()
    text_as_bit = BitArray(bytes = txt)
    return text_as_bit


if __name__ == '__main__':
    a = file_load(test_files_path + "a.txt")
    # print(a)
    vec = nrzu_coder(data=a, amp=5, bit_rate=0.1)
    nrzu_store(vec, "a.txt")
