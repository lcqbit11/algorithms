#!/usr/bin/env python
# -*- coding: utf-8 -*-


def intersectionTwoArrays(nums1, nums2):
    """
    给定两个数组，输出两个数组的交集
    :param nums1: List[int]
    :param nums2: List[int]
    :return: List[int]
    """
    nums = []
    m = {}
    for num1 in nums1:
        if num1 not in m:
            m[num1] = 1
        else:
            m[num1] += 1

    for num2 in nums2:
        if num2 in m:
            nums.append(num2)
            del m[num2]

    return nums


if __name__ == "__main__":
    nums1 = [4,9,5,5]
    nums2 = [9,4,9,8,4]
    print(intersectionTwoArrays(nums1, nums2))