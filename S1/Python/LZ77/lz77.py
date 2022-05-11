


def lz77_tokenizer(filename: str, window_size: int, buffer_size: int):
    input_txt = open(filename).read()
    output_file = open("tokens_" + filename, 'w')
    input_idx = 0
    dictionary = ""
    #if len(input) > buffer_size
    lab = input_txt[0:buffer_size]
    while input_idx < len(input_txt):
        print("lab = " + lab + "   dic = " + dictionary + "  str = " + input_txt)
        pos, buf, inov = find_substring(dictionary, lab)
        print(find_substring(dictionary, lab))

        dictionary += input_txt[input_idx:input_idx+pos+1]
        input_idx += buf+1

        lab = input_txt[input_idx:buffer_size+input_idx+1]


def find_sub(sl, l):
    sll = len(sl)
    if not sl:
        return -1
    for ind in reversed(range(len(l))):
        if l[ind:ind+sll] == sl:
            return ind
    return -1


def find_substring(dict, lab):
    if len(dict) == 0:
        return 0, 0, lab[0]
    best_length = 0
    offset = 0
    buf = dict + lab
    pointer = len(dict)
    for i in range(0, len(dict)):
        idx = len(dict)
        length = 0
        while buf[length + i] == buf[pointer + length]:
            length += 1
            if pointer + length == len(buf):
                length -= 1
                break
            if length + i >= pointer:
                break
        if length > best_length:
            best_length = length
            offset = idx - i
        if length == best_length and offset > idx - i:
            best_length = length
            offset = idx - i
        idx -= 1
    return offset, best_length, buf[pointer + best_length]


if __name__ == '__main__':
    """
    print(find_sub('ABCCD', 'ABC'))
    print(find_sub('ABCC', 'ABC'))
    print(find_sub('ABC', 'ABC'))
    print(find_sub('ABC', 'ABCCD'))
    print(find_sub('ABC', 'ABCC'))
    print(find_sub('ABC', 'ABC'))
    """
    #print(find_substring('ABCABCCBACB', 'CBA'))
    lz77_tokenizer("textlz77.txt", 10, 5)
