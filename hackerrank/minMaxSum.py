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

# Complete the miniMaxSum function below.
from itertools import combinations


def miniMaxSum(arr):
    minMax = [sum(i) for i in list(combinations(arr, len(arr) - 1))]
    print(min(minMax), max(minMax))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
