#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.02.20
@author: felix
"""
from collections import Counter
from typing import List
import numpy as np


def main(num_list: List[int]):
    print(f'{sum(num_list)/len(num_list):.1f}')
    print(f'{np.median(num_list):.1f}')
    values = Counter(num_list)
    max_occurence = max([i for i in values.values()])
    print(f'{min([k for k, v in values.items() if v == max_occurence])}')


if __name__ == '__main__':
    input_length = int(input())
    numbers = [int(i) for i in input().split()]
    main(numbers)


# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 64630