#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.11.19
@author: felix
"""
from typing import List

import numpy as np


def linear_algebra(x: List[list]) -> None:
    print(round(np.linalg.det(x), 2))


if __name__ == '__main__':
    n = int(input())
    m = []
    for i in range(n):
        m.append([float(j) for j in input().strip().split()])
    linear_algebra(m)
