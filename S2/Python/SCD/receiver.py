import numpy as np
from bitstring import BitArray
from matplotlib import pyplot as plt

test_files_path = "../CD_TestFiles/"
scd_output_path = "scd_output/"

NRZU_SAMPLES_PER_BIT = 10


def find_min_bit_time(data):
    last = 0
    cnt = 1
    min = len(data)
    for n in range(len(data)):
        if last == data[n]:
            cnt += 1
        else:
            last = data[n]
            if cnt >1 and cnt < min:
                min = cnt
            cnt = 1
    return min


def find_freq(data):
    last = 0
    cnt = 0
    for n in range(len(data)):
        if last!=0:
            if data[n] == last:
                break
            else:
                if data[n] != 0:
                    last = data[n]
        last = data[n]
    return cnt


def nrzu_decoder(data):
    cnt = 1
    decoded = []

    for byte in data:
        if cnt == NRZU_SAMPLES_PER_BIT:
            cnt = 1
            if byte > 0:
                decoded.append(1)
            else:
                decoded.append(0)
        cnt += 1
    return decoded

def PSK_Demodulator(data):
    # check if signal is

def file_load(file_name):
    file = open(file_name, "rb")
    txt = file.read()
    file.close()
    #text_as_bit = BitArray(bytes=txt)
    return txt


if __name__ == '__main__':
    a = file_load(scd_output_path + "t_nrzu.txt")
    vec = nrzu_decoder(data=a)
    print(vec)
    text_as_bit = BitArray(vec)
