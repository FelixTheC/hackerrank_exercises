#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 30.09.20
@author: felix
"""
from typing import List


def get_happiness(n: set, m: List[set]):
    return len(n & m[0]) - sum(len(n & m[i]) for i in range(1, len(m)))


if __name__ == '__main__':
    n_length, m_length = [int(char.strip()) for char in input().strip().split()]
    n_a = set([int(char.strip()) for char in input().strip().split()])
    m_a = []
    for i in range(m_length):
        m_a.append(set([int(char.strip()) for char in input().strip().split()]))
    print(get_happiness(n_a, m_a))
