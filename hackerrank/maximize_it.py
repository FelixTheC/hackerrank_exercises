#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.11.19
@author: felix
"""
import itertools


if __name__ == '__main__':
    k, m = input().strip().split()
    elements = []
    for _ in range(int(k)):
        elements.append([int(i)**2 for i in input().strip().split()[1:]])
    products = itertools.product(*elements)
    print(max([sum(i) % int(m) for i in products]))
