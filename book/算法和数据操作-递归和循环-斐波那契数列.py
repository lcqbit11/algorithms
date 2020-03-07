#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci_sequence(n):
    """
    :param n: int
    :return: int
    [[1, 1]
     [1, 0]]
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a+b

    return b

if __name__ == "__main__":
    n = 5000
    print(fibonacci_sequence(n))