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

# Complete the staircase function below.
def staircase(n):
    arr = [' ' for _ in range(n - 1)]
    for i in range(1, n):
        arr[-i] = '#'
        print(''.join(arr))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
