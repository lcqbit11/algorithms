#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def lengthOfLIS(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)


def lengthOfLIS_2(nums):
    if not nums:
        return 0
    
    dp = []
    for n in nums:
        if not dp or n > dp[-1]:
            dp.append(n)
        else:
            low = 0
            high = len(dp) - 1
            loc = high
            while low <= high:
                mid = (low + high) // 2
                if dp[mid] >= n:
                    loc = mid
                    high = mid - 1
                else:
                    low = mid + 1
            dp[loc] = n

    return len(dp)


def lengthOfLIS_3(nums):
    if not nums:
        return 0
    
    dp = []
    for ele in nums:
        if not dp or ele > dp[-1]:
            dp.append(ele)
        else:
            low, high = 0, len(dp)-1
            while low < high:
                mid = (low + high) // 2
                if dp[mid] < ele:
                    low = mid + 1
                else:
                    high = mid
            dp[low] = ele
    
    return len(dp)


nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS_3(nums))
