#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bitwise_and_of_numbers_range(m, n):
    """
    给定[m, n]之间的整数，请计算其中所有数之间按位做 AND 逻辑运算的结果。
    解法：找到m和n的公共前缀的bit
    :param m: int
    :param n: int
    :return: int
    """
    index = 0
    while m != n:
        m = m >> 1
        n = n >> 1
        index += 1

    return n << index


def bitwise_and_of_numbers_range1(m, n):
    while m < n:
        n = n & (n-1)
    return n


if __name__ == "__main__":
    m, n = 5, 7
    print(bitwise_and_of_numbers_range1(m, n))