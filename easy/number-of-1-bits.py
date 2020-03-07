#!/usr/bin/env python
# -*- coding: utf-8 -*-


def number1Bits1(n):
    res = 0
    while n > 0:
        res += n&1
        n = n >> 1
    return res


def number1Bits(n):
    """
    对一个无符号的整型，返回其二进制包含的 1 的个数
    :param n:
    :return number:
    """
    res = 0
    while n > 0:
        n = n & (n-1)
        res += 1
    return res


if __name__ == "__main__":
    n = 8887
    print(number1Bits1(n))
    print(2 >> 1)