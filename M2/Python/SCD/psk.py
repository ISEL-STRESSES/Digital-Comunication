import math
import random
import struct

import numpy as np
from matplotlib import pyplot as plt

from S2.Python.utils import file_load, ber_calculator_data, file_store

test_files_path = "../CD_TestFiles/"
scd_output_path = "scd_output/"

SAMPLES_PER_BIT = 10
BIT_RATE = 0.001


def store(vector, file_name, extension="_psk"):
    dest = scd_output_path + file_name.partition(".")[0] + extension + file_name.partition(".")[2]
    data_to_write = bytearray(struct.pack("f", vector))
    file_store(dest, data_to_write, scd_output_path)


def psk_modulator(data, freq, rate, alpha=1.0, draw=False):
    time = np.arange(0, rate * len(data), rate / SAMPLES_PER_BIT)
    vector = []
    channel_freq = freq * alpha  # frequency account for alpha
    for bit in data:
        aux = 0
        for i in range(aux, aux + SAMPLES_PER_BIT):
            calc = math.cos(2 * channel_freq * math.pi * time[i])  # amplitude
            if bit == 1:
                calc = -2 * calc
            else:
                calc = 2 * calc
            vector.append(calc)
        aux += SAMPLES_PER_BIT

    if draw:
        plt.plot(time, vector)
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude(V)")
        plt.title("PSK test")
        plt.show()

    return vector, float(channel_freq)


def psk_demodulator(data, freq):
    vector = []
    checker = abs(freq - 0) / 2

    for idx in range(0, len(data)):
        if idx % SAMPLES_PER_BIT == 0:
            if data[idx] > checker:
                vector.append(1)
            else:
                vector.append(0)

    return vector


if __name__ == '__main__':
    test_files = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
    freq = 2000
    alphas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    print("++++ PSK Modulator/Demodulator ++++")
    print("Alpha: " + str(1.0))
    print("With noise")
    for file_name in test_files:
        file_data = file_load(file_name, test_files_path)
        random_noise = np.array([random.uniform(-2.0, 2.0) for _ in range(len(file_data))])
        data_transform = np.array([file_data[i] + random_noise[i] for i in range(len(file_data))])
        vec, coder_freq = psk_modulator(data_transform, freq, BIT_RATE)
        dec = psk_demodulator(vec, coder_freq)
        ber = ber_calculator_data(file_data.bin, dec)
        print("File: " + file_name + " BER: " + str(ber))

    print("\nWithout Channel noise")
    for alpha in alphas:
        print("\nAlpha: " + str(alpha))
        for file_name in test_files:
            file_data = file_load(file_name, test_files_path)
            vec, coder_freq = psk_modulator(data=file_data, freq=freq, rate=BIT_RATE, alpha=alpha)
            dec = psk_demodulator(vec, coder_freq)
            ber = ber_calculator_data(file_data.bin, dec)
            print("File: " + file_name + " BER: " + str(ber))

    data = [1, 0, 1, 1, 0, 0, 0, 1]
    noise = [random.uniform(-1.0, 1.0) for i in range(len(data))]
    transform = [data[i] + noise[i] for i in range(len(data))]
    vec, coder_freq = psk_modulator(transform, freq=2000, rate=BIT_RATE, alpha=0.5, draw=True)
    decoded = psk_demodulator(vec, coder_freq)
    ber = ber_calculator_data(data, decoded)
    print("DATA:" + str(data) + " BER: " + str(ber))
