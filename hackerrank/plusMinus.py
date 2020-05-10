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

# Complete the plusMinus function below.
def plusMinus(arr):
    total = len(arr)
    positives = sum([1 for i in arr if i > 0]) / total
    negatives = sum([1 for i in arr if i < 0]) / total
    zeros = sum([1 for i in arr if i == 0]) / total
    print(f'{positives:.6f}')
    print(f'{negatives:.6f}')
    print(f'{zeros:.6f}')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
