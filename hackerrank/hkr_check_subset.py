#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""


def is_subset(set_a: set, set_b: set) -> bool:
    return len(set_a.difference(set_b)) == 0


if __name__ == '__main__':
    cases = int(input().rstrip())
    for _ in range(cases):
        n = int(input().rstrip())
        x = set(int(val) for val in input().rstrip().split())

        m = int(input().rstrip())
        y = set(int(val) for val in input().rstrip().split())

        print(is_subset(x, y))
