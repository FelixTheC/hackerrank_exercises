#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.10.19
@author: felix
"""
import gc
import sys
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
t_results = []


def solve(s):
    result = []
    for c in s.split(' '):
        if len(c) > 0:
            if not c[0].isnumeric():
                result.append(c.title())
                continue
        result.append(c)
    return ' '.join(result)


if __name__ == '__main__':
    print(solve('132 456 Wq  m e'))
