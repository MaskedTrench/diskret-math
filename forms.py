def negative(x): return 0 if x == 1 else 0


def implication(x, y): return 1 if x == y else 0


def plus(x, y): return 1 if x + y == 2 else x + y


def xor(x, y): return 1 if x != y else 0


def to(x, y): return 1 if x <= y else 0


def double_build_sknf(table):
    tmp = ''
    for pair in table:
        if pair[2] == 0:
            tmp = f"{tmp}({'-x' if table[0] == 1 else 'x'} v {'-y' if table[1] == 1 else 'y'}) ^ "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def third_build_sknf(table):
    tmp = ''
    for pair in table:
        if pair[3] == 0:
            tmp = f"{tmp}({'-x' if table[0] == 1 else 'x'} v {'-y' if table[1] == 1 else 'y'} v {'-z' if table[2] == 1 else 'z'}) ^ "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def double_build_sdnf(table):
    tmp = ''
    for pair in table:
        if pair[2] == 0:
            tmp = f"{tmp}({'-x' if table[0] == 1 else 'x'} ^ {'-y' if table[1] == 1 else 'y'}) v "
    tmp = tmp[0:len(tmp)-3]
    return tmp


def third_build_sdnf(table):
    tmp = ''
    for pair in table:
        if pair[3] == 0:
            tmp = f"{tmp}({'-x' if table[0] == 1 else 'x'} ^ {'-y' if table[1] == 1 else 'y'} ^ {'-z' if table[2] == 1 else 'z'}) v "
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


def minimalization(table, index):
    return {
        0: [
            [[1, 0], [1, 1]], "x∨¬y", "x∨¬y",
        ],
        1: [
            [[1, 0], [0, 0]], "¬x¬y", "¬x∧¬y",
        ],
        2: [
            [[1, 1], [0, 0]], "¬x", "¬x",
        ],
        3: [
            [[0, 0, 1, 0], [1, 1, 0, 1]], "x¬y∨x¬z∨¬xyz", "(x∨y)∧(x∨z)∧(¬x∨¬y∨¬z)",
        ],
        4: [
            [[1, 0, 1, 0], [0, 0, 0, 0]], "¬¬x¬y¬z∨¬xyz", "¬x∧(¬y∨z)∧(y∨¬z)",
        ],
        5: [
            [[1, 1, 1, 1], [1, 0, 1, 0]], "¬x∨yz∨¬y¬z", "(¬x∨¬y∨z)∧(¬x∨y∨¬z)"
        ]}[index]


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
