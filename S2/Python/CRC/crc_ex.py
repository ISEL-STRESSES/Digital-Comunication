# code based on
# (1) https://pypi.org/project/crc
# (2) https://barrgroup.com/downloads/code-crc-c


import random
import shutil

from crc import CrcCalculator, Crc8

local_path = "../CD_TestFiles/"
test_path = "./Test_Output/"


# Uses the CRC in a file to add error control.
def crc_file_compute(file_name):
    source = local_path + file_name
    dest = test_path + file_name.partition(".")[0] + "_crc." + file_name.partition(".")[2]
    file = open(source, "rb")
    bytes_text = bytes(file.read())
    file.close()

    crc_calculator = CrcCalculator(Crc8.CCITT, True)
    checksum = hex(crc_calculator.calculate_checksum(bytes_text))
    file = open(source, "r")
    new_file = open(dest, "w")

    for line in file:
        new_file.write(line)
    file.close()
    # shutil.copyfile(source, dest) # ain't working

    # new_file = open(dest, "a")  # open for appending
    new_file.write('\n' + checksum)
    new_file.close()
    return checksum


# Checks if the file has any error based on the CRC technique.
def crc_file_check(file_name):
    crc_file = test_path + file_name.partition(".")[0] + "_crc." + file_name.partition(".")[2]
    file = open(crc_file, 'r', errors='ignore')
    last_line = file.readlines()[-1]
    file.close()

    checksum = str(crc_file_compute(file_name))
    return last_line == checksum


# Makes random errors in a file for CRC check.
def make_error(file_name, error_percentage):
    source = test_path + file_name.partition(".")[0] + "_crc." + file_name.partition(".")[2]
    dest = test_path + file_name.partition(".")[0] + "_crc_error." + file_name.partition(".")[2]
    file = open(source, 'rb')
    byte_text = bytearray(file.read())
    file.close()
    shutil.copyfile(source, dest)

    error_size = int(len(byte_text) * (error_percentage / 100))

    for i in range(error_size):
        byte_text[i] = random.randint(0, 255)

    new_file = open(dest, "wb")
    new_file.write(byte_text)
    new_file.close()


if __name__ == '__main__':
    test_files = ["a.txt", "alice29.txt", "cp.htm", "Person.java", "progc.c"]
    print("++++ CRC check error ++++")
    for file_name in test_files:
        crc_file_compute(file_name)
        if crc_file_check(file_name):
            print(file_name, " \t!SUCCESS!")
        else:
            print(file_name, " !ERROR!\n")

    print("++++++ Make errors ++++++")
    errors = [0.0, 0.01, 0.1, 0.5, 1.0, 5.0]
    for file_name in test_files:
        print("\nFile : ", file_name)
        for error in errors:
            make_error(file_name, error)
            if crc_file_check(file_name):
                print("Error: ", error, " \t!SUCCESS!")
            else:
                print(file_name + " !ERROR! " + "Percentage\n" + str(error))
