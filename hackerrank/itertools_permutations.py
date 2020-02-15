#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from itertools import permutations


if __name__ == '__main__':
    text, num = input().strip().split()
    for per in sorted(permutations(text, int(num))):
        print(''.join(per))
