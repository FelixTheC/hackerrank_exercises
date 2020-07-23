#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 22.07.20
@author: felix
"""
import datetime

WEEKDAYS = {
    0: 'MONDAY',
    1: 'TUESDAY',
    2: 'WEDNESDAY',
    3: 'THURSDAY',
    4: 'FRIDAY',
    5: 'SATURDAY',
    6: 'SUNDAY',
}


def main(month: str, day: str, year: str):
    day = int(day[1]) if day.startswith('0') else int(day)
    month = int(month[1]) if month.startswith('0') else int(month)
    year = int(year)
    dt = datetime.datetime(year=year, month=month, day=day)
    print(WEEKDAYS[dt.weekday()])


if __name__ == '__main__':
    mm, dd, yyyy = input().split()
    main(mm, dd, yyyy)
