#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from itertools import combinations


def elem_in_list(elements: iter, _list: list):
    sol = False
    for x in elements:
        if x in _list:
            sol = True
    return sol


def iter_or_iter(n: int, text: list, k: int) -> float:
    combis = list(combinations(range(1, n + 1), k))
    all = len(combis)
    a_s = [i for i, e in enumerate(text, 1) if e == 'a']
    total = sum([1 for i in combis if elem_in_list(i, a_s)])
    return round(total / all, 4)


if __name__ == '__main__':
    n, text, k = input(), input().split(' '), input()
    print(iter_or_iter(int(n), text, int(k)))
