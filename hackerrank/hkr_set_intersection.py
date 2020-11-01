#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""


def get_input() -> set:
    _ = int(input().rstrip())
    set_input = set(val for val in input().rstrip().split())

    return set_input


if __name__ == '__main__':
    set_a = get_input()
    set_b = get_input()

    print(len(set_a & set_b))  # intersection
