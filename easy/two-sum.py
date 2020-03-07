#!/usr/bin/env python
# -*- coding: utf-8 -*-


def two_sum(nums, target):
    """
    给定一个整数数组，请找出数组中两个数字加起来的和等于目标数值，并且返回这两个数字的下标。
    注意：假设结果只有一种可能性，并且只能使用相同下表的数字最多1次。
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    m = {}
    l = len(nums)
    for i in range(l):
        tmp = target - nums[i]
        if tmp in m and m[tmp] != i:
            return [m[tmp], i] if m[tmp] < i else [i, m[tmp]]
        else:
            m[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))