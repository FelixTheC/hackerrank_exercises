#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 01.12.19
@author: felix
"""
import numpy as np

if __name__ == '__main__':
    n, m = input().split(' ')
    np.set_printoptions(legacy='1.13')
    print(np.eye(int(n), int(m), 0))
