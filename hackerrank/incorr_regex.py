#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.11.19
@author: felix
"""
import re


def regex_test(patterns: list) -> list:
    test_str = 'lorem IpSUm 123 $"§ \n'
    results = []
    for pattern in patterns:
        try:
            re.match(pattern, test_str)
        except re.error:
            results.append(False)
        else:
            results.append(True)
    return results


if __name__ == '__main__':
    t = int(input())
    patterns = [input() for x in range(t)]
    [print(x) for x in regex_test(patterns)]
