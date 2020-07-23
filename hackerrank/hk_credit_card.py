#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 22.07.20
@author: felix
"""
import re

NUM_PATTERN = r'[0-9]'
ALLOWED_PATTERN = r'[0-9-]'


def cd_first_num_valid(card_number: str) -> bool:
    return card_number.startswith('4') or card_number.startswith('5') or card_number.startswith('6')


def cd_len_match(card_number: str) -> bool:
    numbers = re.findall(NUM_PATTERN, card_number)
    return len(numbers) == 16


def cd_groups_of_4(card_number: str) -> bool:
    if '-' in card_number:
        groups = card_number.split('-')
        return all(len(nums) == 4 for nums in groups) and len(groups) == 4
    return True


def cd_only_valid_chars(card_number: str) -> bool:
    return len([i for i in re.split(ALLOWED_PATTERN, card_number) if i]) == 0


def cd_repeated_digits(card_number: str) -> bool:
    results = []
    if '-' in card_number:
        card_number = card_number.replace('-', '')
    for i in range(len(card_number)):
        nums = card_number[i: i + 4]
        results.append(len(nums) - len(set(nums)) < 3)
    return all(results)


functions = [(name, func) for name, func in vars().items() if name.startswith('cd')]


def main(card_number: str) -> None:
    valid = all(func[1](card_number) for func in functions)
    if valid:
        print('Valid')
    else:
        print('Invalid')


if __name__ == '__main__':
    for number in [input().strip() for _ in range(int(input()))]:
        main(number)
