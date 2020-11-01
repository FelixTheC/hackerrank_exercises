#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.10.20
@author: felix
"""

NONE = object()


def modify_set(set_obj: set, attr: str, val=NONE) -> set:
    if val is NONE:
        return getattr(set_obj, attr)()
    else:
        return getattr(set_obj, attr)(int(val))


if __name__ == '__main__':
    my_set = set()

    x = input().rstrip()
    values = input().rstrip().split()
    assert len(values) == int(x)
    [my_set.add(int(val)) for val in values]

    num_calls = int(input().rstrip())
    for _ in range(num_calls):
        modify_set(my_set, *input().rstrip().split())

    print(sum(my_set))
