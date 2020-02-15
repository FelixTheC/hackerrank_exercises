#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 01.12.19
@author: felix
"""
import re


def fun(s):
    pattern = r'[A-Za-z0-9-_]+[@][A-Za-z0-9]+[.][a-z]{1,3}'
    if re.fullmatch(pattern, s) is not None:
        return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
