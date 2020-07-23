#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 26.06.20
@author: felix
"""
from collections import namedtuple

if __name__ == '__main__':
    students = []
    total = int(input().rstrip())
    student = namedtuple('student', input().split())
    [students.append(student(*input().split())) for i in range(total)]
    print(sum(int(s.MARKS) for s in students) / total)
