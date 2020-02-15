#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.02.20
@author: felix
"""


from collections import Counter
from typing import List, Tuple, Union


def in_stock(stock: List[str]):
    stocks = Counter(stock)
    result = 0
    while True:
        p = yield
        val = stocks.get(p[0], None)
        if val is not None and val > 0:
            result += int(p[1])
            stocks[p[0]] -= 1
        else:
            result += 0
        yield result


def main(stock: List[str], purchase: List[Union[Tuple[str], Tuple[str]]]) -> int:
    in_stock_corro = in_stock(stock)
    in_stock_corro.__next__()
    total = 0
    for i in purchase:
        total = in_stock_corro.send(i)
        in_stock_corro.send(0)
    return total


if __name__ == '__main__':
    lenght_list = int(input())
    stock_list = [i for i in input().split(' ')]
    purchase_lenght = int(input())
    purchase_list = []
    for _ in range(purchase_lenght):
        i = input().split(' ')
        purchase_list.append(tuple(i))
    print(main(stock_list, purchase_list))
