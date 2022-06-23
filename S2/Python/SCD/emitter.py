from bitstring import BitArray
from matplotlib import pyplot
import numpy as np

local_path = "../CD_TestFiles/"
test_path = "./Test_Output/"


def nrzu_coder():
    # source = local_path + file_name
    # dest = test_path + file_name.partition(".")[0] + "_NRZU." + file_name.partition(".")[2]
    # file = open(source, "rb")
    # dest_file = open(dest, "w")
    # aux = bytes(file.read())
    # byte_data = BitArray(aux)
    # dest_file.write(str(aux))
    # for bit in byte_data:
    #     if bit:
    #         dest_file.write(bit)
    #         print("1", end = '')
    #     else:
    #         dest_file.write(bit)
    #         print("0", end = '')
    # print(byte_data)
    # file.close()
    b = [0, 1, 0, 0, 1, 1, 1, 0]
    t = np.arange(0, 8, .01)
    j = 1
    p = []
    for i in range(0, 800, 1):
        if t[i] < j:
            p.append(b[j - 1])
            #print("up")
        else:
            p.append(b[j])
            #print("down")
            j = j+1
    print(p)
    pyplot.plot(t, p, color='k')
    pyplot.xlabel('Time in sec')
    pyplot.ylabel('Amplitude')
    pyplot.title('Unipolar')
    pyplot.show()
    # dest_file.close()


def psk_modulator(data):
    return 0


if __name__ == '__main__':
    nrzu_coder()
