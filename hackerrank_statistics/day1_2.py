#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.02.20
@author: felix
"""
from statistics import pstdev


def main(array: list) -> str:
    return f'{pstdev(array):.1f}'


if __name__ == '__main__':
    _ = input()
    arr = [int(v) for v in input().split()]
    print(main(arr))
