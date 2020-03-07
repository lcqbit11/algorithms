#!/usr/bin/env python
# -*- coding: utf-8 -*-


def product_of_array_except_self(nums):
    length = len(nums)
    l = [1] * length
    r = [1] * length
    res = [1] * length
    for i in range(1, length):
        l[i] = l[i-1] * nums[i-1]
    for i in reversed(range(length-1)):
        r[i] = r[i+1] * nums[i+1]

    for i in range(length):
        res[i] = l[i] * r[i]

    return res


def product_of_array_except_self1(nums):
    """
    给定一个包含n个整数的数组（n>1），请返回一个这样的数组：其中每个元素表示，原始数组中的每个位置除了其自身外的其他元素的乘积
    :param nums: List[int]
    :return: List[int]
    """
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        dp[i] = dp[i-1] * nums[i-1]

    prod = 1
    for i in reversed(range(len(nums) - 1)):
        prod *= nums[i+1]
        dp[i] *= prod

    return dp


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(product_of_array_except_self1(nums))