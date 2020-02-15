#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from itertools import combinations_with_replacement as combinations


if __name__ == '__main__':
    text, num = input().strip().split()
    combis = sorted([sorted(x) for x in combinations(text, int(num))])
    for per in combis:
        end = '' if per == combis[-1] else '\n'
        print(''.join(per), end=end)
