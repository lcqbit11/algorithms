#!/usr/bin/env python
# -*- coding: utf-8 -*-


def target_sum(nums, S):
    """
    给定一个非负整数数组和一个目标值，现在有两个可选的符号'+'和'-'，对于每一个整数，你可以从中选择一个作为其符号。
    请找出有多少种分配符号的方式使得整数的加和等于目标值。
    :param nums: List[int]
    :param S: int
    :return: int
    """
    # 该函数是从数组中找到加和等于target的子数组的数量
    def find_target_sum(nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in reversed(range(num, target + 1)):
                dp[i] += dp[i - num]
        return dp[target]

    sum_s = sum(nums)
    return 0 if sum_s < S or int((sum_s + S) % 2) != 0 else find_target_sum(nums, int((sum_s + S) / 2))


def target_sum1(nums, S):
    if not nums:
        return 0
    sum_s = sum(nums)
    if sum_s < S or int((sum_s + S) % 2) > 0:
        return 0
    target = int((sum_s + S) / 2)
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in reversed(range(num, target+1)):
            dp[i] += dp[i - num]
    return dp[target]


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    s = 3
    print(target_sum(nums, s))