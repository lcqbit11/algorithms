#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binary_insert_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if not nums or len(nums) == 1:
        return nums
    for i in range(1, len(nums)):
        temp = nums[i]
        low = 0
        high = i - 1
        while low <= high:
            middle = int((low + high) / 2)
            if temp < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        for j in reversed(range(low + 1, i + 1)):
            nums[j] = nums[j - 1]
        nums[low] = temp
    return nums


if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2]
    print(binary_insert_sort(nums))