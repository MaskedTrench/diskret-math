def negative(x): return 0 if x == 1 else 0


def implication(x, y): return 1 if x == y else 0


def plus(x, y): return 1 if x + y == 2 else x + y


def xor(x, y): return 1 if x != y else 0


def to(x, y): return 1 if x <= y else 0


def double_build_sknf(table):
    tmp = ''
    for pair in table:
        if pair[2] == 0:
            tmp = f"{tmp}({'-x' if pair[0] == 1 else 'x'} v {'-y' if pair[1] == 1 else 'y'}) ^ "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def third_build_sknf(table):
    tmp = ''
    for pair in table:
        if pair[3] == 0:
            tmp = f"{tmp}({'-x' if pair[0] == 1 else 'x'} v {'-y' if pair[1] == 1 else 'y'} v {'-z' if pair[2] == 1 else 'z'}) ^ "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def double_build_sdnf(table):
    tmp = ''
    for pair in table:
        if pair[2] == 0:
            tmp = f"{tmp}({'-x' if pair[0] == 0 else 'x'} ^ {'-y' if pair[1] == 0 else 'y'}) v "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def third_build_sdnf(table):
    tmp = ''
    for pair in table:
        if pair[3] == 0:
            tmp = f"{tmp}({'-x' if pair[0] == 0 else 'x'} ^ {'-y' if pair[1] == 0 else 'y'} ^ {'-z' if pair[2] == 0 else 'z'}) v "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def build_polinom(table, index):
    res = {
        0: "1⊕y⊕xy",
        1: "1⊕y⊕x⊕xy",
        2: "1⊕x",
        3: "yz⊕x",
        4: "1⊕z⊕y⊕x⊕xz⊕xy",
        5: "1⊕xz⊕xy",
    }
    return res[index]

def build_polinom_2(massive2):
    massive_2_2 = [-1] * 4
    masive2_1 = [-1] * 4 
    for i in range(4): 
        masive2_1[i] = [-1] * 4 
    for i in range(4): 
        masive2_1[0][i] = massive2[i]    
    for l in range(3):
        massive_2_2[0] = massive2[0]
        for i in range(3 - l):
            if(masive2_1[l][i] == masive2_1[l][i + 1]):
                masive2_1[l + 1][i] = 0
            else:
                masive2_1[l + 1][i] = 1
        massive_2_2[l + 1] = masive2_1[l + 1][0]        
    for l in range(4): 
        for i in range(4): 
            print(masive2_1[l][i], end=' ')
        print()
    print(massive_2_2)
    string = ""
    if(massive_2_2[0] != 0):
        string = string + "1⊕ "
    if(massive_2_2[2] != 0):
        string = string + "1x1⊕ "
    if(massive_2_2[1] != 0):
        string = string + "1x2⊕ " 
    if(massive_2_2[3] != 0):
        string = string + "1x1x2⊕ "  
    string = string[:-1]
    tmp = ''
    for i in range(4):
        tmp = f'{tmp}{string} {massive2[i]}\n'
    return tmp
        
def build_polinom_3(massive3):
    massive_3_2 = [-1] * 8
    masive3_1 = [-1] * 8 
    for i in range(8): 
        masive3_1[i] = [-1] * 8 
    for i in range(8): 
        masive3_1[0][i] = massive3[i]    
    for l in range(7):
        massive_3_2[0] = massive3[0]
        for i in range(7 - l):
            if(masive3_1[l][i] == masive3_1[l][i + 1]):
                masive3_1[l + 1][i] = 0
            else:
                masive3_1[l + 1][i] = 1
        massive_3_2[l + 1] = masive3_1[l + 1][0]        
    for l in range(8): 
        for i in range(8): 
            print(masive3_1[l][i], end=' ')
        print()
    print(massive_3_2)
    string = ""
    if(massive_3_2[0] != 0):
        string = string + "1⊕ "
    if(massive_3_2[4] != 0):
        string = string + "1x1⊕ "
    if(massive_3_2[2] != 0):
        string = string + "1x2⊕ " 
    if(massive_3_2[1] != 0):
        string = string + "1x3⊕ "  
    if(massive_3_2[6] != 0):
        string = string + "1x1x2⊕ "
    if(massive_3_2[5] != 0):
        string = string + "1x1x3⊕ "
    if(massive_3_2[3] != 0):
        string = string + "1x2x3⊕ "
    if(massive_3_2[7] != 0):
        string = string + "1x1x2x3⊕ "
    string = string[:-1]
    tmp = ''
    for i in range(8):
        tmp = f'{tmp}{string} {massive3[i]}\n'
    return tmp

def one_result():
    res = list(range(2 ** 2))
    index = 0
    for x in [0, 1]:
        for y in [0, 1]:
            res[index] = [x, y, plus(x, implication(x, y))]
            index += 1
    return res


def two_result():
    res = list(range(2 ** 2))
    index = 0
    for x in [0, 1]:
        for y in [0, 1]:
            res[index] = [x, y, to(x, negative(y)) * xor(y, negative(x))]
            index += 1
    return res


def three_result():
    res = list(range(2 ** 2))
    index = 0
    for x in [0, 1]:
        for y in [0, 1]:
            res[index] = [x, y, implication(x,
                                        xor(
                                            implication(negative(y), y * negative(x)), y
                                        )
                                     )
                          ]
            index += 1
    return res


def fouth_result():
    res = list(range(2 ** 3))
    index = 0
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                res[index] = [x, y, z, xor(x, y * z)]
                index += 1
    return res


def five_result():
    res = list(range(2 ** 3))
    index = 0
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                res[index] = [x, y, z, implication(plus(x, y), negative(x) * z)]
                index += 1
    return res


def six_result():
    res = list(range(2 ** 3))
    index = 0
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                res[index] = [x, y, z, plus(negative(x), to(implication(xor(z, y), x), negative(z)))]
                index += 1
    return res
