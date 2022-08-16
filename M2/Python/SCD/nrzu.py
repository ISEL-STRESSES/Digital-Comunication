import random

import numpy as np
from bitstring import BitArray
from matplotlib import pyplot as plt

from S2.Python.utils import ber_calculator_data, file_load

test_files_path = "../CD_TestFiles/"
scd_output_path = "scd_output/"

SAMPLES_PER_BIT = 10
BIT_RATE = 0.001


def nrzu_coder(data, amp, bit_rate, alpha=1.0, draw=False):
    time = np.arange(0, bit_rate * len(data), bit_rate / SAMPLES_PER_BIT)
    dots = []
    channel_amp = amp * alpha
    for bit in data:
        aux = 0
        for i in range(aux, aux + SAMPLES_PER_BIT):
            dots.append(bit * channel_amp)
        aux += SAMPLES_PER_BIT

    if draw:
        plt.plot(time, dots)
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude(V)")
        plt.title("NRZU Test")
        plt.show()
    return BitArray(dots), float(channel_amp)


def nrzu_decoder(data, amp):
    dec = []

    for idx in range(0, len(data)):
        if idx % SAMPLES_PER_BIT == 0:
            if data[idx] > (amp / 2):
                dec.append(1)
            else:
                dec.append(0)

    return dec


if __name__ == '__main__':
    test_files = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
    amp = 5
    alphas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    print("++++ NRZU coder/decoder ++++")
    print("Alpha: " + str(1.0))
    print("With noise")
    for file_name in test_files:
        file_data = file_load(file_name, test_files_path)
        random_noise = np.array([random.uniform(-1.0, 1.0) for _ in range(len(file_data))])
        data_transform = np.array([file_data[i] + random_noise[i] for i in range(len(file_data))])
        vec, coder_amp = nrzu_coder(file_data, amp, BIT_RATE)
        dec = nrzu_decoder(vec, coder_amp)
        ber = ber_calculator_data(file_data.bin, dec)
        print("File: " + file_name + " BER: " + str(ber))

    print("\nWithout noise")
    for alpha in alphas:
        print("Alpha: " + str(alpha))
        for file_name in test_files:
            file_data = file_load(file_name, test_files_path)
            constant_noise = random.random() * random.randint(-1, 1)
            data_transform = np.array([file_data[i] * constant_noise for i in range(len(file_data))])
            vec, coder_amp = nrzu_coder(data_transform, amp, BIT_RATE, alpha=alpha)
            dec = nrzu_decoder(vec, coder_amp)
            ber = ber_calculator_data(file_data.bin, dec)
            print("File: " + file_name + " BER: " + str(ber))

    data = [1, 0, 1, 1, 0, 0, 0, 1]
    noise = [random.uniform(-1.0, 1.0) for i in range(len(data))]
    transform = [data[i] + noise[i] for i in range(len(data))]
    cod, a = nrzu_coder(transform, amp, BIT_RATE, draw=True)
    decoded = nrzu_decoder(cod, a)
    ber = ber_calculator_data(data, decoded)
    print("DATA:" + str(data) + " BER: " + str(ber))
