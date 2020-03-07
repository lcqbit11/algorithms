#!/usr/bin/env python
# -*- coding: utf-8 -*-


def coin_change_2(nums, target):
    """
    给定不同面值的硬币(假设每种面值的硬币都有无限多个)和一个总金额，请计算出有多少种组合方式可以组成该总金额。
    :param nums: List[int]
    :param target: int
    :return: int
    """
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]

    return dp[target]


if __name__ == "__main__":
    nums = [1, 2, 5]
    target = 5
    print(coin_change_2(nums, target))