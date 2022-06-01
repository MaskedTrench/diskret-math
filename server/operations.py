#!/bin/python3
# -*- utf-8 -*-
from typing import List


def sknf(table: List[List[int]]) -> str:
    res = ''
    for pair in table:
        try:
            if pair[3] == 0:
                res = f"{res}({'-x' if pair[0] == 1 else 'x'} v {'-y' if pair[1] == 1 else 'y'} v {'-z' if pair[2] == 1 else 'z'}) ^ "
        
        except:
            if pair[2] == 0:
                res = f"{res}({'-x' if pair[0] == 1 else 'x'} v {'-y' if pair[1] == 1 else 'y'}) ^ "
    
    return res[0:-3]


def sdnf(table: List[List[int]]) -> str:
    res = ''
    for pair in table:
        try:
            pair[4]
            if pair[3] == 1:
                res = f"{res}({'-x' if pair[0] == 0 else 'x'} ^ {'-y' if pair[1] == 0 else 'y'} ^ {'-z' if pair[2] == 0 else 'z'}) v "
        
        except:
            if pair[2] == 1:
                res = f"{res}({'-x' if pair[0] == 0 else 'x'} ^ {'-y' if pair[1] == 0 else 'y'}) v "
    
    return res[0:-3]


def __build_polinom_chunc(chunk: List[int]) -> List[List[int]]:
    i = 0
    res = []
    while i != len(chunk) - 1:
        res.append(1 if 1 in [chunk[i], chunk[i+1]] else 0)
        i += 1
    
    return res


def polinom(table: List[List[int]]) -> str:
    res = []
    itter_res = []
    for pair in table:
        try:
            res.append(pair[3])
        
        except:
            res.append(pair[2])
    
    itter_res.append(res[0])
    
    while len(res) != 1:
        res = __build_polinom_chunc(res)
        itter_res.append(res[0])
    
    output = '1' if table[0][-1] == 1 else ''
    i = 1
    try:
        table[0][3]
        while i != len(itter_res):
            output += f' xyz ⊕' if itter_res[i] == 1 else ''
            i += 1
    
    except:
        while i != len(itter_res):
            output += ' xy ⊕' if itter_res[i] == 1 else ''
            i += 1
    
    return output[1:-2]


def monotonicity(array: List[List[int]]) -> bool:
    res = []
    try:
        # Implementation of cube method
        
        # Basement of cube
        res.append(array[0][3] <= array[4][3])
        res.append(array[0][3] <= array[1][3])
        res.append(array[4][3] <= array[5][3])
        res.append(array[1][3] <= array[5][3])
        
        # Roof of cube
        res.append(array[2][3] <= array[3][3])
        res.append(array[2][3] <= array[6][3])
        res.append(array[3][3] <= array[7][3])
        res.append(array[6][3] <= array[7][3])
        
        # Edges of cube
        res.append(array[0][3] <= array[2][3])
        res.append(array[1][3] <= array[3][3])
        res.append(array[4][3] <= array[6][3])
        res.append(array[5][3] <= array[7][3])
        
        
    except:
        # This is quadratic
        
        res.append(array[0][2] <= array[1][2])
        res.append(array[0][2] <= array[2][2])
        res.append(array[1][2] <= array[3][2])
        res.append(array[2][2] <= array[3][2])
    
    return True if False not in res else False


def minimalize_map(table: List[List[int]]) -> list[str]:
    res = []
    res.append('+' if table[0][-1] == 0 else '-')
    res.append('+' if table[-1][-1] == 1 else '-')
    res.append('+' if 'xy' in polinom(table) else '-')
    res.append('+' if monotonicity(table) else ['-'])
    
    return res

