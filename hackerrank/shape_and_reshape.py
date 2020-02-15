#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 01.12.19
@author: felix
"""

import numpy as np


def my_reshape(l: list) -> np.array:
    np_array = np.array(l)
    return np.reshape(np_array, (3, 3))


if __name__ == '__main__':
    data = [int(i) for i in input() if i != ' ']
    print(my_reshape(data))
