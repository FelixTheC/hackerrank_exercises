#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.11.19
@author: felix
"""


def check_for_exceptions(x: str, y: str) -> None:
    try:
        print(int(x) // int(y))
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')


if __name__ == '__main__':
    t = int(input())
    values = [input().strip().split() for x in range(t)]
    [check_for_exceptions(*v) for v in values]
