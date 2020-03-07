#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sqrt_compute(x):
    """
    给定一个非负整数x，计算x的开方值，并返回一个整数，如果返回的是小数值，那么将小数部分截断，只保留整数部分。
    :param x: float
    :return: float
    """
    # 牛顿法
    if x == 0:
        return x
    k = x / 2.0
    while 1:
        k = (k + x / k) / 2.0
        if pow(int(k), 2) <= x and pow(int(k) + 1, 2) > x:
            return int(k)


def sqrt_compute1(x):
    left, right = 0, x
    while left < right:
        mid = (left + right) // 2
        if mid * mid < x:
            left = mid + 1
        else:
            right = mid
    return right-1


if __name__ == "__main__":
    x = 1040
    print(sqrt_compute1(x))