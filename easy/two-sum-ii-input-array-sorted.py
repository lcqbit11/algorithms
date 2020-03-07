#!/usr/bin/env python
# -*- coding: utf-8 -*-


def two_sum_ii(nums, target):
    """
    数组从小到大已经有序，找出数组中的两个数使得加起来等于目标数字，返回这两个数的下标
    :param nums: List[int]
    :param target: int
    :return: tuple
    """
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left]+nums[right] > target:
            right -= 1
        elif nums[left]+nums[right] < target:
            left += 1
        else:
            return (left + 1, right + 1)


if __name__ == "__main__":
    nums = [2,7,11,15]
    print(two_sum_ii(nums, 9))