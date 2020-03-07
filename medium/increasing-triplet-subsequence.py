#!/usr/bin/env python
# -*- coding: utf-8 -*-


def increasing_triplet_subsequence(nums):
    """
    给定一个未排序的数组，请判断是否存在一个包含三个元素的严格升序的子数组，请注意：子数组不一定是连续的。
    要求：时间复杂度O(n)，空间复杂度O(1)。
    :param nums: List[int]
    :return: bool
    """
    cur_min = cur_second_min = float("inf")
    for num in nums:
        if num <= cur_min:
            cur_min = num
        elif num <= cur_second_min:
            cur_second_min = num
        else:
            return True
    return False


if __name__ == "__main__":
    nums = [1,1,3,3,3]
    print(increasing_triplet_subsequence(nums))
