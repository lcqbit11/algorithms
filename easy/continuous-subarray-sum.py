#!/usr/bin/env python
# -*- coding: utf-8 -*-


def continuous_subarray_sum(nums, target):
    """
    给定一个非负数组和一个正数目标值k，请判断数组中是否存在一个连续的子数组，其加和为k的整数倍，
    即其加和等于n*k，其中n也为一个整数。
    :param nums: List[int]
    :param target: int
    :return: bool
    """
    # Solu1
    # if not nums or len(nums) < 2:
    #     return False
    # l = len(nums)
    # for i in range(l - 1):
    #     tmp = nums[i]
    #     for j in range(i + 1, l):
    #         tmp += nums[j]
    #         if k == tmp:
    #             return True
    #         if k and not tmp % k:
    #             return True
    # return False

    # Solu2
    if not nums or len(nums) < 2:
        return False
    l = len(nums)
    tmp = 0
    m = {0: -1}
    for i in range(l):
        tmp += nums[i]
        t = tmp % k if k else tmp
        if t in m:
            if i - m[t] > 1:
                return True
        else:
            m[t] = i
    return False


if __name__ == "__main__":
    # nums = [23, 2, 4, 6, 7]
    # k = 6
    nums = [0, 1, 0]
    k = 0
    print(continuous_subarray_sum(nums, target=k))