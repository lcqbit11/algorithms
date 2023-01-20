#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
# 你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def threeSum(nums):
    if len(nums) < 3:
        return
    nums.sort()
    res = []
    l = len(nums)
    for i in range(l):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        left, right = i + 1, l - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
