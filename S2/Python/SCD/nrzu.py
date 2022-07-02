import random
from bitstring import BitArray
from matplotlib import pyplot as plt
import numpy as np
from S2.Python.utils import ber_calculator_data, file_load

test_files_path = "../CD_TestFiles/"
scd_output_path = "scd_output/"

NRZU_SAMPLES_PER_BIT = 10


def nrzu_coder(data, amp, bit_rate, noise=0, alpha=1, draw=False):
    time = np.arange(0, bit_rate * len(data), bit_rate / NRZU_SAMPLES_PER_BIT)
    dots = []
    for bit in data:
        aux = 0
        for i in range(aux, aux + NRZU_SAMPLES_PER_BIT):
            dots.append(bit * amp * alpha + 0.1 * random.randint(0, noise))
        aux += NRZU_SAMPLES_PER_BIT

    if draw:
        plt.plot(time, dots)
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude(V)")
        plt.title("NRZU")
        plt.show()
    return BitArray(dots), amp


def nrzu_decoder(data, amp):
    cnt = 0
    decoded = []

    for bit in data:
        if cnt % NRZU_SAMPLES_PER_BIT == 0:
            cnt = 0
            if bit > amp:
                decoded.append(1)
            else:
                decoded.append(0)
        cnt += 1
    return decoded


if __name__ == '__main__':
    test_files = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
    amp = 5
    bit_rate = 0.001
    print("++++ NRZU coder/decoder ++++")
    for file_name in test_files:
        file_data = file_load(file_name, test_files_path)
        vec, coder_amp = nrzu_coder(file_data, amp, bit_rate)
        dec = nrzu_decoder(vec, coder_amp)
        ber = ber_calculator_data(file_data.bin, dec)
        print("File: " + file_name + "BER: " + str(ber))

