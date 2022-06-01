#!/bin/python3
# -*- coding: utf-8 -*-

def negative(x: int) -> int: return 0 if x == 1 else 0

def implication(x: int, y: int) -> int: return 1 if x == y else 0

def plus(x: int, y: int) -> int: return 1 if x + y == 2 else x + y

def xor(x: int, y: int) -> int: return 1 if x != y else 0

def to(x: int, y: int) -> int: return 1 if x <= y else 0