import secrets
from PIL import Image
import re
test_files_path = "../CD_TestFiles/"
img_files_output_path = "img_cipher_output/"


def img_cipher(file, lft_x=0, lft_y=0, rgt_x=0, rgt_y=0):
    # get file name and extension
    file_name = file.partition('.')[0]
    get_ext = file.partition('.')[2]

    key_extra_dim = secrets.randbelow(256)

    # open image
    plain_img = Image.open(test_files_path + file)

    # generate key
    width, height = plain_img.size
    key = secrets.token_bytes(width*height + key_extra_dim)

    window_info = "lft_x="+str(lft_x)+"\nlft_y="+str(lft_y)+"\nrgt_x="+str(rgt_x)+"\nrgt_y="+str(rgt_y)+""

    # cipher image
    # TODO(check if corners inside picture (below width and height))
    ciphered_img = make_vernam_cypher_img(plain_img, key, lft_x, lft_y, rgt_x, rgt_y)

    # save ciphered image
    ciphered_img.save(img_files_output_path + file_name + "_img_ciphered." + get_ext)

    # write key to file
    key_file = open(img_files_output_path + file_name + "_img_key.txt", "wb")
    key_file.write(key)
    key_file.close()

    # write window_info to file
    window_info_file = open(img_files_output_path + file_name + "_img_window_info.txt", "w", encoding='utf8')
    window_info_file.write(window_info)
    window_info_file.close()


def make_vernam_cypher_img(img, key, corner_left_x, corner_left_y, corner_right_x, corner_right_y):
    pixel_map = img.load()
    ciphered = Image.new('L', img.size)
    pixels_new = ciphered.load()
    p = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            cond_x = i <= corner_left_x or i >= corner_right_x
            cond_y = j <= corner_left_y or j >= corner_right_y
            if cond_x or cond_y:
                pixels_new[i, j] = pixel_map[i, j]
            else:
                pixels_new[i, j] = (pixel_map[i, j] ^ key[p]) % 256
            p += 1
            if p == len(key):
                p = 0
    return ciphered


def img_decipher(file):
    # get file name and extension
    file_name = file.partition("_img_ciphered")[0]
    get_ext = file.partition('.')[2]

    # read key
    file_key = open(img_files_output_path + file_name + "_img_key.txt", "rb")
    key = file_key.read()
    file_key.close()

    file_window_info = open(img_files_output_path + file_name + "_img_window_info.txt", "r", encoding='UTF-8')
    window_info = file_window_info.read()
    left_corner_x, left_corner_y, right_corner_x, right_corner_y = decode_window_info(window_info)

    try:
        # open image
        plain_img = Image.open(img_files_output_path + file)

        # decipher image
        ciphered_img = make_vernam_cypher_img(plain_img, key, left_corner_x, left_corner_y, right_corner_x, right_corner_y)

        # save ciphered image
        ciphered_img.save(img_files_output_path + file_name + "_img_deciphered." + get_ext)
    except IOError:
        print("ERROR")


def decode_window_info(win_info):
    left_corner_x = re.search('lft_x=(.*)\n', win_info).group(1)
    left_corner_y = re.search('lft_y=(.*)\n', win_info).group(1)
    right_corner_x = re.search('rgt_x=(.*)\n', win_info).group(1)
    right_corner_y = win_info.partition("rgt_y=")[2]
    return int(left_corner_x), int(left_corner_y), int(right_corner_x), int(right_corner_y)


if __name__ == '__main__':
    img_cipher("lena.bmp", 120, 125, 180, 180)
    img_decipher("lena_img_ciphered.bmp")

