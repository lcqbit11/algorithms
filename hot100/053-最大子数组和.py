#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。#


def maxSubArray(nums):
    if not nums:
        return 0
    
    res = nums[0]
    sum_max = 0
    for i in range(len(nums)):
        if sum_max <= 0:
            sum_max = nums[i]
        else:
            sum_max += nums[i]
        res = res if res > sum_max else sum_max
    return res


# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(maxSubArray(nums))
