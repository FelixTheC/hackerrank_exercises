#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 05.05.20
@author: felix
"""
from cmath import phase
from typing import Union


def polar_corordinates(num: Union[int, float, complex]):
    complex_num = num if isinstance(num, complex) else complex(num, 0.0)
    print(abs(complex_num))
    print(phase(complex_num))


if __name__ == '__main__':
    user_in = input()
    try:
        int(user_in)
    except ValueError:
        user_in = complex(user_in)
    polar_corordinates(user_in)
