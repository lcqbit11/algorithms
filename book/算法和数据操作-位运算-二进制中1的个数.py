#!/usr/bin/env python
# -*- coding: utf-8 -*-

def one_number_in_bit(n):
    """
    :param n: int
    :return: int
    """
    cnt = 0
    while n>0:
        n = n & (n-1)
        cnt += 1
    return cnt

if __name__ == "__main__":
    n = 11
    print(one_number_in_bit(n))