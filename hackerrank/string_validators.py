#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 17.10.19
@author: felix
"""


def validate_string(string: str):
    results = []
    funcs = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for func in funcs:
        results.append(str(any([getattr(char, func)() for char in string])))
    print('\n'.join(results))


if __name__ == '__main__':
    validate_string('qA2')
