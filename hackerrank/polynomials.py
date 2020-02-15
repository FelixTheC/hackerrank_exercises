#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.11.19
@author: felix
"""

import numpy as np


def polynomials(*, points: list, x: int) -> None:
    print(np.polyval(points, x))


if __name__ == '__main__':
    points_ = [float(i) for i in input().strip().split()]
    x_ = int(input().strip())
    polynomials(points=points_, x=x_)
