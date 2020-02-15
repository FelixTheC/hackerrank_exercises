#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.02.20
@author: felix
"""
from typing import List


def main(w: List[int], x: List[int]):
    w_sum = sum([i * j for i, j in zip(w, x)])
    return f'{(w_sum/sum(x)):.1f}'


if __name__ == '__main__':
    input_length = int(input())
    numbers_w = [int(i) for i in input().split()]
    numbers_x = [int(j) for j in input().split()]
    print(main(numbers_w, numbers_x))
