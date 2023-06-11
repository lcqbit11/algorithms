#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# #


def searchRange(nums, target):
    if not nums:
        return (-1, -1)
    first = last = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left += 1
        elif nums[middle] > target:
            right -= 1
        else:
            first = middle
            right = middle - 1
    
    if first == -1:
        return (-1, -1)
    
    left = first
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right -= 1
        else:
            last = middle
            left = middle + 1
    
    return (first, last)


nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))
