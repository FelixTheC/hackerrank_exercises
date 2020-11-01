#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""


def modify_set(set_obj: set) -> None:
    attr, times = input().rstrip().split()
    values = set(int(val) for val in input().rstrip().split())

    getattr(set_obj, attr)(values)


if __name__ == '__main__':
    init_values = input().rstrip()
    my_set = set(int(val) for val in input().rstrip().split())

    modifications = int(input().rstrip())
    for modifcation in range(modifications):
        modify_set(my_set)

    print(sum(my_set))
