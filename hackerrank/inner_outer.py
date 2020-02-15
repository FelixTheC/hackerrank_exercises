#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.11.19
@author: felix
"""

import numpy as np


def inner_outer(x: list, y: list) -> None:
    _a = np.array(x)
    _b = np.array(y)
    print(np.inner(_a, _b))
    print(np.outer(_a, _b))


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    b = [int(i) for i in input().strip().split()]
    inner_outer(a, b)
