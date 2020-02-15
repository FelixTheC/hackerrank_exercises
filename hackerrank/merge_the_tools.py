#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 20.10.19
@author: felix
"""
from collections import Counter


def merge_the_tools(string, k):
    sub_strings = [string[i: i + k] for i in range(0, len(string), k)]
    for s in sub_strings:
        res = []
        for c in s:
            if c not in res:
                res.append(c)
        print(f'{"".join(res)}')


if __name__ == '__main__':
    merge_the_tools('AABCAAADA', 3)
