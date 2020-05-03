#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 03.05.20
@author: felix
"""


def camelcase(s: str):
    return 1 + sum([1 for char in s if char.isupper()])


if __name__ == '__main__':
    print(camelcase('saveChangesInTheEditor') == 5)
