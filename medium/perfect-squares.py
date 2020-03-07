#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


def perfect_squares(n):
    """
    给定一个正整数n，请找到和为n的最小的平方的数量。例如n = 13，和为n的最小平方的数量为2，13 = 4 + 9。
    :param n: int
    :return: int
    """
    # 该种方法参考 https://blog.csdn.net/qq_35481167/article/details/82817699
    def is_square(m):
        k = int(sqrt(m))
        return k*k == m

    while n % 4 == 0:
        n = n / 4

    if n % 8 == 7:
        return 4
    if is_square(n):
        return 1

    for i in reversed(range(1, int(sqrt(n))+1)):
        if is_square(n - i*i):
            return 2

    return 3


# 动态规划
def perfect_squares1(n):
    if n == 0:
        return 0
    output = [float('inf')] * (n + 1)
    output[0] = 0
    output[1] = 1
    for i in range(2, n+1):
        j = 1
        while j*j <= i:
            output[i] = min(output[i], output[i - j*j] + 1)
            j += 1

    return output[n]


# leetcode 会TLE
def perfect_squares2(n):
    dp = [float("inf")] * (n+1)
    dp[0] = 0
    for i in range(n+1):
        for j in range(1, n+1):
            if i + j*j <= n:
                dp[i + j*j] = min(dp[i + j*j], dp[i] + 1)
            else:
                break
    return dp[-1]


if __name__ == "__main__":
    n = 6665
    print(perfect_squares1(n))