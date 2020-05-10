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

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    compared = [None if x == y else x > y for x, y in zip(a, b)]
    bob = sum([1 for _ in compared if _ is True])
    alice = sum([1 for _ in compared if _ is False])
    return bob, alice


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
