#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def longestPalindrome(s):
    max_sub = 0
    index = 0
    l = len(s)
    for i in range(l):
        # odd
        for j in range(l):
            if i - j >= 0 and i + j < l:
                if s[i - j] == s[i + j]:
                    if max_sub < 2*j + 1:
                        max_sub = 2*j + 1
                        index = i
                else:
                    break
        # even
        for j in range(l):
            if i - j >= 0 and i + 1 + j < l:
                if s[i - j] == s[i + 1 + j]:
                    if max_sub < (j + 1) * 2:
                        max_sub = (j + 1) * 2
                        index = i
                else:
                    break
    return s[(index-(max_sub-1)//2):(index-(max_sub-1)//2+max_sub)]


# s = "babad"
s = "aacabdkacaa"
print(longestPalindrome(s))
