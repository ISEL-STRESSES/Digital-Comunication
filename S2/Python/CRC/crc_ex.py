# code based on
# (1) https://pypi.org/project/crc
# (2) https://barrgroup.com/downloads/code-crc-c


import shutil
from crc import CrcCalculator, Crc8
import random


# Uses the CRC in a file to add error control.
def crc_file_compute(file):
    f = open(file, "rb")
    bytes_text = bytes(f.read())
    f.close()

    crc_calculator = CrcCalculator(Crc8.CCITT, True)
    checksum = hex(crc_calculator.calculate_checksum(bytes_text))
    new_file_name = f.name + "_crc"
    shutil.copyfile(f.name, new_file_name)

    new_file = open(new_file_name, "a")
    new_file.write('\n' + checksum)
    new_file.close()

    return checksum


# Checks if the file has any error based on the CRC technique.
def crc_file_check(file):
    f = open(file, 'r')
    last_line = f.readlines()[-1]
    f.close()

    checksum = str(crc_file_compute(file))

    return last_line == checksum


# Makes random errors in a file for CRC check.
def make_error(file, error_percentage):
    file = open(file, 'rb')
    content = bytearray(file.read())
    file.close()
    new_file_name = file.name + "_crc_error"
    shutil.copyfile(file.name, new_file_name)

    error_size = int(len(content) * (error_percentage / 100))

    for i in range(error_size):
        content[i] = random.randint(0, 255)

    new_file = open(new_file_name, "wb")
    new_file.write(content)
    new_file.close()


if __name__ == '__main__':
    test_files = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
    print("crc check for errors")
    for file in test_files:
        crc_file_compute(file)
        if not crc_file_check(file):
            print(file, " !ERROR!\n")

    print("make errors")
    errors = [0, 0.01, 0.1, 0.5, 1, 5]
    for file in test_files:
        for error in errors:
            make_error(file, error)
            if not crc_file_check(file):
                print(file, " !ERROR! ", error, "Percentage\n")
