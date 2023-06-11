#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-the-duplicate-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def findDuplicate(nums):
    if not nums:
        return
    
    slow = 0
    fast = 0
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    p = 0
    while p != slow:
        p = nums[p]
        slow = nums[slow]

    return slow


# nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(findDuplicate(nums))
