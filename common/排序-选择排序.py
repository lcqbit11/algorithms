#!/usr/bin/env python
# -*- coding: utf-8 -*-

def choose_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if not nums and len(nums) == 1:
        return nums
    for i in range(0, len(nums) - 1):
        temp = nums[i]
        index = i
        for j in range(i + 1, len(nums)):
            if temp > nums[j]:
                temp = nums[j]
                index = j
        if index != i:
            nums[i] = nums[i] ^ nums[index]
            nums[index] = nums[i] ^ nums[index]
            nums[i] = nums[i] ^ nums[index]
    return nums

if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2]
    print(choose_sort(nums))