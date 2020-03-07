#!/usr/bin/env python
# -*- coding: utf-8 -*-

def direct_insert_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if not nums or len(nums) == 1:
        return nums
    for i in range(1, len(nums)):
        index = i
        for j in reversed(range(0, i)):
            if nums[index] < nums[j]:
                nums[index] = nums[index] ^ nums[j]
                nums[j] = nums[index] ^ nums[j]
                nums[index] = nums[index] ^ nums[j]
                index -= 1
    return nums

if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2]
    print(direct_insert_sort(nums))