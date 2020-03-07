#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_1_to_max(n):
    """
    :param n: int
    :return: void
    """
    def can_increase(num):
        jump = 1
        for i in reversed(range(len(num))):
            temp = ord(num[i]) - ord("0") + jump
            jump = int(temp/10)
        if jump == 1:
            return False
        return True

    def number_increase(num):
        jump = 1
        for i in reversed(range(len(num))):
            temp = ord(num[i]) - ord("0") + jump
            num[i] = chr(ord("0") + int(temp % 10))
            jump = int(temp / 10)
        return num

    k = ['0'] * n
    k[n-1] = '1'
    print("".join(k))
    while can_increase(k):
        k = number_increase(k)
        # print("".join(k))

if __name__ == "__main__":
    n = 4
    print_1_to_max(n)