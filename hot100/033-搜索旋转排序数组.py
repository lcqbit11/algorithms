#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
# nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


from audioop import mul
from ctypes.wintypes import tagMSG


def search(nums, target):
    if not nums:
        return -1
    
    low , high = 0, len(nums) -1
    while low <= high:
        middle = (low + high) // 2
        if target == nums[middle]:
            return middle
        
        if nums[middle] >= nums[low]:
            if nums[middle] > target and nums[low] <= target:
                high = middle - 1
            else:
                low = middle + 1
        else:
            if nums[middle] < target and nums[high] >= target:
                low = middle + 1
            else:
                high = middle - 1

    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))
