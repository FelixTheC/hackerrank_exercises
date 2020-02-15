#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from typing import List


def compress_str(text: str) -> List[tuple]:
    res = []
    current = text[0]
    count = 0
    for i, char in enumerate(text):
        if current == char:
            count += 1
        else:
            res.append((count, int(current)))
            count = 1
            current = char
        if i == len(text) - 1:
            res.append((count, int(char)))
    return res


if __name__ == '__main__':
    user_text = input()
    print(' '.join([str(i) for i in compress_str(user_text)]))
