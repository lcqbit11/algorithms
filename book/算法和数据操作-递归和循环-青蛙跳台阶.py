#!/usr/bin/env python
# -*- coding: utf-8 -*-

def frog_jump_floor(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return frog_jump_floor(n-1) + frog_jump_floor(n-2)

if __name__ == "__main__":
    n = 10
    print(frog_jump_floor(n))