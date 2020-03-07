#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubble_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if not nums or len(nums) == 1:
        return nums
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                nums[j] = nums[j] ^ nums[j + 1]
                nums[j + 1] = nums[j] ^ nums[j + 1]
                nums[j] = nums[j] ^ nums[j + 1]
    return nums

if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2]
    print(bubble_sort(nums))