#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.10.19
@author: felix
"""


def avg(args):
    return sum(args)/len(args)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    reverse = True if sorted([k for k in student_marks.keys()])[0] == query_name else False
    print(format(avg(student_marks[sorted(student_marks, key=lambda x: x[0], reverse=reverse)[n - 1]]), '.2f'))

