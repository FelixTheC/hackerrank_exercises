#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.07.20
@author: felix
"""
import math


class Points:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, other):
        return Points(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        return Points((self.y * other.z) - (self.z * other.y),
                      (self.z * other.x) - (self.x * other.z),
                      (self.x * other.y) - (self.y * other.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'


if __name__ == '__main__':
    points = [list(map(float, input().split())) for i in range(4)]

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print(f'{math.degrees(angle):.2f}')
