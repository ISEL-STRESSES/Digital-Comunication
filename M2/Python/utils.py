from bitstring import BitArray


def ber_calculator_file(original, tester):
    original_file = open(original).readlines()
    tester_file = open(tester).readlines()
    return ber_calculator_data(original_file, tester_file)


def ber_calculator_data(original, tester):
    size_original = len(original)
    size_tester = len(tester)

    error = abs(size_tester - size_original)
    for i in range(0, size_original):
        if int(original[i]) != tester[i]:
            error += 1

    return error / float(size_original)


def file_load(file_name, src_path):
    file = open(src_path + file_name, "rb")
    txt = file.read()
    file.close()
    text_as_bit = BitArray(bytes=txt)
    return text_as_bit


def file_store(file_name, data, dst_path):
    file = open(dst_path + file_name, "wb")
    file.write(data)
    file.close()
