#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.05.20
@author: felix
"""
import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    if s[-2:].lower() == 'pm' and int(s[:2]) < 12:
        return f'{int(s[:2]) + 12}{s[2:-2]}'
    elif s[-2:].lower() == 'pm' and int(s[:2]) == 12:
        return s[:-2]
    if s[-2:].lower() == 'am' and int(s[:2]) == 12:
        return f'00{s[2:-2]}'
    else:
        return s[:-2]


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)
