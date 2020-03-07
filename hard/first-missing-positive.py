#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def first_missing_positive(nums):
    """
    给定一个无序的整型数组，找出第一个缺失的正整数，
    例如[1,2,0] 缺少的第一个正整数就是3；而[3,4,-1,1] 缺少的第一个正整数就是2.
    :param nums: List[int]
    :return: int
    """
    n = len(nums)
    for i in range(n):
        while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1

if __name__ == "__main__":
    nums = [2, 1]

    print(first_missing_positive(nums))




