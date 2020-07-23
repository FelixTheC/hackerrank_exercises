#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 26.06.20
@author: felix
"""
from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    n, m = [int(i.strip()) for i in input().split()]
    for i in range(n):
        d['n'].append(input())
    for i in range(m):
        d['m'].append(input())

    for val in d['m']:
        if val in d['n']:
            print(' '.join([str(i) for i, k in enumerate(d["n"], start=1) if k == val]))
        else:
            print(-1)
            continue
