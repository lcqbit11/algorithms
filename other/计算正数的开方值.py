#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compute_sqrt(x, precision):
    """
    给定一个非负整数x，计算x的开方值，并返回一个整数，如果。
    :param x: float
    :param precision: float
    :return: float
    """
    if x == 0:
        return x
    k = x / 2.0
    while 1:
        k = (k + x / k) / 2.0
        if (pow(k + precision, 2) - x)*(pow(k, 2) - x) < 0 or (pow(k - precision, 2) - x)*(pow(k, 2) - x) < 0:
            return k


if __name__ == "__main__":
    x = 1024
    precision = 0.01
    print(compute_sqrt(x, precision))