#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.11.19
@author: felix
"""
if __name__ == '__main__':
    n = input().strip()
    print(all([n == n[::-1], all([int(x) > 0 for x in input().strip().split()])]))
