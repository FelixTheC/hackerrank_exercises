#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""
from collections import Counter


if __name__ == '__main__':
    group_size = int(input().rstrip())
    k = input().rstrip().split()
    c_dict = Counter(k)
    print(sorted(c_dict.items(), key=lambda x: x[1])[0][0])
