import math
import struct
from matplotlib import pyplot as plt
import numpy as np

from S2.Python.utils import file_load, ber_calculator_data, file_store

test_files_path = "../CD_TestFiles/"
scd_output_path = "scd_output/"

NRZU_SAMPLES_PER_BIT = 10
PSK_SAMPLES_PER_BIT = 10


def store(vector, file_name, extension="_psk"):
    dest = scd_output_path + file_name.partition(".")[0] + extension + file_name.partition(".")[2]
    data_to_write = bytearray(struct.pack("f", vector))
    file_store(file_name, data_to_write, scd_output_path)


def psk_modulator(data, freq, rate, noise=0, alpha=0.0, draw=False):
    time = np.arange(0, rate * len(data), rate / PSK_SAMPLES_PER_BIT)
    vector = []
    channel_freq = freq * alpha   # frequency account for alpha
    for bit in data:
        aux = 0
        for i in range(aux, aux + PSK_SAMPLES_PER_BIT):
            calc = math.cos(2 * channel_freq * math.pi* time[i])  # amplitude
            if bit == 1:
                calc = -2 * calc
            else:
                calc = 2 * calc
            vector.append(calc + noise)
        aux += PSK_SAMPLES_PER_BIT

    if draw:
        plt.plot(time, vector)
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude(V)")
        plt.title("PSK")
        plt.show()

    return vector, float(channel_freq)


def psk_demodulator(data, freq):  # check if signal is
    vector = []
    checker = abs(freq - 0) / 2
    for idx in range(0, len(data)):
        if idx % PSK_SAMPLES_PER_BIT == 0:
            if data[idx] < checker:
                vector.append(1)
            else:
                vector.append(0)

    return vector


if __name__ == '__main__':
    test_files = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
    freq = 2000
    bit_rate = 0.001
    alpha = 1
    print("++++ PSK Modulator/Demodulator ++++")
    print("Alpha: " + str(alpha))
    for file_name in test_files:
        file_data = file_load(file_name, test_files_path)
        vec, channel_freq = psk_modulator(file_data, freq, bit_rate)
        dec = psk_demodulator(vec, channel_freq)
        ber = ber_calculator_data(file_data.bin, dec)
        print("File: " + file_name + " BER: " + str(ber))
    alpha = 0.5
    print("\nAlpha: " + str(alpha))
    for file_name in test_files:
        file_data = file_load(file_name, test_files_path)
        vec, channel_freq = psk_modulator(data=file_data, freq=freq, rate=bit_rate, alpha=alpha)
        dec = psk_demodulator(vec, channel_freq)
        ber = ber_calculator_data(file_data.bin, dec)
        print("File: " + file_name + " BER: " + str(ber))
    vec, channel_freq = psk_modulator([1, 0, 1, 1, 0, 0, 0, 1], freq=2000, rate=bit_rate, alpha=0.5, draw=True)
    print(vec)
    print(channel_freq)
