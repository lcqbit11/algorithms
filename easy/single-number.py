#!/usr/bin/env python
# -*- coding: utf-8 -*-


def singleNumber(nums):
    """
    数组中只有一个数字出现了1次，其他数字均出现了两次，找出这个只出现了一次的数字
    :param nums: List[int]
    :return: int
    """
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]


if __name__ == "__main__":
    nums = [2, 4, 1, 4, 2, 6, 6]
    print(singleNumber(nums))