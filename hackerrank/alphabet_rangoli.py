#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.10.19
@author: felix
"""
from string import ascii_lowercase


def print_rangoli(size: int) -> None:
    lines = (size * 2) - 2
    letters = [i for i in ascii_lowercase][:size]
    letters_back = letters[::-1]
    text_list = []
    for i in range(size):
        text = ''
        text += f'{"-" * lines}'
        text += '-'.join(letters_back[: i + 1])
        if i > 0:
            text += '-'
            text += '-'.join(letters[size - i:])
        text += f'{"-" * lines}\n'
        text_list.append(text)
        lines -= 2
    result = f"{''.join(text_list)}{''.join(list(reversed(text_list))[1:])}"
    print(result)


if __name__ == '__main__':
    """
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------
    """
    print_rangoli(5)
