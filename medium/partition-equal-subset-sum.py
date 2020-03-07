#!/usr/bin/env python
# -*- coding: utf-8 -*-


def partition_equal_subset_sum(nums):
    """
    给定一个非空的正整数数组，请判断是否能将该数组分成两个子数组，且两个子数组各自元素的加和相等。
    :param nums: List[int]
    :return: bool
    """
    if not nums:
        return False
    s = sum(nums)
    if s % 2 > 0:
        return False

    n = int(s / 2)
    dp = [False] * (n + 1)  # dp[i]表示是否有元素加和为i的情况发生
    dp[0] = True
    for num in nums:
        for i in reversed(range(num, n + 1)):  # 如果是正序的话，则将一个元素使用了多次，不符合题意
            dp[i] = dp[i] | dp[i - num]

    return dp[n]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(partition_equal_subset_sum(nums))