#!/usr/env/env python
# -*- coding: utf-8 -*-


def removeDuplicates(nums):
    """
    给定一个有序数组，去除数组中的重复元素，按原来的顺序保留所有非重复的元素。
    :param nums: List[int]
    :return int: List[int]
    """
    low = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[low]:
            low = low+1
            nums[low] = nums[i]

    return low+1


def removeDuplicates1(nums):
    k = float('inf')
    i = 0
    while i < len(nums):
        if k != nums[i]:
            k = nums[i]
            i += 1
        else:
            del nums[i]
    return len(nums)


if __name__ == "__main__":
    # nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 6]
    nums = [1, 1, 2]
    print(removeDuplicates1(nums))