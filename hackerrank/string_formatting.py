#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.10.19
@author: felix
"""


def print_formatted(num: int) -> None:
    width = len(f'{num:b}') + 1
    for i in range(1, num + 1):
        deci = f'{i:d}'
        octa = f'{i:o}'
        hexa = f'{i:x}'.upper()
        bina = f'{i:b}'
        print(f'{deci:>{width - 1}}{octa:>{width}}{hexa:>{width}}{bina:>{width}}')


if __name__ == '__main__':
    print_formatted(17)
    """
     1  1  1  1
     2  2  2 10
    """
