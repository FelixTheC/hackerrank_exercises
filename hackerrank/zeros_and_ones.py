#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 01.12.19
@author: felix
"""
import numpy as np


if __name__ == '__main__':
    shape = tuple([int(i) for i in input() if i != ' '])
    dtype = np.int
    print(np.zeros((shape), dtype=dtype))
    print(np.ones((shape), dtype=dtype))
