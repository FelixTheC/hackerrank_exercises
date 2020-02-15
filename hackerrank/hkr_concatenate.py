#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 01.12.19
@author: felix
"""
import numpy as np


if __name__ == '__main__':
    lists_n = []
    lists_m = []
    n, m, p = input().split(' ')
    for i in range(int(n)):
        lists_n.append([int(i) for i in input() if i != ' '])
    for i in range(int(m)):
        lists_m.append([int(i) for i in input() if i != ' '])
    print(np.concatenate((lists_n, lists_m)))
