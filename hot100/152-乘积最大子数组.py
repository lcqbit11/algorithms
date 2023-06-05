#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

# 测试用例的答案是一个 32-位 整数。

# 子数组 是数组的连续子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def maxProduct(nums):
    if not nums:
        return 
    
    min_val = max_val = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        tmp = max(max_val*nums[i], nums[i], min_val*nums[i])
        min_val = min(max_val*nums[i], nums[i], min_val*nums[i])
        max_val = tmp
        res = max(res, max_val)
    
    return res


nums = [2,3,-2,4]
print(maxProduct(nums))
