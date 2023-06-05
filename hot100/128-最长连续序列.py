#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-consecutive-sequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def longestConsecutive(nums):
    if not nums:
        return 0
    
    d = dict()
    max_len = 0
    for ele in nums:
        if ele not in d:
            left = d.get(ele-1, 0)
            right = d.get(ele+1, 0)

            cur_len = 1 + left + right
            if cur_len > max_len:
                max_len = cur_len
            
            d[ele] = cur_len
            d[ele - left] = cur_len
            d[ele + right] = cur_len
    
    return max_len


def longestConsecutive_2(nums):
    if not nums:
        return 0
    
    d = {key: False for key in nums}
    max_len = 0
    for key in nums:
        if not d[key]:
            left_len = 0
            left_v = key - 1
            while left_v in d:
                left_len += 1
                d[left_v] = True
                left_v -= 1
            
            right_len = 0
            right_v = key + 1
            while right_v in d:
                right_len += 1
                d[right_v] = True
                right_v += 1
            
            max_len = max(max_len, 1+left_len+right_len)

    return max_len


nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [1,2,0,1]
print(longestConsecutive_2(nums))
