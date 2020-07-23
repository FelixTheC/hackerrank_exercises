#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 28.06.20
@author: felix
"""
from collections import deque


if __name__ == '__main__':
    d = deque()
    n = int(input().rstrip())
    for _ in range(n):
        user_in = input().rstrip()
        try:
            attr, value = user_in.split()
        except ValueError:
            attr, value = user_in.split()[0], None

        if value is not None:
            getattr(d, attr)(value)
        else:
            getattr(d, attr)()
    for val in d:
        print(val, end=' ')
