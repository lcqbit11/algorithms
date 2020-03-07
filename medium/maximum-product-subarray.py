#!/usr/bin/env python
# -*- coding: utf-8 -*-


def maximum_product_sub_array(nums):
    """
    给定一个整数数组，找到连续的子数组（至少包含一个数值），使得子数组内的所有数字的乘积最大。
    解法：找到以当前元素为结尾的子数组的乘积最大值和最小值
    :param nums: List[int]
    :return: int
    """
    max_merge = [0] * len(nums)
    min_merge = [0] * len(nums)
    max_merge[0] = nums[0]
    min_merge[0] = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        max_merge[i] = max(max_merge[i-1] * nums[i], nums[i], min_merge[i-1] * nums[i])
        min_merge[i] = min(max_merge[i-1] * nums[i], nums[i], min_merge[i-1] * nums[i])
        res = max(res, max_merge[i])

    return res


def maximum_product_sub_array1(nums):
    max_merge = min_merge = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        tmp = max(max_merge * nums[i], nums[i], min_merge * nums[i])
        min_merge = min(max_merge * nums[i], nums[i], min_merge * nums[i])
        max_merge = tmp
        res = max(res, max_merge)
    return res


if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(maximum_product_sub_array1(nums))