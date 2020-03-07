#!/usr/bin/env python
# -*- coding: utf-8 -*-


def move_zeros(nums):
    """
    将数组中的0值移到数组的最后，并保持非0元素的顺序不变
    :param nums: List[int]
    :return: List[int]
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    while k < len(nums):
        nums[k] = 0
        k += 1

    return nums


if __name__ == "__main__":
    nums = [0,1,0,3,12,12,3,0,1,0,0]
    print(move_zeros(nums))