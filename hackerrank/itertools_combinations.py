#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from itertools import combinations


if __name__ == '__main__':
    text, num = input().strip().split()
    for i in range(1, int(num) + 1):
        combis = sorted([sorted(x) for x in combinations(text, i)])
        for per in combis:
            end = '' if i == int(num) and per == combis[-1] else '\n'
            print(''.join(per), end=end)
