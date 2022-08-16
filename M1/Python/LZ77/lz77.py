def lz77_tokenizer(filename: str, window_dim: int, buffer_dim: int):
    input_txt = open(filename).read()
    output_file = open("generated_tokens_" + filename, 'w')
    input_idx = 0
    dictionary = ""
    lab = input_txt[0:buffer_dim+1]
    while input_idx < len(input_txt):
        pos, size, inov_symbol = get_token_elements(dictionary, lab)
        token = "(" + str(pos) +", " + str(size) + ", " + str(inov_symbol) + ")"
        output_file.write(token + ";\n")
        print(token + "  lab = " + lab + "   dic = " + dictionary)   #FOR DEBUG PURPOSES
        dictionary += input_txt[input_idx:input_idx+size+1]
        input_idx += size+1
        lab = input_txt[input_idx:buffer_dim+input_idx+1]


def get_token_elements(dic, lab):
    if len(dic) == 0:
        return 0, 0, lab[0]
    window = dic + lab
    search_it = len(dic)
    l = 0
    p = 0
    for i in range(0, len(dic)):
        idx = len(dic)
        length = 0
        while window[length+i] == window[length + search_it]:
            length += 1
            if length + search_it == len(window):
                length -= 1
                break
            if length + i >= search_it:
                break
        if length > l:
            l = length
            p = idx-i
        if length == l and p > idx-i:
            l = length
            p = idx-i
        idx -= 1
    return p, l, window[l + search_it]


if __name__ == '__main__':
    lz77_tokenizer("textlz77.txt", 10, 5)
