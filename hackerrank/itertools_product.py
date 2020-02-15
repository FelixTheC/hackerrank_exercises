#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from itertools import product


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    b = [int(i) for i in input().strip().split()]
    print(' '.join([f'{prod}' for prod in product(a, b)]))
