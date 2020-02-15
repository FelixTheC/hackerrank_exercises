#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.02.20
@author: felix
"""

def print_standardized_num(num: str) -> None:
    number = num[-10:]
    print(f'+91 {number[:5]} {number[5:]}')


def wrapper(f):
    def fun(l):
        for i in l:
            print_standardized_num(l)
        return fun(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
