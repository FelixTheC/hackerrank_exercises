#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 06.07.20
@author: felix
"""

test_cases = """
2
6
4 3 2 1 3 4 <- Yes
3
1 3 2 <- No
"""
"""
  21
 3  3
4    4
"""
"""
  
 3
1 2
"""


def is_stackable():
    pass

"""
3
427731488 922935208 973233245 <- Yes
"""

if __name__ == '__main__':
    cases = int(input().rstrip())
    for _ in range(cases):
        n = int(input().rstrip())
        m = set(input().rstrip().split(' '))
        if n % 2 == 0 and len(m) > 1:
            print('Yes')
        else:
            print('No')
