#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 22.11.19
@author: felix
"""

cube = lambda x: x**3


def fibonacci(n: int) -> list:
    results = []
    for i in range(n):
        if i is not None:
            results.append(tmp(i))
    return results


def tmp(m: int) -> int:
    if m <= 1:
        return m
    else:
        return tmp(m - 1) + tmp(m - 2)


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
