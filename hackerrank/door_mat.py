#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 02.11.19
@author: felix
"""
import operator

"""
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""


def helper(n: int, m: int, *, operation: str, sc: int) -> list:
    symbol = '.|.'
    str_list = []
    for i in range(n // 2):
        tmp = ''.join(['-' for _ in range((m - (len(symbol) * sc)) // 2)])
        tmp += symbol * sc
        tmp += ''.join(['-' for _ in range((m - (len(symbol) * sc)) // 2)])
        str_list.append(tmp + '\n')
        sc = getattr(operator, operation)(sc, 2)
    return str_list


def design_door_mat(n: int, m: int) -> str:
    sign = 'WELCOME'
    mat = []
    mat.extend(helper(n, m, operation='add', sc=1))
    middle = ''.join(['-' for _ in range((m - len(sign) * 1) // 2)])
    middle += sign
    middle += ''.join(['-' for _ in range((m - len(sign) * 1) // 2)])
    mat.append(middle + '\n')
    mat.extend(helper(n, m, operation='sub', sc=n - 2))
    return ''.join(mat)


if __name__ == '__main__':
    x, y = input().split(' ')
    print(design_door_mat(int(x), int(y)))
