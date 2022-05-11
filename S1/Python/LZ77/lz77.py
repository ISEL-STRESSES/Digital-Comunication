def findStr(dic, cen):

    if cen in dic:
        for n in range(len(dic),0,-1):
            if cen == dic[n]:
                return (1,1,n)
    return None


def lz77tokenizer(str):
    dic = ""
    ret = []
    for n in range(0,len(str)):
        if findStr(dic,str[n]) is not None:
            dic += str[n]
            ret += [(0,n,str[n])]
    return ret


if __name__ == '__main__':
    print(findStr("bbva",'a'))
    #print(lz77tokenizer("aa"))



