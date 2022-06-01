from .operators import *


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
                                            to(negative(y), y * negative(x)), y
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
                res[index] = [x, y, z, to(plus(negative(x), implication(xor(z, y), x)), negative(z))]
                index += 1
    return res
