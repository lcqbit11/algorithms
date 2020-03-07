#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverseBits(n):
    """
    对于给定的32位无符号整型的bit位进行翻转。
    :param n: int
    :return: int
    """
    res = 0
    mask = 1
    for i in range(32):
        res <<= 1
        if mask & n:
            res |= 1
        n >>= 1
    return res


if __name__ == "__main__":
    # n = 00000010100101000001111010011100
    n = 1312424
    print(reverseBits(n))