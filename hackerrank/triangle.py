#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.07.20
@author: felix
"""

if __name__ == '__main__':
    for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also. No str
        print(f'10**(i) = {10**(i)}')
        print(f'(10**(i)//9) = {(10**(i)//9)}')
        print(f'result: {(10**(i)//9)*i}')
