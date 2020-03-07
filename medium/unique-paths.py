#!/usr/bin/env python
# -*- coding: utf-8 -*-


def unique_paths(m, n):
    """
    给定一个m*n的网格，一个机器人的初始位置在左上方格子，机器人每次只能向右或者向下移动一个格子，
    那么机器人从左上方格子移动到右下方格子，有多少种不同的走法
    :param m: int
    :param n: int
    :return: int
    """
    nums = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            nums[j] += nums[j-1]

    return int(nums[n-1])

    # def fun(n1, n2):
    #     if n1 == 0 or n2 == 0:
    #         return 0
    #     if n1 == 1 or n2 == 1:
    #         return 1
    #     return fun(n1-1, n2) + fun(n1, n2-1)
    #
    # return fun(m, n)


if __name__ == "__main__":
    m = 7
    n = 3
    print(unique_paths(m, n))