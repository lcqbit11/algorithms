#!/usr/bin/env python
# -*- coding: utf-8 -*-


def shell_insert_sort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if not nums or len(nums) == 1:
        return nums
    gap = int(len(nums)/3) + 1
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i - gap
            while j > 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = int(gap/3)
    return nums


if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2]
    print(shell_insert_sort(nums))