#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.11.19
@author: felix
"""
import operator

MATHOPERATORS = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'floordiv'
}


def input_prob(x: int, k: int, polyn: str) -> bool:
    tmp = polyn.replace('x', str(x)).split(' ')
    for i, t in enumerate(tmp):
        if '**' in t:
            a, b = t.split('**')
            tmp[i] = operator.pow(int(a), int(b))
        else:
            try:
                tmp[i] = int(t)
            except (ValueError, TypeError):
                pass
    while len(tmp) > 1:
        for i, x in enumerate(tmp):
            if x in MATHOPERATORS.keys():
                b, x, a = tmp.pop(i + 1), tmp.pop(i), tmp[0]
                tmp[0] = getattr(operator, MATHOPERATORS[x])(int(a), int(b))
    return tmp[0] == k


if __name__ == '__main__':
    # x**3 + x**2 + x + 1
    x, k = [int(i) for i in input().strip().split()]
    polyn = input()
    print(input_prob(x, k, polyn))
