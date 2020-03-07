#!/usr/bin/env python
# -*- coding: utf-8 -*-


def findKMax(nums, k, low, high):
    """
    找到无序数组nums中，按照从大到小排序的第k大的数字。
    :param nums: List(int)
    :param k: int
    :return: int
    """
    def partition_big2small(nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] <= pivot:
                high -= 1
            nums[low] = nums[high]
            
            while low < high and nums[low] >= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    if not nums:
        return -1
    if low < high:
        temp = partition_big2small(nums, low, high)
        if temp + 1 == k:
            return nums[temp]
        elif temp + 1 > k:
            return findKMax(nums, k, low, high - 1)
        else:
            return findKMax(nums, k, low + 1, high)
    else:
        return -1


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 5]
    k = 1
    low, high = 0, len(nums) - 1
    print(findKMax(nums, k, low, high))