#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.05.20
@author: felix
"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    def get_diagonal(arr: list, start: int, end: int):
        if end > 0:
            return sum([arr[i][i] for i in range(end)])
        else:
            ranged = list(reversed(range(start)))
            return sum([arr[j][i] for i, j in zip(ranged, range(start))])
    return abs(get_diagonal(arr, 0, len(arr)) - get_diagonal(arr, len(arr), 0))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
