#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""


def is_superset(set_a: set, set_b: set) -> bool:
    return set_a.issuperset(set_b)


if __name__ == '__main__':
    super_set = set(input().rstrip().split())
    n = int(input().rstrip())

    print(all(is_superset(super_set, set(input().rstrip().split())) for _ in range(n)))
