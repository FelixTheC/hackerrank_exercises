#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 17.10.19
@author: felix
"""


def count_substring(string, sub_string):
    count = 0
    length = len(sub_string)
    for i in range(len(string)):
        if string[i: i + length] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    count_substring('ABCDCDC', 'CDC')
