import random
import string

from S1.Python.StringFountain.string_fountain import string_fountain_gen


def cc_already_exists(new_cc):
    global already_used_cc
    if already_used_cc.count(int(new_cc)) > 0:
        print("Element Exists")
        return True
    return False


def gen_cc():
    global already_used_cc
    while True:
        random_chars = string_fountain_gen(string.digits, [1/len(string.digits)]*len(string.digits), 8, False, False)
        cc = ""
        for n in random_chars:
            cc += n
        if cc_already_exists(cc) is False:
            break
    already_used_cc.append(cc)

    return cc


def gen_nome(first_name, last_name):
    fname = string_fountain_gen(first_name, [1 / len(first_name)] * len(first_name), random.randint(1, 2), False, False)
    lname = string_fountain_gen(last_name, [1 / len(last_name)] * len(last_name), random.randint(1, 2), False, False)

    name = ""
    for n in fname:
        name += str(n + " ")
    for n in lname:
        name += str(n + " ")
    return name


def table_contents_gen(first_name_text, last_name_text, concelho_text, prof_text):
    cc = gen_cc()
    name = gen_nome(first_name_text, last_name_text)
    concelho = str(string_fountain_gen(concelho_text, [1/len(concelho_text)]*len(concelho_text), 1, False, False)[0])
    prof = str(string_fountain_gen(prof_text, [1/len(prof_text)]*len(prof_text), 1, False, False)[0])
    return cc, name, concelho, prof


def print_teste_results(person_file_name, bet_file_name, quantity):
    first_name_txt = open("../AuxFiles/Nomes.txt").read().splitlines()
    last_name_input_txt = open("../AuxFiles/Apelidos.txt").read().splitlines()
    concelho_txt = open("../AuxFiles/Concelhos.txt").read().splitlines()
    prof_txt = open("../AuxFiles/Profissões.txt").read().splitlines()
    file_person_info = open(person_file_name + ".txt", 'w')
    file_bet = open(bet_file_name + ".txt", 'w')
    global already_used_cc
    already_used_cc = []

    for n in range(0, quantity):
        cc, name, concelho, prof = table_contents_gen(first_name_txt, last_name_input_txt, concelho_txt, prof_txt)
        file_person_info.write(cc + "; " + name + "; " + concelho + "; " + prof + "\n")
    for n in range(0, quantity):
        bet = random.sample(range(1, 50), 5)
        bet50 = ""
        for k in bet:
            bet50 += " " + str(k)
        bet = random.sample(range(1, 11), 2)
        bet11 = ""
        for k in bet:
            bet11 += " " + str(k)
        month = random.randint(1, 12)
        year = random.randint(1900, 2021)
        maxday = 31
        if month == 2:
            if year/4 == 0:
                maxday = 29
            else:
                maxday = 28
        else:
            if month in [4, 6, 9, 11]:
                maxday = 30
        day = random.randint(1, maxday)
        date = str(str(day) + "-" + str(month) + "-" + str(year))
        file_bet.write(already_used_cc[n] + ";" + str(bet50) + ";" + str(bet11) + "; " + date + "\n")


if __name__ == '__main__':
    print_teste_results("p_info1", "b1", 1000)
    print_teste_results("p_info2", "b2", 1000)
    print_teste_results("p_info3", "b3", 1000)
    print_teste_results("p_info4", "b4", 1000)
    print_teste_results("p_info5", "b5", 1000)
