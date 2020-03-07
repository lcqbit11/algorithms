#!/usr/bin/env python
# -*- coding: utf-8 -*-

def power_value(a, b):
    """
    :param a: float
    :param b: float
    :return: float
    """
    if a == 0:
        return 0
    if b == 0:
        return 1
    if b == 1:
        return a
    if b == 2:
        return a*a
    temp = b
    if b < 0:
        b = -b
    result = 1
    if b%2 == 0:
        result = power_value(a, b/2)*power_value(a, b/2)
    else:
        result = power_value(a, (b-1)/2)*power_value(a, (b-1)/2)*a
    if temp < 0:
        result = 1/result
    return result


    if a == 0:
        return 0
    if b == 0:
        return 1
    result = 1
    temp = b
    if b < 0:
        b = -b
    while b > 0:
        result *= a
        b -= 1
    if temp < 0:
        result = 1/result
    return result

if __name__ == "__main__":
    a, b = 3, 98
    print(power_value(a, b))