import shutil
from crc import CrcCalculator, Crc8
import random


def crc_file_compute(file):
    file = open(file, "rb")
    bytes_text = bytes(file.read())

    crc_calculator = CrcCalculator(Crc8.CCITT, True)
    checksum = hex(crc_calculator.calculate_checksum(bytes_text))

    shutil.copyfile("a.txt", "crc_file.txt")

    new_file = open("crc_file.txt")
    new_file.write(checksum)
    new_file.close()

    return checksum


def crc_file_check(file):
    file = open(file, 'r')
    last_line = file.readlines()[-1]
    file.close()

    checksum = str(crc_file_compute(file))

    return last_line == checksum


def make_error(file, error_percentage):
    file = open(file, 'rb')
    content = bytearray(file.read())
    file.close()

    error_size = int(len(content) * (error_percentage / 100))

    for i in range(error_size):
        content[i] = random.randint(0, 255)

    new_file = open("make_error", 'wb')
    new_file.write(content)
    new_file.close()
