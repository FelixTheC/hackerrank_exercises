#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""

if __name__ == '__main__':
    my_set = set()

    limit = int(input())
    for _ in range(limit):
        my_set.add(input())

    print(len(my_set))
