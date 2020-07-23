#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 27.06.20
@author: felix
"""

from collections import OrderedDict
from typing import Union


def prepare_item_for_dict(item: list):
    if len(item) == 2:
        return item[0], int(item[1])
    return ' '.join(item[:-1]), int(item[-1])


def add_item_to_dict(d: OrderedDict, item: Union[tuple, list]):
    if item[0] in d:
        d[item[0]] += item[1]
    else:
        d[item[0]] = item[1]


if __name__ == '__main__':
    d = OrderedDict()
    n = int(input().rstrip())
    [add_item_to_dict(d, prepare_item_for_dict(item)) for item in [input().strip().split() for _ in range(n)]]
    for key, val in d.items():
        print(key, val)
