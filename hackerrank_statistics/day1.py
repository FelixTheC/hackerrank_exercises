#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.02.20
@author: felix
"""
from statistics import median


def main(array: list):
    m = len(array) // 2 if len(array) % 2 == 0 else (len(array) // 2) + 1
    lower = array[:m]
    upper = array[m:]
    q1 = median(sorted(lower))
    q3 = median(sorted(upper))
    return f'{q3 - q1:.1f}'


if __name__ == '__main__':
    x = input()
    arr = []
    arr_dict = {i: int(v) for i, v in enumerate(input().split())}
    for i, v in enumerate(input().split()):
        arr.extend([arr_dict[i] for _ in range(int(v))])
    print(main(sorted(arr)))
