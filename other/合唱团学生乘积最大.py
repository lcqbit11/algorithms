#!/usr/bin/env python
# -*- coding: utf-8 -*-

def multi_max(nums, k, d):
    """
    合唱团 N个学生中选K个，相邻两个的位置编号不超过D，使得K个学生乘积最大
    :param nums: List[int]
    :return: int
    """
    n = len(nums)
    maxProduct = [[0] * k] * n  # maxProduct[i][j]表示以第i个人为结尾，合唱团的人数为 j+1 时
    minProduct = [[0] * k] * n
    for i in range(n):
        maxProduct[i][0] = nums[i]
        minProduct[i][0] = nums[i]

    res = float('inf')
    # for i in range(n):
    #     for j in range(k):

